import os

from character_creation import buy_supplies

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Type 1 is normal pause screen
# Type 2 is fort pause screen
def print_pause_screen(ch_data, pause_type=1):
    while True:
        clear_screen()
        print(f'''
    {f'{ch_data['month']}/{ch_data['day']}/{ch_data['year']}'.center(45)}
    Next Landmark: {ch_data['next_landmark']}, {ch_data['landmark_distance']} mi
    Distance to Oregon: {2000 - ch_data['distance']}
    Health: {ch_data['health']}
    Pace: {ch_data['pace']}
    Food Rations: {ch_data['rations']}''')
        if pause_type == 1:
            pause_screen_choice = input('''
        You may:
            1. Continue your journey
            2. Check Supplies
            3. Change Rations
            4. Change Pace
            5. Rest to improve health
            6. Hunt for food
        Your Choice: ''')
        else:
            pause_screen_choice = input('''
        You may:
            1. Continue your journey
            2. Check Supplies
            3. Change Rations
            4. Change Pace
            5. Rest to improve health
            6. Hunt for food
            7. Buy Supplies
        Your Choice: ''')
            
        if pause_screen_choice == '1':
            break
        elif pause_screen_choice == '2':
            check_supplies(ch_data)
        elif pause_screen_choice == '3':
            ch_data = change_rations(ch_data)
        elif pause_screen_choice == '4':
            ch_data = change_pace(ch_data)
        elif pause_screen_choice == '5':
            break
        elif pause_screen_choice == '6':
            break
        elif pause_type == 2:
            if pause_screen_choice == '7':
                purchase_output = buy_supplies(ch_data['money'], ch_data)
                money, oxen, food, ammunition, spare_parts = purchase_output.values()
                ch_data['money'] = money
                ch_data['supplies']['oxen']+=oxen
                ch_data['supplies']['food']+=food
                ch_data['supplies']['ammunition']+=ammunition
                ch_data['supplies']['spare_parts']+=spare_parts
        
        else:
            print('Invalid Command')
    return ch_data


def check_supplies(ch_data):
    print(f'''
    Oxen: {ch_data['supplies']['oxen']}
    Food: {ch_data['supplies']['food']}
    Ammunition: {ch_data['supplies']['ammunition']}
    Spare Parts: {ch_data['supplies']['spare_parts']}
''')
    input('Press "Enter" to continue')


def change_rations(ch_data):
    new_ration = input(f'''
    Change Rations-
    1. Filling - Large meals to increase health
    2. Meager - Smaller meals, but still adequate
    3. Bare-Bones - Very small meals, constant hunger
    Your Choice: ''')
    if new_ration == '1':
        ch_data['rations'] = 'filling'
    elif new_ration == '2':
        ch_data['rations'] = 'meager'
    elif new_ration == '3':
        ch_data['rations'] = 'bare-bones'
    return ch_data


def change_pace(ch_data):
    new_pace = input(f'''
    Change Rations-
    1. Slow - Isn't the fastest, but is good for health
    2. Medium - A good middle ground for speed and health
    3. Fast - Travel quickly, but you become extremely tired and your health suffers
    Your Choice: ''')
    if new_pace == '1':
        ch_data['pace'] = 'slow'
    elif new_pace == '2':
        ch_data['pace'] = 'medium'
    elif new_pace == '3':
        ch_data['pace'] = 'fast'
    return ch_data


if __name__ == "__main__":
    character_data = {
    'character_type' : 'banker',
    'name' : 'name',
    'money' : 500,
    'supplies' : {
        'oxen' : 3,
        'food' : 934,
        'ammunition' : 60,
        'spare_parts' : 4,
    },
    'distance': 0,
    'next_landmark': 'Kansas River Crossing',
    'landmark_distance': 100,
    'health': 8,
    'pace': 'slow',
    'rations': 'filling',
    'month': 3,
    'day': 1,
    'year': 1848
    } #19 lines for 1 var!!!!
    ch_data = print_pause_screen(character_data, 2)
    print(ch_data)

