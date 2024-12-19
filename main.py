import typer
import json


def main():
    user_name_input = typer.prompt("What's your name?")
    print(f'Hello {user_name_input}')
    user_pin_input = typer.prompt('Enter PIN')
    typer.echo(user_pin_input)
    #user_pin_input=hashlib.sha256(user_pin.encode()).hexdigest()           hashedpin
    user_credentials = {
        'Name:':user_pin_input,
        'user_pin_input':user_pin_input
    }
    try:
        with open('user_name_pin_data','r', encoding='utf-8') as file:
            user_credentials = json.load(file)
    except FileNotFoundError:
        user_name_pin_data.append(user_credentials)
        
    with open('user_name_pin_data','w', encoding='utf-8') as file:
        json.dump(user_credentials, file, indent=4)
        
        
        
    
    

if __name__ == "__main__":
    typer.run(main)