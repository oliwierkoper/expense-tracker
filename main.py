import json

FILE_NAME = "expenses.json"

print("expense tracker")
print("0. add ")
print("1. show")
print("2. statistics")
print("3. filter by category")
print("4. exit")

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
           price = float(price)
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
        if not expenses:
            print("no expenses")
            continue
        amt = 0
        for i in expenses:
            amt += int(i["amount"])
        print(f'max: {max(expenses, key=lambda expense: expense["amount"])["amount"]}')
        print(f"sum: {amt}")
        print(f'avg: {float(amt/len(expenses))}')
    elif choose == "3":
        cat_filter = input("filter by: ")
        if not cat_filter:
            print("input cannot be empty")
            continue
        ctr=0
        for i in expenses:
            if cat_filter==i["category"]:
                ctr +=1
                print(f'{i["amount"]} | {i["category"]} | {i["description"]}')
        if ctr==0:
            print("no such category")
    elif choose == "4":
        break
    else:
        print("wrong option")