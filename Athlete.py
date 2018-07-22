class Athlete:
    
    def __init__(self, id, state):
        self.id = id
        self.state = state
        self.marks = set()
        
    """Adds (event, time) to marks dictionary"""
    def addMark(self, mark):
        self.marks.add(mark)
        
    """Adds all marks from another athlete to this one."""    
    def merge(self, athlete):
        for mark in athlete.marks:
            self.addMark(mark)
    
    """Finds a specific mark based on event, year"""
    def getMark(self, event, year):
        for mark in self.marks:
            if mark.event == event and mark.year == year:
                return mark
        return None
        
   
        
        
        