import json
from datetime import date
import typer

app = typer.Typer()

class FileManager:
    def load_json(filename):
        try:
            with open(filename, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return None

    def save_json(data, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

class UserManager:
    def __init__(self):
        self.user_details = {}

    def authenticate_user(self, username, pin):
        stored_data = FileManager.load_json('user_details.json')
        if stored_data and stored_data == {'Name': username, 'PIN': pin}:
            typer.echo('Log-in details verified. Welcome back!')
            self.user_details = stored_data
            return True
        else:
            self.user_details = {'Name': username, 'PIN': pin}
            FileManager.save_json(self.user_details, 'user_details.json')
            typer.echo('New log-in details saved!')
            return True

class CalorieTracker:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.calorie_target = None
        self.today_entry = {}

    def set_calorie_target(self):
        calorie_daily_target = int(typer.prompt('Set your daily target calorie: '))
        today = date.today().isoformat()
        calorie_daily_target_data = {
            'Name': self.user_manager.user_details['Name'],
            'Calories daily': calorie_daily_target,
            'Date': today
        }
        FileManager.save_json(calorie_daily_target_data, 'calories_daily_target_data.json')
        self.calorie_target = calorie_daily_target
        typer.echo(f'Calorie target {calorie_daily_target} for {today} has been updated!')

    def add_calorie_entry(self):
        calories_total_data = int(typer.prompt('Add to today entry: '))
        stored_data = FileManager.load_json('calories_total_data.json')
        if stored_data:
            self.today_entry = stored_data
        else:
            today = date.today().isoformat()
            self.today_entry = {'date': today, 'calories': []}

        self.today_entry['calories'].append(calories_total_data)
        FileManager.save_json(self.today_entry, 'calories_total_data.json')
        typer.echo('calories saved')
        typer.echo(f"Calories added today: {self.today_entry['calories']}")
        total_today = sum(self.today_entry['calories'])
        typer.echo(f"Total calories consumed today: {total_today}")

def show_menu():
    typer.echo("\nOptions:")
    typer.echo(" 1. Set calories target")
    typer.echo(" 2. Add calorie entry")
    typer.echo(" 3. Help")
    typer.echo(" 4. Quit")

@app.command()
def login(username: str = None, pin: str = None):
    if username is None:
        username = typer.prompt("Enter your name")
    if pin is None:
        pin = typer.prompt("Enter your PIN", hide_input=True, confirmation_prompt=True)

    user_manager = UserManager()
    if user_manager.authenticate_user(username, pin):
        while True:
            show_menu()
            choice = typer.prompt("Enter option: ")
            
            if choice == "1":
                calorie_tracker = CalorieTracker(user_manager)
                calorie_tracker.set_calorie_target()
            elif choice == "2":
                calorie_tracker = CalorieTracker(user_manager)
                calorie_tracker.add_calorie_entry()
            elif choice == "3":
                typer.echo('Follow the menu instructions to track and view your calories')
            elif choice == "4":
                typer.echo('Quitting...')
                break
            else:
                typer.echo('Invalid option. Please choose a valid option.')

@app.command()
def help():
    typer.echo('Follow the menu instructions to track and view your calories')

@app.callback(invoke_without_command=True)
def root(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        login()

if __name__ == "__main__":
    app()
