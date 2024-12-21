import json
from datetime import date


def main():
    
    user_name_input = (input('Enter your name: ' ))
    user_pin_input = (input('Enter PIN: ' ))
    
    #Dictionary for user_name & user_pin
    user_credentials_input = {
        'Name:':user_name_input,
        'PIN':user_pin_input
    }
    print(user_credentials_input)
    
    # user_credentials = {
    #     'Name:':'bonnie',
    #     'PIN':'456'
    # } debugging purposes
        
    try:     
    #check if user file exists      
        with open('user_credentials.json','r', encoding='utf-8') as file:
            user_credentials = json.load(file)
            
        if user_credentials == user_credentials_input:
            print('login details present')

        else:
            with open('user_credentials.json','w', encoding='utf-8') as file:
                json.dump(user_credentials_input, file, indent=4)   
        print('login saved') 

    except FileNotFoundError:
        print('error')


    #main menu options
    print('You have [calories]/ [{calorie_daily_target}]today.')
    print('Options:\n 1.Set calories target \n 2.Add calorie entry \n 3.Help \n 4.Quit')
            
    choice = int(input('Enter option: '))
    
    match choice:
        case 1:
            #set calories target & save to json file
            calorie_daily_target = (input('Set your daily target calorie: '))
            today = date.today().isoformat()
            
            calorie_daily_target_data = {
                'Name':user_name_input,
                'Calories daily': calorie_daily_target,
                'Date': today
            }
            try:
            #read & write to file
                with open('calories_daily_target.json','r', encoding='utf-8') as file:
                    calorie_daily_target_data = json.load(file)
                    
                    while True:
                        calorie_daily_target_data['Calories daily'] += calorie_daily_target
                    
                        print({today})
                        break

                with open('calories_daily_target.json', 'w', encoding='utf-8') as file:
                    json.dump(calorie_daily_target_data, file, indent=4)
                    print(f'Calorie target {calorie_daily_target} has been updated!')
            
            except FileNotFoundError:
            # If file doesn't exist, create it with new data
                with open('calories_daily_target.json', 'w', encoding='utf-8') as file:
                    json.dump(calorie_daily_target_data, file, indent=4)
                    print(f'Calorie target {calorie_daily_target} has been updated.')
            finally: 
                print('xxxxxx')
                #add method/function to return to menu or quit 
            

            
        case 2:
            print('Add calorie entry')
            #add calories to the day & save to json file
            calories_entry = (input('Enter calories you would like to add today.' ))
            print(calories_entry)
            today = date.today().isoformat()
            print(today)
            
            
            calories_entry_today = {
                'Date': 'date today',
                'Calories to add':calories_entry
            }
            
            try:
                with open('calories_entry_today.json','w', encoding='utf-8') as file:
                    json.dump(calories_entry_today, file, indent=4)
                with open('calories_entry_today','r', encoding='utf-8') as file:
                    calories_entry_today = json.load(file)
                print(calories_entry_today) 
            finally:
                print('xxxxxxx')
            
        case 3:
            print('Help')
            print('Follow the menu instructions to track and view your calories')
            return_to_menu = ('Enter any key to return to menu')
     
        
        case 4:
            print('Quit')
            quit()
            
            
if __name__ == "__main__":
    main()