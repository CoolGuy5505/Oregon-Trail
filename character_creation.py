import os
from utils import *

from my_coloring import *

# print(color.cl, end='')


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    input('Press "Enter" to continue ')

def select_character_type():
    print_option_4 = False
    while True:
        clear_screen()
        character_type = ''
        print(f'''Select Your Character!
    You may:{color.choices}
        1. Be a banker
        2. Be a carpenter
        3. Be a farmer
        4. Find out the differences 
           between these choices{color.cl}
          ''')
        if print_option_4:
            print('''Bankers receive $1600 cash, but do not get a point bonus
    Carpenters receive $800 cash, and get a 2x points bonus
    Farmers receive $400 but get a 3x point bonus
                ''')
        character_type_choice = input(f'What is your choice? {color.input}')
        print(color.cl, end='')
        if character_type_choice == '1':
            character_type = confirm_character_type('banker')
            print_option_4 = False
        elif character_type_choice == '2':
            character_type = confirm_character_type('carpenter')
            print_option_4 = False
        elif character_type_choice == '3':
            character_type = confirm_character_type('farmer')
            print_option_4 = False
        elif character_type_choice == '4':
            print_option_4 = True
        else:
            invalid()
            press_enter()
            print_option_4 = False
        if character_type != '':
            break
    return character_type


def confirm_character_type(character_type):
    confirm_character_selection_text = input(f'Are you sure you want to be a {color.data+character_type+color.cl} [y/n] {color.input}')
    print(color.cl, end='')
    if confirm_character_selection_text.lower() == 'y' or confirm_character_selection_text.lower() == 'yes':
        return character_type
    else:
        return ''


def name_character():
    while True:
        clear_screen()
        name = input(f'What is you name? {color.input}')
        print(color.cl, end='')
        confirm_name_selection = input(f'Is you name {color.data+name+color.cl}? [y/n] {color.input}')
        print(color.cl, end='')
        if confirm_name_selection.lower() == 'y' or confirm_name_selection.lower() == 'yes': 
            return name
            break
    
    
def buy_supplies(money, ch_data=None):
    clear_screen()
    print(f"You have {color.money}${money}{color.cl} to spend, but you don't have to use all of it right now")
    if ch_data == None:
        print(f'''I recommend buying at least:
5 oxen
1000 lbs of food
5-10 boxes of bullets
6 spare parts{color.cl}''')
    print('')
    press_enter()
    
    oxen_bill = 0
    food_bill = 0
    ammunition_bill = 0
    spare_parts_bill = 0
    
    oxen = 0
    food = 0
    ammunition = 0
    spare_parts = 0
    
    while True:
        clear_screen()
        print(f'''David's general store-
1. Oxen             ${oxen_bill}
2. Food             ${food_bill}
3. Ammunition       ${ammunition_bill}
4. Spare Parts      ${spare_parts_bill}
5. Leave Store

Total Bill          ${oxen_bill + food_bill + ammunition_bill + spare_parts_bill}

You Have            ${money}
''')
        purchase_choice = input('What item would you like to buy? ')
        #User chooses to buy ox
        if purchase_choice == '1':
            if oxen_bill > 0:
                money += oxen_bill
            result_of_oxen_purchase = purchase('oxen', 20, money)
            oxen_bill = result_of_oxen_purchase['amount_of_item'] * 20
            money = result_of_oxen_purchase['money']
            oxen = result_of_oxen_purchase['amount_of_item']
        #User chooses to buy food
        elif purchase_choice == '2':
            if food_bill > 0:
                money += food_bill
            result_of_food_purchase = purchase('food', 0.20, money)
            food_bill = result_of_food_purchase['amount_of_item'] * 0.20
            money = result_of_food_purchase['money']
            food = result_of_food_purchase['amount_of_item']
        #User chooses to buy ammunition
        elif purchase_choice == '3':
            if ammunition_bill > 0:
                money += ammunition_bill
            result_of_ammunition_purchase = purchase('ammunition', 2, money)
            ammunition_bill = result_of_ammunition_purchase['amount_of_item'] * 2
            money = result_of_ammunition_purchase['money']
            ammunition = result_of_ammunition_purchase['amount_of_item'] * 20
        elif purchase_choice == '4':
            if spare_parts_bill > 0:
                money += spare_parts_bill
            result_of_spare_parts_purchase = purchase('spare_parts', 10, money)
            spare_parts_bill = result_of_spare_parts_purchase['amount_of_item'] * 2
            money = result_of_spare_parts_purchase['money']
            spare_parts = result_of_spare_parts_purchase['amount_of_item']
        elif purchase_choice == '5':
            if ch_data == None:
                if food > 2000:
                    print('You cannot carry more than 2000 lbs of food')
                    press_enter()
                elif spare_parts > 7:
                    print('You cannot carry more than 7 spare parts')
                    press_enter()
                elif oxen < 1:
                    print('You cannot travel without oxen!')
                    press_enter()
                else:
                    confirm_purchase = input('Are you finished with your purchases? [y/n] ')
                    if confirm_purchase.lower() == 'y' or confirm_purchase.lower() == 'yes':
                        break
            else:
                if food + ch_data['supplies']['food'] > 2000:
                    print('You cannot carry more than 2000 lbs of food')
                    print(f'{food + ch_data['supplies']['food']} is more than 2000')
                    press_enter()
                elif spare_parts + ch_data['supplies']['spare_parts'] > 7:
                    print('You cannot carry more than 7 spare parts')
                    print(f'{spare_parts + ch_data['supplies']['spare_parts']} is more than 7')
                    press_enter()
                elif oxen + ch_data['supplies']['oxen'] < 1:
                    print('You cannot travel without oxen!')
                    press_enter()
                else:
                    confirm_purchase = input('Are you finished with your purchases? [y/n] ')
                    if confirm_purchase.lower() == 'y' or confirm_purchase.lower() == 'yes':
                        break
            
    output = {
        'money' : money,
        'oxen' : oxen,
        'food' : food,
        'ammunition' : ammunition,
        'spare_parts' : spare_parts
    }
    return output


