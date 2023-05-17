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
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

    # display objects
    def __repr__(self):
        display = f"\n Player: {self.name}, {self.age} y/o, pos: {self.position}, team: {self.team} \n"
        return display
    
# player1 = Player()
# print(player1)
# kevin = {
#     	"name": "Kevin Durant", 
#     	"age":34, 
#     	"position": "small forward", 
#     	"team": "Brooklyn Nets"
# }
# jason = {
#     	"name": "Jason Tatum", 
#     	"age":24, 
#     	"position": "small forward", 
#     	"team": "Boston Celtics"
# }
# kyrie = {
#     	"name": "Kyrie Irving", 
#     	"age":32,
#         "position": "Point Guard", 
#     	"team": "Brooklyn Nets"
# }
# player_jason = Player(jason)
# print(player_jason)
# player_kyrie = Player(kyrie)
# print(player_kyrie)
# player_kevin = Player(kevin)
# print(player_kevin)
new_team = []
for i in range(0,len(players)):
    print(players[i]["name"],players[i]["age"],players[i]["position"],players[i]["team"])
    new_team.append(Player(players[i]["name"],players[i]["age"],players[i]["position"],players[i]["team"]))

print(new_team)