import requests

from pymtodo.list import ToDoList
from pymtodo.task import ToDoTask


class ToDoConnection:
    """
    Main class. Contains information about user and connection
    """
    
    # microsoft live urls
    _oauth20_url = 'https://login.live.com/oauth20_authorize.srf'
    _credential_url = "https://login.live.com/GetCredentialType.srf"
    _access_url = 'https://login.live.com/ppsecure/post.srf'
    
    # urls associated with apis
    _callback_url = 'https://to-do.microsoft.com/auth/callback'
    _scope_url = 'https://substrate.office.com/Todo-Internal.ReadWrite'
    _api_url = 'https://substrate.office.com/todo/api/v1/'
    
    # api specific values
    _client_id = '000000004C18365E'
    _pid = '15216'
    
    def __init__(self):
        """
        Init method of ToDoConnection class           
        """
        
        self._lists = []
    
    def _get_auth_tokens(self):
        """
        Gets MSPOK and PPFT tokens which are necessary for authentification
        
        Returns:
            MSPOK (str): MSPOK token
            PPFT (str): PPFT token
        """
        
        params = {
            'response_type': 'token',
            'client_id': self._client_id,
            'redirect_uri': self._callback_url,
            'scope': self._scope_url,
        }
        
        response = requests.get(url = self._oauth20_url, params = params)
        MSPOK = response.headers['Set-Cookie'].split('MSPOK=')[1].split(';')[0]
        PPFT = response.text.split('hidden')[1].split('value="')[1].split('"')[0]
        return MSPOK, PPFT
    
    def _check_email_credentials(self, email, MSPOK, PPFT):
        """
        Checks if email exists in Microsoft Live system. The check is done only 
        in the case in which authentification with entered email and password failed
        (in order to distinguish the incorrect email error from other errors)
        
        Args:
            email (str): User email
            MSPOK (str): MSPOK token
            PPFT (str): PPFT token
            
        Returns:
            bool: The return value. True if email exists, False otherwise
        """
        
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
            'Cookie': 'MSPOK=' + MSPOK,
        }
        
        data = {
            'username': email,
            'flowToken': PPFT,
        }
        
        response = requests.post(url = self._credential_url, headers = headers, data = str(data))        
        try:
            if_not_exist = response.json()['IfExistsResult']
        except:
            if_not_exist = True            
        return not if_not_exist
        
    
    def _get_access_tokens(self, email, password, MSPOK, PPFT):
        """
        Gets access tokens which are necessary for authorized requests to Microsoft To-Do
        
        Args:
            email (str): User email
            password (str): User password
            MSPOK (str): MSPOK token
            PPFT (str): PPFT token
            
        Returns:
            access_token (str): Access token for authorized requests
            access_token_type (str): Type of access token
            access_token_expires_in (int): Expiration time of access token
            user_id (str): User id        
        """
        
        headers = {
            'Content-type': 'application/x-www-form-urlencoded',
            'Cookie': 'MSPOK=' + MSPOK,
        }
        
        params = {
            'response_type': 'token',
            'client_id': self._client_id,
            'redirect_uri': self._callback_url,
            'scope': self._scope_url,
            'pid': self._pid,
        }
        
        data = {
            'login': email,
            'passwd': password,
            'PPFT': PPFT,
        }
        
        response = requests.post(url = self._access_url, headers = headers, params = params,
                                 data = data, allow_redirects = False)
        
        if 'Location' not in response.headers:
            if self._check_email_credentials(email, MSPOK, PPFT):
                raise Exception("Your password is incorrect")
            else:
                raise Exception("Email doesn't exist or not connected to To-Do account")
        
        access_info = response.headers['Location'].split('access_token=')[1].split('&')
        access_token = access_info[0]
        access_token_type = access_info[1].split('token_type=')[1]
        access_token_expires_in = access_info[2].split('expires_in=')[1]
        user_id = access_info[4].split('user_id=')[1]
        return access_token, access_token_type, access_token_expires_in, user_id
    
    def _get_lists(self):
        """
        Gets user lists (represented by ToDoList instances)
        
        Returns:
            list of ToDoLists: User lists
        """
        
        lists_url = self._api_url + 'taskfolders'
        
        headers = {
            'Authorization': self.access_token_type + ' ' + self.access_token,
            'X-AnchorMailbox': 'CID:' + self.user_id,
        }
        
        response = requests.get(url = lists_url, headers = headers)
        response_json = response.json()
        
        if 'Value' in response_json:
            self._lists = []
            for _dict in response_json['Value']:
                self._lists.append(ToDoList(self, _dict))
                
        return self._lists
    
    def _get_tasks(self, list_id):
        """
        Gets tasks in the list given list_id
        
        Args:
            list_id (int): Id of the list
        
        Returns:
            list: List of tasks in the list
        """
        
        tasks = []
        
        list_url = self._api_url + 'taskfolders/' + list_id + '/tasks'
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.access_token_type + ' ' + self.access_token,
            'X-AnchorMailbox': 'CID:' + self.user_id
        }
        
        response = requests.get(url = list_url, headers = headers)
        response_json = response.json()
        if 'Value' in response_json:
            for _dict in response_json['Value']:
                tasks.append(ToDoTask(self, _dict))
        return tasks
    
    def create_list(self, name):
        """
        Creates new list
        
        Args:
            name (str): Name of the list
            
        Returns:
            bool: The return value. True for success, False otherwise 
        """
        lists_url = self._api_url + 'taskfolders'
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.access_token_type + ' ' + self.access_token,
            'X-AnchorMailbox': 'CID:' + self.user_id
        }
            
        data = {
            'Name': name,
            'OrderDateTime': '1969-12-31T21:46:40.000Z',
            'ShowCompletedTasks': 'true',
            'ThemeColor': 'blue',
        }
        
        response = requests.post(url = lists_url, headers = headers, data = str(data))
        if response.status_code == 201:
            return True
        else:
            return False
        
    def _delete_list(self, list_id):
        """
        Deletes list by list_id
        
        Args:
            list_id (int): Id of the list
            
        Returns:
            bool: The return value. True for success, False otherwise 
        """
        
        list_url = self._api_url + 'taskfolders/' + list_id
        
        headers = {
            'Authorization': self.access_token_type + ' ' + self.access_token,
            'X-AnchorMailbox': 'CID:' + self.user_id
        }
        
        response = requests.delete(url = list_url, headers = headers)
        if response.status_code == 204:
            return True
        else:
            return False
    
    def _create_task(self, name, list_id, importance):
        """
        Creates new task
        
        Args:
            name (str): Name of the task
            list_id (int): Id of the list in which task should be created
            importance (str): Importance of the task
            
        Returns:
            bool: The return value. True for success, False otherwise
        """
        
        list_url = self._api_url + 'taskfolders/' + list_id + '/tasks'
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': self.access_token_type + ' ' + self.access_token,
            'X-AnchorMailbox': 'CID:' + self.user_id
        }
        
        data = {
            'ParentFolderId': list_id,
            'Subject': name,
            'OrderDateTime': '2017-09-25T21:43:45.000Z',
            'Importance': importance,
        }
        
        response = requests.post(url = list_url, headers = headers, data = str(data))
        if 'Id' in response.json():
            return True
        else:
            return False
        
    def _delete_task(self, task_id):
        """
        Deletes task by task_id
        
        Args:
            task_id (str): Id of the task to be deleted
            
        Returns:
            bool: The return value. True for success, False otherwise    
        """
        
        task_url = self._api_url + 'tasks/' + task_id
        
        headers = {
            'Authorization': self.access_token_type + ' ' + self.access_token,
            'X-AnchorMailbox': 'CID:' + self.user_id
        }
        
        response = requests.delete(url = task_url, headers = headers)
        if response.status_code == 204:
            return 1
        else:
            return 0
    
    @property
    def lists(self):
        """The same as _get_lists"""
        
        return self._get_lists()
        
    def connect(self, email, password):
        """
        Establishes the connection with Microsoft To-Do server
        
        Args:
            email (str): User email
            password (str): User password
        """
        
        MSPOK, flowToken = self._get_auth_tokens()
        self.access_token, self.access_token_type, self.access_token_expires_in, self.user_id = \
             self._get_access_tokens(email, password, MSPOK, flowToken)