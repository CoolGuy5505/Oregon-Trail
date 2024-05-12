import random as rd
import time
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def new_day(ch_data):
    clear_screen()
    ch_data = update_date(ch_data)
    ch_data = update_food(ch_data)
    ch_data = update_health(ch_data)
    ch_data = update_distance(ch_data)
    ch_data = update_landmarks(ch_data)
    input(f'''
press "enter" to pause''')
    return ch_data

def update_date(ch_data):
    if ch_data['day'] < 30:
        ch_data['day'] += 1
    else:
        ch_data['day'] = 0
        if ch_data['month'] < 12:
            ch_data['month'] += 1
        else:
            ch_data['month'] = 1
            ch_data['year'] += 1
    return ch_data


def update_food(ch_data):
    #numbers may need balancing
    if ch_data['rations'] == 'filling':
        ch_data['supplies']['food'] -= rd.randint(12,18)
    elif ch_data['rations'] == 'meager':
        ch_data['supplies']['food'] -= rd.randint(8,12)
    elif ch_data['rations'] == 'bare-bones':
        ch_data['supplies']['food'] -= rd.randint(4,7)
    else:
        ch_data['rations'] = 'super_filling'
        ch_data['supplies']['food'] -= rd.randint(25,40)
    if ch_data['supplies']['food'] < 0:
        ch_data['health'] -= rd.randint(4,10) #NEEDS to be balanced
        ch_data['supplies']['food'] = 0
    return ch_data


def update_health(ch_data):
    pace = ch_data['pace']
    rations = ch_data['rations']
    health = ch_data['health']
    if ch_data['supplies']['food'] > 0:
        if rations == 'filling':
            if pace == 'slow':
                health += rd.randint(-3,6)
            if pace == 'medium':
                health += rd.randint(-4,5)
            if pace == 'fast':
                health += rd.randint(-5,4)
            else:
                pace = 'slow'
                health += rd.randint(-3,6)
        elif rations == 'meager':
            if pace == 'slow':
                health += rd.randint(-4,5)
            if pace == 'medium':
                health += rd.randint(-4,4)
            if pace == 'fast':
                health += rd.randint(-5,3)
            else:
                pace = 'slow'
                health += rd.randint(-4,5)
        elif rations == 'bare-bones':
            if pace == 'slow':
                health += rd.randint(-5,3)
            if pace == 'medium':
                health += rd.randint(-6,2)
            if pace == 'fast':
                health += rd.randint(-7,1)
            else:
                pace = 'slow'
                health += rd.randint(-4,5)
        #Available only through save-file editing or glitches
        else: 
            rations = 'super_filling'
            if pace == 'slow':
                pass
            if pace == 'medium':
                pass
            if pace == 'fast':
                pass
            else:
                pace = 'slow'
                pass
    if health <= 115:
        ch_data['health'] = health
    else:
        ch_data['health'] = 115
    ch_data['pace'] = pace
    ch_data['rations'] = rations
    return ch_data


def update_distance(ch_data):
    #numbers may need to be balanced
    pace = ch_data['pace']
    distance = ch_data['distance']
    if pace == 'slow':
        travel_distance = rd.randint(10,15) #20-base game
    elif pace == 'medium':
        travel_distance = rd.randint(15,25) #30-base game
    elif pace == 'fast':
        travel_distance = rd.randint(25,35) #40-base game
    else:
        pace = 'slow'
        travel_distance = rd.randint(10,15) #20-base game
    distance += travel_distance 
    ch_data['pace'] = pace
    ch_data['distance'] = distance
    return ch_data
        

def stop_at_landmark():
    pass

    
def set_distance_at_landmark(ch_data, landmark_pos, landmark_name):
    if ch_data['distance'] >= landmark_pos and landmark_name not in ch_data['reached_landmarks']:
        ch_data['distance'] = landmark_pos
        ch_data['reached_landmarks'].add(landmark_name)
        stop_at_landmark()
    if landmark_name not in ch_data['reached_landmarks']:
        ch_data['landmark_distance'] = landmark_pos - ch_data['distance']
        ch_data['next_landmark'] = landmark_name
    #ch_data = set_landmark_vars(ch_data, landmark_pos, landmark_name)
    return ch_data


def set_landmark_vars(ch_data, landmark_pos, landmark_name):
    if landmark_name not in ch_data['reached_landmarks']:
        ch_data['landmark_distance'] = landmark_pos - ch_data['distance']
        ch_data['next_landmark'] = landmark_name
    return ch_data
    
    
def update_landmarks(ch_data):
    
    LANDMARKS = [
        ('David River', 100),
        ('David Plains', 250),
        ('Chocolate Fort', 300),
        ('Candy RIver OF DOOM', 490),
        ('David River again', 555),
        ('Lonely Stone', 660),
        ("Pierre's General Store", 745),
        ('Mountain Lake- Home of the Legend', 850),
        ('Calico Desert', 960),
        ('Skull Cavern', 1000),
        ('TIny Rock', 1132),
        ('TIny Rock', 1200),
        ('TIny Rock', 1340),
        ('TIny Rock', 1500),
        ('TIny Rock', 1800),
        ('TIny Rock', 1900),
        ('TIny Rock', 2000),
    ]
    LANDMARKS.reverse()
    
    for landmark_name, landmark_pos in LANDMARKS:
        ch_data = set_distance_at_landmark(ch_data, landmark_pos, landmark_name)
        
    return ch_data


if __name__ == "__main__":
    ch_data = {
    'character_type' : 'banker',
    'name' : 'name',
    'money' : 500,
    'supplies' : {
        'oxen' : 3,
        'food' : 2000,
        'ammunition' : 60,
        'spare_parts' : 4,
    },
    'distance': 0,
    'next_landmark': 'David River',
    'landmark_distance': 100,
    'reached_landmarks':set(),
    'health': 90,
    'pace': 'medium',
    'rations': 'meager',
    'month': 12,
    'day': 28,
    'year': 1848
    } #19 lines for 1 var!!!!
    while True:
        ch_data = new_day(ch_data)
        print('Returned Data:')
        print(ch_data)
        confirmation = input('Continue?')
        if confirmation == 'n' or confirmation == 'no':
            break
