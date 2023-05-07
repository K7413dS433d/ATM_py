import json
import datetime
from includes import encryption as enc
from includes import admin_functions as adm


# user authentication
def user_Authenticated(user_id, user_password, section):

    with open(enc.users_file, 'r') as getAllData:  # users_file
        data = json.load(getAllData)

    if adm.user_exist(user_id, section):
        user_idx = adm.get_user_idx(user_id, section)
        if enc.en_code(user_id) == data[section][user_idx]["id"] and enc.en_code(user_password) == data[section][user_idx]["password"]:
            print(f"\033[31m Access successfully \n\twelcome {user_id}\033[0m")
            if section == "users":
                write_log(user_id)
            return True
    return False


# write log data
def write_log(user_id):
    with open(enc.users_file, 'r') as getAllData:
        user_data = json.load(getAllData)
    idx = adm.get_user_idx(user_id, "users")
    passwd = user_data["users"][idx]["password"]
    with open(enc.log_file, 'a') as setData:
        data = user_id+' : '+passwd+' ( Date -> '+str(datetime.date.today())+' )' + \
            '( Time -> '+datetime.datetime.now().strftime("%H:%M:%S")+' )'+"\n"
        setData.write(data)


# get all log data
def log_history():
    with open(enc.log_file, 'r') as getAllData:
        data = getAllData.read()
    return data


# get log data in specific date and time
# (user_id , Date (year-moth-day) , Time (hours:minutes:second))
# minimum number of parameters is 1
def search_log(*args):

    argLen = len(args)
    for i in args:
        if i == "":
            argLen -= 1

    with open(enc.log_file, 'r') as data:
        if argLen == 1:
            for i in data:
                line = i.split(' ')
                if args[0] == line[0]:
                    print("        "+i)
        elif argLen == 2:
            for i in data:
                line = i.split(' ')
                if args[0] == line[0] and line[6].endswith(args[1]):
                    print("       "+i)
        elif argLen == 3:
            for i in data:
                line = i.split(' ')
                if args[0] == line[0] and line[6].endswith(args[1]) and line[10].startswith(args[2]):
                    print("        "+i)
