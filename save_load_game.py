import json

def save_game_file(game_state, filepath):
    with open(filepath, 'w') as file:
        json.dump(game_state, file)

def save_game(data):
    save_game_file(data, 'Oregon_Trail_Save.davidfile')
    
def load_game(file_path):
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Save file not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding the file. Invalid save file.")
        return None

if __name__ == '__main__':
    choice = input('save or load? ')
    if choice == 'save':
        overwrite = input('This will overwrite any existing file, continue [y/n] ')
        if overwrite == 'y' or overwrite == 'yes':
            save_game({
        'character_type' : 'banker',
        'name' : 'name',
        'money' : 500,
        'supplies' : {
            'oxen' : 3,
            'food' : 934,
            'ammunition' : 60,
            'spare_parts' : 4,
        },
        'distance':0,
        'next_landmark': 'Kansas River Crossing',
        'landmark_distance': 100,
        'health':8,
        'pace':'steady',
        'rations':'filling',
        'month':3,
        'day':1,
        'year':1848
        } #19 lines for 1 var!!!!
                    )
    elif choice == 'load':
        character_data = load_game('Oregon_Trail_Save.davidfile')
        print(character_data)
    else:
        print('Invalid Command')