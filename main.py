import typer
import json


def main():
    '''Prompt for name and PIN
    '''
    user_name_input = typer.prompt('Enter your name')
    user_pin_input = typer.prompt('Enter PIN')
    typer.echo(f'{user_name_input}:{user_pin_input}')
    
    #Dictionary for user_name & user_pin
    user_credentials = {
        'Name:':user_name_input,
        'user_pin_input':user_pin_input
    }
    #check if user file exists, if not,m create it with empty state
    with open('user_credentials','w', encoding='utf-8') as file:
        json.dump(user_credentials, file, indent=4)
    
    # load user file with state
    with open('user_credentials','r', encoding='utf-8') as file:
        user_credentials = json.load(file)
            

    #main menu options
    typer.echo('You have [calories]/{calories_daily_target} today.')
    typer.echo('You have [calories]/[target] this week')
    typer.echo('Options:\n 1.Set calories target \n 2.Add calorie entry \n 3.Help \n 4.Quit')
            
    choice = typer.prompt('Enter option', type=int)
    
    match choice:
        case 1:
            typer.echo('Set calorie target')
            #set calories target & save to json file
            calorie_daily_target = typer.prompt('Set your daily target calorie', type=int)
            calorie_daily_target_data = {
                'Name':user_name_input,
                'Calories daily': calorie_daily_target
            }
            with open('calories_daily_target','w', encoding='utf-8') as file:
                json.dump(calorie_daily_target_data, file, indent=4)
            with open('calories_daily_target','r', encoding='utf-8') as file:
                calorie_daily_target_data = json.load(file)
                print(calorie_daily_target_data)
            
            
        case 2:
            typer.echo('Add calorie entry')
            
        case 3:
            typer.echo('Help')
        case 4:
            typer.echo('Quit')

    


        
        
        
    
    

if __name__ == "__main__":
    typer.run(main)