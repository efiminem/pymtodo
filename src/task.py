class ToDoTask:
    """
    Contains information about Task
    """
    def __init__(self, connection, task_dict):
        """
        Init method of ToDoTask class
        
        Args:
            connection (ToDoConnection): Parent ToDoConnection instance
            task_dict (dict): Description of ToDoTask            
        """
        
        self._connection = connection
        self.change_key = task_dict['ChangeKey']
        self.committed_day = task_dict['CommittedDay']
        self.committed_order = task_dict['CommittedOrder']
        self.completed_date_time = task_dict['CompletedDateTime']
        self.created_date_time = task_dict['CreatedDateTime']
        self.due_date_time = task_dict['DueDateTime']
        self.id = task_dict['Id']
        self.is_ignored = task_dict['IsIgnored']
        self.is_imported = task_dict['IsImported']
        self.is_reminder_on = task_dict['IsReminderOn']
        self.last_modified_date_time = task_dict['LastModifiedDateTime']
        self.order_date_time = task_dict['OrderDateTime']
        self.postponed_day = task_dict['PostponedDay']
        self.recurrence = task_dict['Recurrence']
        self.reminder_date_time = task_dict['ReminderDateTime']
        self.status = task_dict['Status']
        self.subject = task_dict['Subject']
        self.source = task_dict['Source']
        self.all_extensions = task_dict['AllExtensions']
        self.importance = task_dict['Importance']
        self.created_by_user = task_dict['CreatedByUser']
        self.completed_by_user = task_dict['CompletedByUser']
        
    def delete(self):
        """
        Deletes current task
        
        Returns:
            bool: the return value. True for success, False otherwise            
        """
        
        return self._connection._delete_task(self.id)
        
    def _assign_parent(self, parent):
        """
        Used to assign parent ToDoList instance for ToDoTask instance
        
        Args:
            parent (ToDoTask): parent ToDoTask instance            
        """
        
        self.parent = parent
        
    def __repr__(self):
        """
        String representation of an instance
        
        Returns:
            str: string representation            
        """
        
        return "ToDoTask <{}>".format(self.subject)