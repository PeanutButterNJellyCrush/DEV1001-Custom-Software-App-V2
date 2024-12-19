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
    typer.echo('You have [calories]/[target] today.')
    typer.echo('You have [calories]/[target] this week')
    typer.echo('Options:\n 1. Set calories target 2.Add calorie entry 3.Help 4.Quit')
            
    choice = typer.prompt('Enter option', type=int)
    
    match choice:
        case 1:
            typer.echo('Set calorie target')
        case 2:
            typer.echo('Add calorie entry')
        case 3:
            typer.echo('Help')
        case 4:
            typer.echo('Quit')



        
        
        
    
    

if __name__ == "__main__":
    typer.run(main)