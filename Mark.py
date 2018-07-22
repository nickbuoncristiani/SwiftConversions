class Mark:
    
    def __init__(self, event, time, grade, year, date):
        self.event = event
        self.time = time
        self.year = year
        self.date = date
        self.grade = grade
        
    """Converts a time in xx:xx format to double format"""
    def getSeconds(self):
        if ':' in self.time:
            minutes = float('0' + self.time[0 : self.time.find(':')]) 
            seconds = float(self.time[self.time.find(':') + 1:])
            return minutes * 60 + seconds
        return float(self.time)
    