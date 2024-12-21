import json
from datetime import date

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
            print('Log-in details verified. Welcome back!')
            self.user_details = stored_data
            return True
        else:
            self.user_details = {'Name': username, 'PIN': pin}
            FileManager.save_json(self.user_details, 'user_details.json')
            print('New log-in details saved!')
            return True

class CalorieTracker:
    def __init__(self, user_manager):
        self.user_manager = user_manager
        self.calorie_target = None
        self.today_entry = {}

    def set_calorie_target(self):
        calorie_daily_target = int(input('Set your daily target calorie: '))
        today = date.today().isoformat()
        calorie_daily_target_data = {
            'Name': self.user_manager.user_details['Name'],
            'Calories daily': calorie_daily_target,
            'Date': today
        }
        FileManager.save_json(calorie_daily_target_data, 'calories_daily_target_data.json')
        self.calorie_target = calorie_daily_target
        print(f'Calorie target {calorie_daily_target} for {today} has been updated!')

    def add_calorie_entry(self):
        calories_total_data = int(input('Add to today entry: '))
        stored_data = FileManager.load_json('calories_total_data.json')
        if stored_data:
            self.today_entry = stored_data
        else:
            today = date.today().isoformat()
            self.today_entry = {'date': today, 'calories': []}

        self.today_entry['calories'].append(calories_total_data)
        FileManager.save_json(self.today_entry, 'calories_total_data.json')
        print('calories saved')
        print(f"Calories added today: {self.today_entry['calories']}")
        total_today = sum(self.today_entry['calories'])
        print(f"Total calories consumed today: {total_today}")

def main():
    user_manager = UserManager()
    calorie_tracker = CalorieTracker(user_manager)

    user_name_input = input('Enter your name: ')
    user_pin_input = input('Enter your PIN: ')

    if user_manager.authenticate_user(user_name_input, user_pin_input):
        while True:
            print('\nOptions:')
            print('1. Set calories target')
            print('2. Add calorie entry')
            print('3. Help')
            print('4. Quit')

            choice = int(input('Enter option: '))

            if choice == 1:
                calorie_tracker.set_calorie_target()
            elif choice == 2:
                calorie_tracker.add_calorie_entry()
            elif choice == 3:
                print('Help')
                print('Follow the menu instructions to track and view your calories')
            elif choice == 4:
                print('Quit')
                break
            else:
                print('Invalid option. Please choose a valid option.')

if __name__ == "__main__":
    main()
