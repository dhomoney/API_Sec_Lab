         #!/bin/bash
         cat ~/API_Sec_Lab/files/FuzzLists/usernames.txt | while read line; do curl -X GET -H 'Connection: close' --insecure "http://192.168.100.45:5000/users/v1/$(echo $line|tr -d '\n\t\r')" -s -w --insecure'\n'; done