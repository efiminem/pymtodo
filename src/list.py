class ToDoList:
    """
    Contains information about List
    """
    def __init__(self, connection, list_dict):
        """
        Init method of ToDoList class
        
        Args:
            connection (ToDoConnection): Parent ToDoConnection instance
            list_dict (dict): Description of ToDoList            
        """
        
        self._connection = connection
        self.change_key = list_dict['ChangeKey']
        self.id = list_dict['Id']
        self.is_default_folder = list_dict['IsDefaultFolder']
        self.is_shared_folder = list_dict['IsSharedFolder']
        self.is_owner = list_dict['IsOwner']
        self.name = list_dict['Name']
        self.order_date_time = list_dict['OrderDateTime']
        self.sharing_link = list_dict['SharingLink']
        self.show_completed_tasks = list_dict['ShowCompletedTasks']
        self.sort_ascending = list_dict['SortAscending']
        self.sort_type = list_dict['SortType']
        self.sync_status = list_dict['SyncStatus']
        self.sharing_status = list_dict['SharingStatus']
        
    
    def delete(self):
        """
        Deletes current list
        
        Returns:
            bool: The return value. True for success, False otherwise            
        """
        
        return self._connection._delete_list(self.id)
    
    def create_task(self, name, importance = 'Normal'):
        """
        Creates new task in the current list
        
        Args:
            name (str): name of the task
            importance (str): importance of the task
        """
        
        return self._connection._create_task(name, self.id, importance)
    
    def _get_tasks(self):
        """
        Gets tasks in the current list
        
        Returns:
            list: List of tasks in the current list
        """
        
        self._tasks = self._connection._get_tasks(self.id)
        for task in self._tasks:
            task._assign_parent(self)
        return self._tasks
        
    @property
    def tasks(self):
        """The same as _get_tasks."""
        
        return self._get_tasks()
        
    def __repr__(self):
        """
        String representation of an instance
        
        Returns:
            str: string representation            
        """
        
        return "ToDoList <{}>".format(self.name)