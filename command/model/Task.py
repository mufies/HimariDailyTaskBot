class Task:
    def __init__(self,guildid,userid, name, description,time):
        self.userid = userid
        self.guildid = guildid
        self.name = name
        self.description = description
        self.time = time

        

    def to_dict(self):
        return {
            "guildid": self.guildid,
            "userid": self.userid,
            "name": self.name,
            "description": self.description,
            "time": self.time,

        }

    def __str__(self):
        return f"{self.name} - {self.description} - {self.time}"

    
