import base64

# paths
dp_files = "files/databases/"
users_file = "files/users.json"
log_file = "files/log.txt"


#options
admin_options = f'''
                press [1] to add user \n
                press [2] to remove user  \n
                press [3] to change user password \n
                press [4] to get user database name \n
                press [5] to get user info \n
                press [6] to change your password \n
                press [7] to get log data \n
                press [8] to search log data \n
                press [9] to get user transaction history \n
                press [10] to go to login page \n
                press any number to exit \n
                '''

user_options=f'''
                press [1] to get current balance \n
                press [2] to withdraw \n
                press [3] to deposit \n
                press [4] to get last transaction \n
                press [5] to show transaction history\n
                press [6] to change password \n
                press [7] to remove account \n
                press [8] to go to login page \n
                press any number to exit \n
        '''


# encoding
def en_code(message):
    encoded_message = base64.b64encode(message.encode('utf-8'))
    encoded_message = encoded_message.decode('utf-8')
    return encoded_message


# decoding
def de_code(encoded_message):
    decoded_message = base64.b64decode(encoded_message).decode('utf-8')
    return decoded_message


# create database
def dp_id(encrypted_id):
    file_path = dp_files+encrypted_id+".json"  # All transaction here
    f = open(file_path, 'w')
    f.close()
