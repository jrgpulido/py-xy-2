#
# 
#
import requests

r = requests.get("https://api.github.com/search/repositories?q=language:python")
#vs
#r = requests.get("https://api.github.com/users/Connor-SM")
#vs
#r = requests.get("https://api.github.com/users/yours")
data = r.json( )

print(type(data))

print(data.keys())
#vs
#print(data.items())
#vs
#for k,v in data.items():
#    print(k,'->',v,'\n')


print(data['total_count'])
#vs
#print(data['login'])
