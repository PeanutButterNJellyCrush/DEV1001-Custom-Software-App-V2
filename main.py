import json
from datetime import date


def main():
    
    user_name_input = str(input('Enter your name'))
    user_pin_input = int(input('Enter PIN'))
    
    #Dictionary for user_name & user_pin
    user_credentials_input = {
        'Name:':user_name_input,
        'PIN':user_pin_input
    }
    print(user_credentials_input)

    user_credentials = {
    }
        
    try:     
    #check if user file exists      
        with open('user_credentials.json','r', encoding='utf-8') as file:
            user_credentials = json.load(file)
            
        if user_credentials == user_credentials_input:
            print('login details present')
            with open('user_credentials.json','w', encoding='utf-8') as file:
                    json.dump(user_credentials, file, indent=4)    
        else:
            print('no valid login details.')
    #if not, create one
    except FileNotFoundError:
        print('error')


    #main menu options
    print('You have [calories]/ today.')
    print('You have [calories]/[target] this week')
    print('Options:\n 1.Set calories target \n 2.Add calorie entry \n 3.Help \n 4.Quit')
            
    choice = int(input('Enter option'))
    
    match choice:
        case 1:
            print('Set calorie target')
            #set calories target & save to json file
            calorie_daily_target = int(input('Set your daily target calorie'))
            today = date.today().isoformat()
            
            calorie_daily_target_data = {
                'Name':user_name_input,
                'Calories daily': calorie_daily_target,
                'Date': today
            }
            #open file to check if name and calories daily match
            with open('calories_daily_target','r', encoding='utf-8') as file:
                calorie_daily_target_data = json.load(file)
                print(calorie_daily_target_data)
                
            #iterate though data to check
            for entry in calorie_daily_target:
                print(entry)
            for entry in calorie_daily_target.entry():
                print(entry)
                
                
                # for entry in calorie_daily_target_data:
                #     if entry.get('Name') == user_name_input:
                #         if 'Calories daily' in entry:
                #             return True, entry['Calories daily']
                #         else: #if not found, write into file
                #             with open('calories_daily_target','w', encoding='utf-8') as file:
                #                 json.dump(calorie_daily_target_data, file, indent=4)
                 
                # print('data match')

            
        case 2:
            print('Add calorie entry')
            #add calories to the day & save to json file
            calories_entry = int(input('Enter calories you would like to add today', type=int))
            print(calories_entry)
            today = date.today().isoformat()
            print(today)
            calories_entry_today = {
                'Date': 'date today',
                'Calories to add':calories_entry
            }
            with open('calories_entry_today','w', encoding='utf-8') as file:
                json.dump(calories_entry_today, file, indent=4)
            with open('calories_entry_today','r', encoding='utf-8') as file:
                calories_entry_today = json.load(file)
                print(calories_entry_today)
        case 3:
            print('Help')
            print('Follow the menu instructions to track and view your calories')
            return_to_menu = ('Enter any key to return to menu')
        case 4:
            print('Quit')
            
            
if __name__ == "__main__":
    main()