#
# 
#
import requests

r = requests.get("https://api.github.com/search/repositories?q=language:python")
data = r.json( )

print(type(data))