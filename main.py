import json
from datetime import date
import rich
from typing import List, Dict
import typer

app = typer.Typer()

class User:
    def __init__(self, name: str, pin: str):
        self.name = name
        self.pin = pin

class CalorieTracker:
    def __init__(self, user: User):
        self.user = user
        self.calorie_daily_target = 2000  # Default value
        self.entries: List[Dict] = []

    def set_calorie_target(self):
        while True:
            try:
                self.calorie_daily_target = int(typer.prompt("Set your daily calorie target: "))
                if self.calorie_daily_target <= 0:
                    raise ValueError
                self.save_calorie_target()
                typer.echo(f"Daily calorie target set to {self.calorie_daily_target}.", color="green")
                break
            except ValueError:
                typer.echo("Please enter a positive integer.", color="red")

    def add_calorie_entry(self):
        while True:
            try:
                today = date.today().isoformat()
                calories = int(typer.prompt("Add to today's entry: "))
                if calories < 0:
                    raise ValueError
                self.entries.append({"date": today, "calories": calories})
                self.save_entries()
                typer.echo(f"Entry added: {calories} calories on {today}", color="green")
                break
            except ValueError:
                typer.echo("Please enter a non-negative integer.", color="red")

    def view_entries(self):
        if not self.entries:
            typer.echo("No entries yet.", color="yellow")
            return

        typer.echo("\nCalorie Entries:", color="cyan")
        for entry in self.entries:
            typer.echo(f"{entry['date']}: {entry['calories']} calories")
        remaining_calories = self.get_remaining_calories()
        typer.echo(f"\nRemaining calories: {remaining_calories}", color="magenta")

    def get_remaining_calories(self):
        consumed_calories = sum(entry["calories"] for entry in self.entries)
        return self.calorie_daily_target - consumed_calories

    def save_calorie_target(self):
        data = {
            "name": self.user.name,
            "calorie_daily_target": self.calorie_daily_target,
            "date": date.today().isoformat()
        }
        try:
            with open("calorie_target.json", "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            typer.echo(f"Error saving calorie target: {e}", color="red")

    def save_entries(self):
        data = {
            "name": self.user.name,
            "entries": self.entries
        }
        try:
            with open("calorie_entries.json", "w") as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            typer.echo(f"Error saving entries: {e}", color="red")

    @classmethod
    def load_calorie_target(cls, user: User):
        try:
            with open("calorie_target.json", "r") as f:
                data = json.load(f)
                if data["name"] == user.name:
                    return data["calorie_daily_target"]
        except (FileNotFoundError, json.JSONDecodeError):
            return 2000

    @classmethod
    def load_entries(cls, user: User):
        try:
            with open("calorie_entries.json", "r") as f:
                data = json.load(f)
                if data["name"] == user.name:
                    return data["entries"]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

@app.command()
def authenticate_user():
    name = typer.prompt("Enter your name")
    pin = typer.prompt("Enter your PIN", hide_input=True, confirmation_prompt=True)
    user = User(name, pin)
    tracker = CalorieTracker(user)
    tracker.calorie_daily_target = CalorieTracker.load_calorie_target(user)
    tracker.entries = CalorieTracker.load_entries(user)
    return tracker

@app.command()
def display_menu(tracker: CalorieTracker):
    while True:
        choice = typer.prompt(
            "\nChoose an option:\n"
            "1. Set calorie target\n"
            "2. Add calorie entry\n"
            "3. View entries\n"
            "4. Help\n"
            "5. Quit",
            show_choices=False
        )
        if choice == "1":
            tracker.set_calorie_target()
        elif choice == "2":
            tracker.add_calorie_entry()
        elif choice == "3":
            tracker.view_entries()
        elif choice == "4":
            display_help()
        elif choice == "5":
            typer.echo("Goodbye!", color="green")
            break
        else:
            typer.echo("Invalid choice. Please choose a valid option.", color="red")

@app.command()
def display_help():
    help_text = """
    Calorie Tracker Help

    Welcome to the Calorie Tracker app! This tool helps you monitor your daily calorie intake.

    How to Use:
    1. Set your daily calorie target
    2. Add calorie entries throughout the day
    3. View your entries and remaining calories

    Troubleshooting:
    - If entries aren't saving, check file permissions
    - For incorrect calculations, verify input values
    
    """
    typer.echo(help_text)
    typer.confirm("Press Enter to return to the main menu...", default=True)

@app.command()
def main():
    tracker = authenticate_user()
    display_menu(tracker)

if __name__ == "__main__":
    app()
