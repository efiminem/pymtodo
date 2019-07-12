class ToDoSubTask:
    """
    Contains information about SubTask
    """
    def __init__(self, connection, subtask_dict):
        """
        Init method of ToDoSubTask class
        
        Args:
            connection (ToDoConnection): Parent ToDoConnection instance
            subtask_dict (dict): Description of ToDoSubTask
        """
        
        self._connection = connection
        self.subject = subtask_dict['Subject']
        self.completed_date_time = subtask_dict['CompletedDateTime']
        self.created_date_time = subtask_dict['CreatedDateTime']
        self.id = subtask_dict['Id']
        self.is_completed = subtask_dict['IsCompleted']
        
    def delete(self):
        """
        Deletes current subtask
        
        Returns:
            bool: the return value. True for success, False otherwise            
        """
        
        return self._connection._delete_subtask(self.parent.id, self.id)
    
    def _assign_parent(self, parent):
        """
        Used to assign parent ToDoTask instance for ToDoSubTask instance
        
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
        
        return "ToDoSubTask <{}>".format(self.subject)