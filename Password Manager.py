master_pwd = input('What is your password? ')

#defining a function
def view():
    with open('password.txt', 'r') as f:
       for line in f.readlines():
           data = line.rsplit(':')
           user, passw = data.split()





def add():
    name = input('Account name: ')
    pwd = input('Password : ')

    #creating a file to add the password, with automatically closes file
    #now for modes, w,r and a, w is writing, r is read,
    with open('password.txt', 'a') as f:
        f.write(name + '' + pwd + '\n')
        f.close()

while True:
    mode = input('Would you like to add a new password or view existing ones?(view or add). Type q to quit ')
    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
       add()
    else:
        print('Please enter either "view" or "add"')
        continue

