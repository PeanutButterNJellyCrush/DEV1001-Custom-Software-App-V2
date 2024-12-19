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
    with open('user_name_pin_data','w', encoding='utf-8') as file:
        json.dump(user_credentials, file, indent=4)
    
    # load user file with state
    with open('user_name_pin_data','r', encoding='utf-8') as file:
            user_credentials = json.load(file)
            

    #main menu options
    typer.echo('You have [calories]/[target] today.')
    typer.echo('You have [calories]/[target] this week')
    typer.echo('Options:\n 1. Set calories target 2.Add calorie entry 3.Help 4.Quit')
            
    choice = typer.prompt('Enter option:', type=int)
    if choice == 1:
        typer.echo('Set calorie target')
    if choice == 2:
        typer.echo('Add calorie entry')
    if choice == 3:
        typer.echo('Help')
    if choice == 4:
        typer.echo('Quit')
    else:
        typer.echo('Invalid request. Please try again using the above options.')


        
        
        
    
    

if __name__ == "__main__":
    typer.run(main)