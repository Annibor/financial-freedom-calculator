"""
Import needed for the code
"""
import gspread
from google.oauth2.service_account import Credentials


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('financial-freedom-calculator')


def get_user_data():
    """
    Collect user data like name, email, and address.
    """

    name = input('What is your name?: ')
    while True:
        email = input('What is your email?: ')
        if "@" in email and "." in email and email.find("@") < email.rfind('.'):
            break
        else:
            print('Invalid email address, please try again!')

    while True:
        age = input('What is your age?: ')
        if age.isdigit():
            age = int(age)
            break
        else:
            print('Invalid age, please try again!')

    return {
        'name': name,
        'email': email, 
        'age': age
    }

def update_google_sheets(data):
    """
    Update Googlesheets
    """
    print('Updating Googlesheets...\n')
    worksheet = SHEET.worksheet(0)
    worksheet.append_row(data)
    print('Googlesheets updated!')


def main():
    """
    Main function, runs all the functions
    """
    get_user_data()
    update_google_sheets(get_user_data())

print('Welcome to the financial freedom calculator!\n')
print('This program will help you calculate the number of years'
          'it takes to reach financial freedom, or how much you need to'
          'save every month to reach financial freedom.')
main()