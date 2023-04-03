from data_byIsraa import *
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


#       upgrade points :
def upgrade_place (player_name , player_lijst , answer):
    points = 0
    for player in player_lijst:
        if player['name'] == player_name:
            if answer:
                points = player['points'] + 1
    return points


#       check questions :
def check_questions (player_place):
    questions = '' 
    if player_place in check_easy_questions:
        questions = 'easy'
    elif player_place in check_medium_questions:
        questions = 'medium'
    elif player_place in check_hard_questions:
        questions = 'hard'
    else:
        questions = 'nothing'
    
    return questions 


#       check questions :