def purchase(item, cost, total_funds):
    while True:
        try:
            if item != 'food' and item != 'ammunition':
                amount_of_item = int(input(f'How many {item} would you like? Each cost ${cost} '))
            elif item == 'food':
                amount_of_item = int(input(f'How many lbs of food would you like? Each lb costs ${cost} '))
            elif item == 'ammunition':
                amount_of_item = int(input(f'How many boxes of ammunition would you like? There are 20 bullets per box. Each box costs ${cost} '))            
            if amount_of_item < 0:
                print('Please enter a positive integer')
            elif amount_of_item * cost < total_funds:
                total_funds -= cost * amount_of_item
                result = {
                'money': total_funds,
                'amount_of_item' : amount_of_item
                }
                return result
            else:
                print('insufficient funds')
        except ValueError:
            print('Please enter a positive integer')
    

def create_default_vars(character_type):
    if character_type == 'banker':
        health = 8
    elif character_type == 'carpenter':
        health = 10
    elif character_type == 'farmer':
        health = 12
    pace = 'slow'
    rations = 'filling'
    month = 3
    day = 1
    year = 1848
    distance = 2000
    next_landmark = 'Kansas River Crossing'
    landmark_distance = 100
    default_vars = {
        'distance':distance,
        'next_landmark':next_landmark,
        'landmark_distance':landmark_distance,
        'health':health,
        'pace':pace,
        'rations':rations,
        'month':month,
        'day':day,
        'year':year
    }
    return default_vars

def set_ch_money(character_type):
    if character_type == 'banker':
        money = 1600
    elif character_type == 'carpenter':
        money = 800
    elif character_type == 'farmer':
        money = 400
    else:
        while True:    
            error_response_selection = input('Something went wrong... restart from beginning? [y/n] ')
            if error_response_selection != 'n' and error_response_selection != 'no':
                return 'Error'
    return money


def create_character():
    character_type = select_character_type()
    name = name_character()
    money = int(set_ch_money(character_type))
    supplies = buy_supplies(money)
    if money == 'Error':
        create_character()
    money, oxen, food, ammunition, spare_parts = supplies.values()
    default_vars = create_default_vars(character_type)
    distance, next_landmark, landmark_distance, health, pace, rations, month, day, year = default_vars.values()
    character_data = {
        'character_type' : character_type,
        'name' : name,
        'money' : money,
        'supplies' : {
            'oxen' : oxen,
            'food' : food,
            'ammunition' : ammunition,
            'spare_parts' : spare_parts,
        },
        'distance':distance,
        'next_landmark':next_landmark,
        'landmark_distance':landmark_distance,
        'landmarks_reached':set(),
        'health':health,
        '-_health_mod': 1,
        '+_health_mod': 1,
        'pace':pace,
        'rations':rations,
        'month':month,
        'day':day,
        'year':year
    }
    return character_data


if __name__ == "__main__":
    create_character()