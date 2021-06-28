def user_prompt(prompt):
    while True:
        input_data = input(f'Enter your {prompt}: ').lower()
        if len(input_data) > 6:
            break
        else:
            print(f'Please enter a valid {prompt}')
    return input_data


def write_to_file(data):
    file = open('userdata.txt', 'a')
    file.write(data + '\n')
    file.close()


def check_username_exists(username):
    lines = list(open('userdata.txt', 'r'))
    usernames = [u.split(',')[0] for u in lines]
    print(usernames)
    if username in usernames:
        return True
    return False


def registration():
    username = user_prompt('username')
    if check_username_exists(username):
        print('User already exists with this username! Please try different username')
        raise Exception('User already exists')
    password = user_prompt('password')
    write_to_file(','.join([username, password]))
    print('User created successfully! ')
    return 'User created successfully'


def login():
    username = user_prompt('username')
    password = user_prompt('password')
    if not check_username_exists(username):
        print('User does not exists with this username')
        return False
    lines = list(open('userdata.txt', 'r'))
    data = [u for u in lines if u.split(',')[0] == username]
    if password == data[0].rstrip('\n'):
        print('User successfully logged In')
    else:
        raise Exception('Password is wrong')


registration()
print('Login user')
login()