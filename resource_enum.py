 import requests

 host = 'http://10.50.100.45:5000/'
 file1 = open('./API_Sec_Lab/IntruderPayloads/dirbuster-quick.txt', 'r')
 Lines = file1.read().splitlines()

 count = 0
 for line in Lines:
     count += 1
     x = requests.get(host + line, verify=False)
     print('Resource: ' + line + ' | ' + str(x.status_code))