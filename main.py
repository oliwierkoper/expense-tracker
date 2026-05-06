import json

FILE_NAME = "expenses.json"

def save_expense(expenses):
    with open(FILE_NAME,"w") as file:
        json.dump(expenses, file)

print("expense tracker")
print("0. add ")
print("1. show")
print("2. sum")
print("3. exit")

try:
    with open(FILE_NAME,"r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    expenses = []
while True:
    choose = input("choose: ")
    if choose == "0":
        expenses.append({
            "amount": input("amount: "),
            "category": input("category: "),
            "description": input("description: ")
        })
        save_expense(expenses)
        print("expense saved")
    elif choose == "1":
        if not expenses:
            print("no expenses")
        else:
            for i in expenses:
                print(f'{i["amount"]} | {i["category"]} | {i["description"]}')
    elif choose == "2":
        pass
    elif choose == "3":
        break
    else:
        print("wrong option")