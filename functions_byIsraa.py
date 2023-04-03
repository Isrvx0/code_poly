import random
#       check winner :
def check_winner(points , place):
    winner = False
    if place == 100 or points >= 20:
        winner = True
    return winner


#       player dictionary :
def player_dictionary (player_name):
    dictionary = [{"name" : {player_name},
                   "position" : 0 ,
                   "points" : 0
                   }]


#       Choice player to start :
def started_player (players_list):
    random_radint = random.randint(0,len(players_list))
    player = players_list[random_radint]['name']
    return player


#       reminder position :
def reminder_position (player_name , player_lijst):
    position = 0
    for player in player_lijst:
        if player['name'] == player_name:
            position = player['position']
    return position


#       upgrade place :
def upgrade_place (player_name , player_lijst , duppel_steen):
    place = 0
    for player in player_lijst:
        if player['name'] == player_name:
            place = player['position'] + duppel_steen
    return place