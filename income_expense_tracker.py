import csv
import re
import os
import json


class Tracker:
    def __init__(self, month, salary: float, bonus: float, rent: float, food: float, utility: float, transport: float, fun: float):
        self.month = month
        self._salary = salary
        self.bonus = bonus
        self.rent = rent
        self.food = food
        self.utility = utility
        self.transport = transport
        self.fun = fun
    
    @property
    def salary(self):
        return self._salary
    

    def transaction_record(self):
        self.income_total = self._salary + self.bonus
        self.expense_total = self.rent + self.food + self.fun + self.transport + self.utility
        self.net_value = self.income_total - self.expense_total
    
        #This is to avoid any duplicated months

        with open("Income.csv") as file:
            reader = csv.DictReader(file, delimiter='|')
            for row in reader:
                if row['Month'] == self.month:
                    print(f"{self.month} is already recorded.")
                    return 
        data = [
            {'Month': self.month, 
             'Salary': self._salary, 
             'Bonus': self.bonus,
             'Month-Total-Income': self.income_total,
             'Rent': self.rent,
             'Food': self.food,
             'Utility': self.utility,
             'Transport': self.transport,
             'Fun': self.fun,
             'Month-Total-Expense': self.expense_total,
             'Net-Value': self.net_value}
        ]
        with open("Income.csv", "a", newline='') as file:
            fieldnames = ['Month', 'Salary', 'Bonus', 'Month-Total-Income', 'Rent', 'Food', 'Utility', 'Transport', 'Fun', 'Month-Total-Expense', 'Net-Value']
            record = csv.DictWriter(file, fieldnames=fieldnames, delimiter='|')
            if not file or os.stat("Income.csv").st_size == 0:
                record.writeheader()

            for row in data:
                record.writerow(row)


#main function to call all the options
def main():
    print("\n\t\tWELCOME TO INCOME-EXPENSE TRACKER")
    print("-" * 70)
    
    print("OPTIONS:")
    print("\t1|Record income and expense|")
    print("\t2|Month History            |")
    print("\t3|Month Summary            |\n")

    while True:
        try:
            option = int(input("Enter your option: "))
            match option:
                case 1:
                    record_new_data()
                    break
                case 2:
                    month = get_month("Which month's history you want to check? ('e.g: January-2024'): ")
                    print(month_history(month))
                    break
                case 3:
                    month = get_month("Which month's summary you want to see? ('e.g: January-2024'): ")
                    print(month_summary(month))
                    break
                case _:
                    print("Option number must be from one of the above")
        except ValueError:
            print("Option number must be from one of the above")
            

def record_new_data():
    month = get_month("Enter the current month('e.g: January-2024'): ")
    salary = get_input("Enter your Salary: ", "Salary")
    bonus = get_input(f"Enter your {month} bonuses: ", "Bonus")
    rent = get_input(f"Enter {month}'s house rent: ", "Rent")
    food = get_input(f"Enter expenses for food this month: ", "Food")
    utility = get_input(f"Enter utility expenses for this month: ", "Utility")
    transport = get_input(f"Enter transport expenses for this month: ", "Transport")
    fun = get_input(f"Enter entertainment expenses for this month: ", "Entertainment")
    monthly_income = Tracker(month, salary, bonus, rent, food, utility, transport, fun)
    monthly_income.transaction_record()

#can be tested
def month_history(given_month):
    history_dict = {}
    with open("Income.csv") as file:
        reader = csv.DictReader(file, delimiter='|')
        for row in reader:
            if row['Month'] == given_month:
                history_dict = {key: row[key] for key in ['Salary', 'Bonus', 'Month-Total-Income', 'Rent', 'Fun', 'Food', 'Utility', 'Transport', 'Month-Total-Expense', 'Net-Value']}
                break
        if history_dict:
            return json.dumps(history_dict, indent=4)
        else:
            return "Month not found"
#can be tested
def month_summary(given_month):
    title_month = given_month.title()
    with open("Income.csv") as file:
        reader = csv.DictReader(file, delimiter='|')
        for row in reader:
            if row['Month'] == title_month:
                if 0 < float(row['Net-Value']) <= 100:
                    return f"Summary: You need to lower your expense and/or start extra shift working hour."
                # elif float(row['Net-Value']) <= 0:
                #     return f"Invalid Net-Value"
                else:
                    return f"Summary: Your expense is balanced."
            else:
                return "Month not found"
#can be tested
def get_month(prompt):
    months = [
        'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'
    ]
    pattern = r"^(\w+)-\d+$"
    while True:
        month_year = input(prompt).title()
        if matches:= re.search(pattern, month_year):
            month = matches.group(1)
            if month in months:
                return month_year
        raise ValueError("Invalid month")

def get_input(prompt, reason, testing=False):
    while True:
        try:
            user_input = float(input(prompt))
            if user_input >=0:
                return user_input
            if reason != "Bonus" and reason != "Salary":
                if testing:
                    return f"{reason} expense must be greater than or equal to 0!!"
                print(f"{reason} expense must be greater than or equal to 0!!")
            if testing:
                return f"{reason} must be greater than or equal to 0!!"
            print(f"{reason} must be greater than or equal to 0!!")

        except ValueError:
            if reason != "Bonus" and reason != "Salary":
                if testing:
                    return f"{reason} expense must be an integer or float!!"
                print(f"{reason} expense must be an integer or float!!")
            else:
                if testing:
                    return f"{reason} must be an integer or float!!"
                print(f"{reason} must be an integer or float!!")

if __name__ == "__main__":
    main()