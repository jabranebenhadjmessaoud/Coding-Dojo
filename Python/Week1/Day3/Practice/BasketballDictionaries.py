players = [
    {
        "name": "Kevin Durant", 
        "age":34, 
        "position": "small forward", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Jason Tatum", 
        "age":24, 
        "position": "small forward", 
        "team": "Boston Celtics"
    },
    {
        "name": "Kyrie Irving", 
        "age":32,
        "position": "Point Guard", 
        "team": "Brooklyn Nets"
    },
    {
        "name": "Damian Lillard", 
        "age":33,
        "position": "Point Guard", 
        "team": "Portland Trailblazers"
    },
    {
        "name": "Joel Embiid", 
        "age":32,
        "position": "Power Foward", 
        "team": "Philidelphia 76ers"
    },
    {
        "name": "DeMar DeRozan",
        "age": 32,
        "position": "Shooting Guard",
        "team": "Chicago Bulls"
    }
]
class Player:
    #this is the constructor
    def __init__(self,index):
        self.name =players[index]["name"]
        self.age =players[index]["age"]
        self.position =players[index]["position"]
        self.team = players[index]["team"]
    def printname(self):
        print(f"the name is {self.name}")
    def printage(self):
        print(f"the age is {self.age}")

user1=Player(2)
user1.printname()
user1.printage()
    

    # def __init__(self, name, age, position, team):
    #     self.name = name
    #     self.age = age
    #     self.position = position
    #     self.team = team


