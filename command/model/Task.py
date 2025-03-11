class Task:
    def __init__(self, name, description,time ,status):
        self.name = name
        self.description = description
        self.status = status
        time_str = time.split(" / ")
        self.time = time_str[1]
        self.dotw = time_str[0]

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "time": self.time,
            "dotw": self.dotw,
            "status": self.status
        }
    


    def __str__(self):
        return f"{self.name} - {self.description} - {self.dotw} - {self.time} - {self.status}"
    
    def updateStatus(self, status):
        self.status = status
    
