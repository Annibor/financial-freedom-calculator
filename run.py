"""
Imports for project
"""
import re
import numpy as np
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


def calculate_years_to_financial_freedom(initial_savings, monthly_savings, target_goal,annual_interest_rate, monthly_savings_percentage)
"""
Calculate the years it would take to achieve financial freedom.

Args: initial_savings (float): The initial savings amount in euros.
monthly savings (float): The monthly savings amount in euros.
target_goal (float): The target savings goal in  euros.
annual_interest_rate (float): The annual interest rate as a percentage.
monthly_savings_percentage (float): The monthly savings percentage as a percentage.

Returns: int: The number of years required to achieve the financial goal.
"""
years = 0
annual_interest_rate /= 100
monthly_savings_percentage /= 100

while initial_savings < traget_goal:
    initial_saving += (monthly_savings + ( intitial_savings * monthly_savings_procentage))
    initial_savings *= (1 + annual_interest_rate)
    years += 1

return years


def calculate_required_monthly_savings(initial_savings_two, target_goal_two, years_to_goal):
    """
    Calculate the monthly savings that are required to reach the financial goal in a specific number of years.

    Args: 
    initial_savings_two (float): The initial savings amount in euros.
    target_goal (float): The target savings goal in euros.
    years_to_goal (int): The number of years it talkes to reach the financial goal.

    Returns:
    float: The required monthly savings amount in euros.
    """
    return (target_goal_two - initial_savings_two) / (years_to_goal * 12)
