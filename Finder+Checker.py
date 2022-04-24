# This Version Save Only Working Sub-Domains
# Subdomain Finder By AhmedViruso
# Interpreter: Python 3.10.4
# Os: Windows 10 Home

from urllib3 import PoolManager,disable_warnings
from json import loads
from socket import gethostbyname

disable_warnings()
Domain = input("Enter Domain -> ").strip()
Http = PoolManager()
Request = Http.request("GET","https://crt.sh?q={}&output=json".format(Domain))
Response = loads(Request.data)

List = []
for Object in Response:
    Grabbed = Object["name_value"].split("\n")
    for Url in Grabbed:
        if(Url not in List):
            try:
                gethostbyname(Url.replace("*.",""))
                with open("Result.txt","a", encoding = "utf-8") as File:
                    File.write(Url + "\n")
                print("Working [{}]".format(Url))
            except Exception:
                print("Not Working [{}]".format(Url))
            List.append(Url)
else:
    print("[+] Done, Check: Result.txt")