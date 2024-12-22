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
            
            else:
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
            calorie_daily_target = int(input('Set your daily target calorie: '))
            today = date.today().isoformat()
            
            calorie_daily_target_data = {
                'Name':user_name_input,
                'Calories daily': calorie_daily_target,
                'Date': today
            }
            
            try:
            #write to file
        
                with open('calories_daily_target_data.json', 'w', encoding='utf-8') as file:
                    json.dump(calorie_daily_target_data, file, indent=4)
                    print(f'Calorie target {calorie_daily_target} for {today} has been updated!')
                    print({'Calories daily' in calorie_daily_target_data})
            
            except FileNotFoundError:
            # If file doesn't exist, create it with new data
                with open('calories_daily_target_data.json', 'w', encoding='utf-8') as file:
                    json.dump(calorie_daily_target_data, file, indent=4)
                    print(f'Calorie target {calorie_daily_target} has been updated.')
            finally: 
                print('return to main menu')
                #add method/function to return to menu for options
        
        case 2:
            today = date.today().isoformat()#today date
            calories_entry = int(input('Add to today entry: '))
            
            try:
                with open('calories_total_data.json','r',encoding='utf-8') as file:
                    calories_data = json.load(file)#assign name to file when loads
                    
            except FileNotFoundError:
                calories_data = {'calories':[].append(calories_entry)}#assigning dictionary to variable
                print(calories_data)
                
                
                
                
                today_entry = {'date':today, 'calories':[]}#dictionary variable
                calories_data.append(today_entry)#appended to calories total data
                today_entry['calories'].append(calories_data)  # appended to calories total data
                calories_data = {'Calorie entry':[]}  
             
            with open('calories_total_data.json', 'w', encoding='utf-8') as file:
                    json.dump(calories_data, file, indent=4)
                    print(calories_data)

            
        case 3:
            print('Help')
            print('Follow the menu instructions to track and view your calories')
            #to do return_to_menu = ('Enter any key to return to menu')
     
        
        case 4:
            print('Quit')
            
            
if __name__ == "__main__":
    main()