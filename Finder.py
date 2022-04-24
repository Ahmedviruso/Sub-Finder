# Subdomain Finder By AhmedViruso
# Interpreter: Python 3.10.4
# Os: Windows 10 Home

from urllib3 import PoolManager
from json import loads

Domain = input("Enter Domain -> ").strip()
Http = PoolManager()
Request = Http.request("GET","https://crt.sh?q={}&output=json".format(Domain))
Response = loads(Request.data)

List = []
for Object in Response:
    Grabbed = Object["name_value"].split("\n")
    for Url in Grabbed:
        if(Url not in List):
            with open("Result.txt","a", encoding = "utf-8") as File:
                File.write(Url + "\n")
            List.append(Url)
else:
    print("[+] Done, Check: Result.txt")