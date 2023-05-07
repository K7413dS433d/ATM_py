# ATM Machine

projct with simpel database using json and text files for ATM mathcine with admin and users account

admin authorization
```
id : admin
password : admin
```
user1 authorization
```
id : khaled
password : khaled
```
user2 authorization
```
id : zeiad
password : zeiad
```
user3 authorization
```
id : eslam
password : eslam
```


## Files and Directories :

```
ATM
├── Includes
│   ├── ATM.py
│   ├── Authentication.py
│   ├── admin_functions.py
│   └── encryption.py
├── README.md
├── files
│   ├── databases
│   │   ├── ZXNsYW0=.json
│   │   ├── a2hhbGVk.json
│   │   └── emVpYWQ=.json
│   ├── log.txt
│   └── users.json
└── main.py
```
## Includes director

#### encryption.py
```
file pathes:
    dp_files : locate folder containing database users Files
    users_files : locate json file contains users, admin login data and database names for users
    log_files : locate log file  contains log data for users

options:
    admin and user options that can perform

en_code(message) : encode message

de_code(encoded_message) : decode message

dp_id(encrypted_id) : create database file for new user
```

#### admin_functions.py
```
user_exist(user_id, section) : check if user or admin found

get_user_idx(user_id, section) : get user index from users file

add_user(user_id, user_passwd) : add new user

remove_user(user_id) : remove user

change_user_passwd(user_id, user_newPassword) : change user user Password

get_dp_name(user_id) : get database name for user

user_info(user_id) : get all user information

chang_admin_passwd(admin_newPassword) : change admin password

transactions_history(user_id) : get transactions history
```

#### Authentication.py
```
user_Authenticated(user_id, user_password, section) : check if user aor admin is Authenticated

write_log(user_id) : write a log data

log_history() : get all log data

search_log(*args) : search in log data
```

#### ATM.py
```
get_PID(user_id) : get a process id

initial_transaction(user_id) : make initial transaction data

add_Transaction(user_id, current_balance,  withdraw_amount, deposit_amount) : to add transaction information to user file in database

withdraw(user_id, withdraw_amount) : withdrow from account

deposit(user_id, deposit_amount) : deposit from account

current_balance(user_id) : get current balance account

last_transaction(user_id) : get last transaction information

print_options(options) : print a string contains all options for user

get_PID(user_id) : to get a process id

initial_transaction(user_id) : make initial transaction data

add_Transaction(user_id, current_balance,  withdraw_amount, deposit_amount) : to add transaction information to user file in database

withdraw(user_id, withdraw_amount) : withdrow from account

deposit(user_id, deposit_amount) : deposit from account

current_balance(user_id) : get current balance account

last_transaction(user_id) : get last transaction information

print_options(options) : print a string contains all options for user
```

## files directory

```
database directory : includes all users database json files

log files : includes all log data

users.json : includes all users data

```

