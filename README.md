# Income-Expense Tracker

## Project Overview
The Income-Expense Tracker is a command-line application that allows users to record their monthly income and expenses, and view a summary of their financial status for each month. It saves the data in a CSV file and provides functionalities to track income, expenses, and calculate the net value for each month.
## Features
* **Record Income and Expenses**: Input your salary, bonuses, and expenses (rent, food, utility, transport, entertainment) for a specific month.
* **Check Month History**: View detailed records of income and expenses for a given month.
* **Monthly Summary**: Get a financial summary for the selected month, including advice on whether you should lower your expenses.
* **Avoid Duplicate Entries**: The program checks for existing records to ensure you don't add duplicate data for the same month.

## Installation
1. Make sure you have Python installed on your machine.
2. Clone or download this project to your local machine.
3. Run the script from the command line:
`python income_expense_tracker.py`

## Usage
1. **Record New Data**:
*  The program will prompt you to enter details about your salary, bonuses, and expenses for a given month.
* Example input: `January-2024`
2. **Check Month History**:
* Input a month (e.g., `January-2024`) to retrieve the detailed history of that month’s income and expenses.
3. **View Month Summary**:
* Input a month to view a summary of your financial performance, including whether your expenses are balanced or need adjustment.

## CSV File Structure

The program saves data in a file called `Income.csv`. This file uses the pipe (`|`) as the delimiter and contains the following fields:
* `Month`
* `Salary`
* `Bonus`
* `Month-Total-Income`
* `Rent`
* `Food`
* `Utility`
* `Transport`
* `Fun`
* `Month-Total-Expense`
* `Net-Value`
## Error Handling
* **Invalid Month Input**: The program validates month input and prompts the user to enter a valid month in the format "Month-Year" (e.g., `January-2024`).
* **Expense Input Validation**: The program ensures that expenses are non-negative and in proper numeric format (integer of float)