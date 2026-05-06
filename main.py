import json

FILE_NAME = "expenses.json"

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
        price = input("amount: ")
        try:
           price = int(price)
        except:
            print("wrong type")
            continue
        cat = input("category: ")
        if not cat:
            print("input cannot be empty")
            continue
        des = input("description: ")
        if not des:
            print("input cannot be empty")
            continue
        expenses.append({
            "amount": price,
            "category": cat,
            "description": des
        })
        with open(FILE_NAME,"w") as file:
            json.dump(expenses, file)
        print("expense saved")
    elif choose == "1":
        if not expenses:
            print("no expenses")
        else:
            for i in expenses:
                print(f'{i["amount"]} | {i["category"]} | {i["description"]}')
    elif choose == "2":
        amt = 0
        for i in expenses:
            amt += int(i["amount"])
        print(amt)
    elif choose == "3":
        break
    else:
        print("wrong option")