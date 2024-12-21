import json
from datetime import date
import rich

def main():
   
    user_name_input = (input('Enter your name: ' ))
    user_pin_input = (input('Enter your PIN: ' ))

    #Dictionary for user_name & user_pin
    user_details_input = {
        'Name:':user_name_input,
        'PIN':user_pin_input
    }
    print(user_details_input)
        
    try:     
    #check if user file exists in user details   
        with open('user_details.json','r', encoding='utf-8') as file:
            user_details_data= json.load(file)#read as user_dtails_data for python
            print(user_details_data)#print
            
            if user_details_data == user_details_input:
                print('Log-in details verified. Welcome back!')#check if the same details present

        with open('user_details.json','w', encoding='utf-8') as file:#open json file and write input details to it
                json.dump(user_details_input, file, indent=4)   
                print('New log-in details saved!') 

    except FileNotFoundError:#if the file is not found 
        with open('user_details.json','w', encoding='utf-8') as file:#open json file and write input details to it
            json.dump(user_details_input, file, indent=4)   
            print('Login saved finally')


    #main menu options
    print('You have {calorie_daily_target} today.') #create classes and methods to pass calories_daily_target to this output display.
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

            calories_entry = int(input('Enter calories you would like to add today: '))
            print(calories_entry)
            today = date.today().isoformat()
            print(today)
            
            calories_list = [0] #store calories_entry as an array 
            calories_list.append(calories_entry)
            print(calories_list)
            total_calories_consumed_today = (sum(calories_list))

            calories_entry_today = {
                'Date': today,
                'Calories to add':calories_entry, #input from user at the present moment 
                'Total calories consumed today': total_calories_consumed_today
            }
            try:
                #read file, if no file
                with open('total_calories_consumed_today','r', encoding='utf-8') as file:
                    total_calories_consumed_today = json.load(file)
                    print(f'total calories file found: {total_calories_consumed_today} ')
                #if no file, make file and add to file   
            except FileNotFoundError:
                with open('total_calories_consumed_today.json','w', encoding='utf-8') as file:
                    json.dump(total_calories_consumed_today, file, indent=4)
                    print(f'total_calories_comsumed_today file created: {total_calories_consumed_today}')
                    
                print(f'You have successfully added: {calories_entry_today} to your account today.') 
                print(f'Total calories consumed today: {total_calories_consumed_today}')
            finally:
                print('xxxxxxx')#test purposes
                #to add return to main menu or quit method 
            
        case 3:
            print('Help')
            print('Follow the menu instructions to track and view your calories')
            return_to_menu = ('Enter any key to return to menu')
     
        
        case 4:
            print('Quit')
            quit()
            
            
if __name__ == "__main__":
    main()