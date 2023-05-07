import json
import random
import datetime
import time
from includes import admin_functions as adm
from includes import encryption as enc


# create a Process id for each transaction
def get_PID(user_id):
    flag = True
    with open(enc.dp_files+adm.get_dp_name(user_id), 'r') as getAllData:
        data = json.load(getAllData)
    while flag:
        pid = random.randrange(1234, 5644886464664)
        for i in data["process"]:
            if pid == i["PID"]:
                break
            else:
                flag = False
    return pid


# add initial transaction to new users
def initial_transaction(user_id):
    initial_data = {
        "process":
            [
                {
                    "PID": 1,
                    "date": str(datetime.date.today()),
                    "time": datetime.datetime.now().strftime("%H:%M:%S"),
                    "current balance": 0,
                    "withdraw amount": 0,
                    "deposit amount": 0
                }
            ]
    }

    with open(enc.dp_files+adm.get_dp_name(user_id), 'w') as setAllDAta:
        json.dump(initial_data, setAllDAta, indent=2)


# add Process
def add_Transaction(user_id, current_balance,  withdraw_amount, deposit_amount):

    with open(enc.dp_files+adm.get_dp_name(user_id), 'r') as getAllDAta:
        data = json.load(getAllDAta)

    new_data = {
                    "PID": get_PID(user_id),
                    "date": str(datetime.date.today()),
                    "time": datetime.datetime.now().strftime("%H:%M:%S"),
                    "current balance": current_balance,
                    "withdraw amount": withdraw_amount,
                    "deposit amount": deposit_amount
    }

    data["process"].append(new_data)

    with open(enc.dp_files+adm.get_dp_name(user_id), 'w') as setAllDAta:
        json.dump(data, setAllDAta, indent=2)


# withdraw
def withdraw(user_id, withdraw_amount):

    with open(enc.dp_files+adm.get_dp_name(user_id), 'r') as getAllDAta:
        data = json.load(getAllDAta)
        current_balance = data["process"][len(
            data["process"])-1]["current balance"]
    if withdraw_amount > current_balance:
        print("\033[31mError cannot withdraw!\033[0m")
        return
    else:
        current_balance -= withdraw_amount
        add_Transaction(user_id, current_balance, withdraw_amount, 0)


# deposit
def deposit(user_id, deposit_amount):

    with open(enc.dp_files+adm.get_dp_name(user_id), 'r') as getAllDAta:
        data = json.load(getAllDAta)
        current_balance = data["process"][len(
            data["process"])-1]["current balance"]
    current_balance += deposit_amount
    add_Transaction(user_id, current_balance, 0, deposit_amount)


# get current balance
def current_balance(user_id):
    with open(enc.dp_files+adm.get_dp_name(user_id), 'r') as getAllDAta:
        data = json.load(getAllDAta)
    return data["process"][len(data["process"])-1]["current balance"]


# get last transaction info
def last_transaction(user_id):
    with open(enc.dp_files+adm.get_dp_name(user_id), 'r') as getAllDAta:
        data = json.load(getAllDAta)
    last = data["process"][len(data["process"])-1]
    res = f'''
    \t\tPID : {last['PID']}
    \t\tdate : {last['date']}
    \t\ttime : {last['time']}
    \t\tcurrent balance : {last['current balance']}
    \t\twithdraw amount : {last['withdraw amount']}
    \t\tdeposit amount : {last['deposit amount']}
    '''
    return res


def print_options(options):
    for line in options.splitlines():
        print(line)
        time.sleep(.15)