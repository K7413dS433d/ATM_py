import os
import json
from includes import encryption as enc
from includes import ATM as atm


# check user is exist
def user_exist(user_id, section):
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    for i in data[section]:
        if i["id"] == enc.en_code(user_id):
            return True
    return False


# get user index
def get_user_idx(user_id, section):
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    index = 0
    for i in data[section]:
        if i["id"] == enc.en_code(user_id):
            return index
        index += 1
        if index >= len(data[section]):
            return index


# add user
def add_user(user_id, user_passwd):
    enc.dp_id(enc.en_code(user_id))
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    tmp = data["users"]
    app = {
        "id": enc.en_code(user_id),
        "password": enc.en_code(user_passwd),
        "dp_name": enc.en_code(user_id)+".json"
    }
    tmp.append(app)
    with open(enc.users_file, 'w') as setAllDAta:  # users_file
        json.dump(data, setAllDAta, indent=2)
    atm.initial_transaction(user_id)
    print("user added successfully\n")


# remove user bad one
# def remove_user(user_id):
#     os.remove(enc.dp_files+enc.en_code(user_id))
#     with open(enc.users_file, 'r') as getAllData: #users_file
#         data = json.load(getAllData)
#     index = get_user_idx(user_id,"users")
#     new_data = {"admins": [], "users": []}
#     new_data["admins"].append(data["admins"])
#     j = 0
#     for i in data["users"]:
#         if j != index:
#             new_data["users"].append(i)
#         j += 1
#     with open(enc.users_file, 'w') as setAllDAta: #users_file
#         json.dump(new_data, setAllDAta, indent=2)


# remove user
def remove_user(user_id):
    os.remove(enc.dp_files+get_dp_name(user_id))
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    index = get_user_idx(user_id, "users")
    del data["users"][index]
    with open(enc.users_file, 'w') as setAllDAta:  # users_file
        json.dump(data, setAllDAta, indent=2)
    print("user removed successfully\n")


# change user password
def change_user_passwd(user_id, user_newPassword):
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    index = get_user_idx(user_id, "users")
    data["users"][index]["password"] = enc.en_code(user_newPassword)
    with open(enc.users_file, 'w') as setAllDAta:  # users_file
        json.dump(data, setAllDAta, indent=2)
    print("password changed successfully\n")


# get database name
def get_dp_name(user_id):
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    user_idx = get_user_idx(user_id, "users")
    return data["users"][user_idx]["dp_name"]


# get user info
def user_info(user_id):
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    user_idx = get_user_idx(user_id, "users")
    user_info = f'''
    user id : {enc.de_code(data["users"][user_idx]["id"])}
    password : {enc.de_code(data["users"][user_idx]["password"])}
    database name : {data["users"][user_idx]["dp_name"]}
    last transaction : {atm.last_transaction(user_id)}
    '''
    return user_info


# change admin password
def chang_admin_passwd(admin_newPassword):
    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)
    data["admins"][0]["password"] = enc.en_code(admin_newPassword)
    with open(enc.users_file, 'w') as setAllDAta:  # users_file
        json.dump(data, setAllDAta, indent=2)
    print("password changed successfully\n")


# show transaction history
def transactions_history(user_id):
    with open(enc.dp_files+get_dp_name(user_id), 'r') as getAllDAta:
        data = json.load(getAllDAta)
        for i in data["process"]:
            print(      "PID : "+str(i["PID"]))
            print("     date : "+i["date"])
            print("     Time : "+i["time"])
            print("     current balance : "+str(i["current balance"]))
            print("     withdraw amount"+str(i["withdraw amount"]))
            print("     deposit amount"+str(i["deposit amount"]))
            print("----------------------------------------------")

