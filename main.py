from includes import encryption as enc
from includes import ATM as atm
from includes import admin_functions as adm
from includes import Authentication as auth
import time
import subprocess

if __name__ == '__main__':

    login_number = 0
    option = 0

    while login_number <= 3:

        print("login to your account")
        id = input('Enter id : ')
        passwd = input('Enter password : ')

    # admin
        if adm.user_exist(id, "admins"):

            if auth.user_Authenticated(id, passwd, "admins"):

                time.sleep(1)

                while option <= 10:

                    atm.print_options(enc.admin_options)
                    option = int(input("press a number : "))

                    if option == 1:
                        new_id = input('Enter new_id : ')
                        new_passwd = input('Enter new_password : ')
                        adm.add_user(new_id, new_passwd)

                    elif option == 2:
                        rm_id = input('Enter id : ')
                        adm.remove_user(rm_id)

                    elif option == 3:
                        user_id = input("Enter user id : ")
                        new_passwd = input("Enter user new password : ")
                        adm.change_user_passwd(user_id, new_passwd)

                    elif option == 4:
                        user_id = input("enter user id : ")
                        print("user database : "+adm.get_dp_name(user_id))

                    elif option == 5:
                        user_id = input("Enter user id : ")
                        print(adm.user_info(user_id))

                    elif option == 6:
                        new_passwd = input("Enter your new password : ")
                        adm.chang_admin_passwd(new_passwd)

                    elif option == 7:
                        print(auth.log_history())

                    elif option == 8:
                        # user then date then times
                        user = ""
                        date = ""  # (year-moth-day)
                        times = ""  # (hours:minutes:second)
                        user = input("enter user id : ")
                        date = input("enter date of log : ")
                        times = input("enter time of log : ")
                        if user != "":
                            print("\n   log data : ")
                            auth.search_log(user, date, times)
                        else:
                            print("invalid input please insert an id")

                    elif option == 9:
                        user_id = input("Enter user id : ")
                        adm.transactions_history(user_id)

                    elif option == 10:
                        subprocess.call(["python3", __file__])

                    else:
                        print("exit...\n")
                        time.sleep(.5)
                        exit(0)

    # user
        elif adm.user_exist(id, "users"):

            if auth.user_Authenticated(id, passwd, "users"):

                time.sleep(1)

                while option <= 8:

                    atm.print_options(enc.user_options)
                    option = int(input("press a number : "))

                    if option == 1:
                        print("current balance : " +
                        str(atm.current_balance(id)))

                    elif option == 2:
                        amount = int(input("Enter withdraw amount : "))
                        atm.withdraw(id, amount)

                    elif option == 3:
                        amount = int(input("Enter deposit amount : "))
                        atm.deposit(id, amount)

                    elif option == 4:
                        print("\n     Last transaction : ")
                        print(atm.last_transaction(id))

                    elif option == 5:
                        print("\n     Transaction history : ")
                        adm.transactions_history(id)

                    elif option == 6:
                        old_password = input("Enter old password : ")
                        if auth.user_Authenticated(id, old_password,"users"):
                            new_password = input("Enter new password : ")
                            adm.change_user_passwd(id, new_password)
                        else:
                            print("Wrong Old password")

                    elif option == 7:
                        sure = input(
                            " note: this will discard all account info and balance \n\t\t press [y] to remove : "
                        )
                        if sure == "y":
                            adm.remove_user(id)
                            print("your account removed successfully")
                            time.sleep(1)
                            subprocess.call(["python3", __file__])

                    elif option == 8:
                        subprocess.call(["python3", __file__])

                    else:
                        print("exit...\n")
                        time.sleep(.5)
                        exit(0)

        if not auth.user_Authenticated(id, passwd, "users"):
            login_number += 1
            print(f"\033[31m Invalid credentials \033[0m")

        if login_number >= 3:
            print(
                "You typed wrong credential 3 times please contact admin for more information")
            time.sleep(1)
            exit(0)
