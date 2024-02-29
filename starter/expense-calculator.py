import math

"""
categorized list of expenses, anything outside these is considered miscellaneous
"""
CATEGORIES = {
        "travel": ["uber", "flight"],
        "food": ["zoe's kitchen", "tacobell"],
        "registration": ["registration"],
        "shopping": ["sMart"],
        "hotel": ["marriott"]
    }

"""
Calculates and prints expense % in each category

Inputs : totals (list of total expenditure in different categories), sum (overall expense)
Outputs : None
"""
def print_expense_percentage(totals, sum):
    for key, val in totals.items():
        print(key, "=>", val, ":", math.floor(val/sum*100), "%")

"""
Categorizes expenses and calculates the total in each category

Inputs : expense_list (list of expenses)
Outputs : None
"""
def calculate_expenses(expense_list):
    totals = {}
    sum = 0 
    for expense, val in expense_list.items():
        print (expense)
        sum += val
        found = False
        for category, types in CATEGORIES.items():
            if expense in types:
                found = True
                print(category, "=>" , types)
                if(category in totals.keys()):
                    totals[category] += val
                else:
                    totals[category] = val
        if found is False:
            if("miscellaneous" in totals.keys()):
                totals["miscellaneous"] += val
            else:
                totals["miscellaneous"] = val

    print_expense_percentage(totals, sum)

def main():
    expense_list = {"registration": 200, "uber": 30, "tacobell": 10, "flight": 157, "zoe's kitchen": 28, "sMart": 14, "marriott": 560, "payment": 130}
    calculate_expenses(expense_list)

if __name__ == "__main__":
    main()

