class DailyTask:
    def __init__(self,userid, name, description,time):
        self.userid = userid
        self.name = name
        self.description = description
        time_str = time.split(" / ")
        self.time = time_str[1]
        self.dotw = time_str[0]
        

    def to_dict(self):
        return {
            "userid": self.userid,
            "name": self.name,
            "description": self.description,
            "time": self.time,
            "dotw": self.dotw,
        }
    


    def __str__(self):
        return f"{self.name} - {self.description} - {self.dotw} - {self.time}"

    
