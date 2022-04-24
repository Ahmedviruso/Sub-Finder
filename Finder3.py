# Subdomain Finder v3 By AhmedViruso
# Interpreter: Python 3.10.4
# Os: Windows 10 Home

from urllib3 import PoolManager,disable_warnings
from json import loads
from time import sleep
from hashlib import md5

disable_warnings()
Domain = input("Enter Domain -> ").strip()
Http = PoolManager()

def Grab(Value):
  Request = Http.request("GET","https://crt.sh?q={}&output=json".format(Value))
  Response = loads(Request.data)
  return Response

List = []
def Analyse(Host,Name):
  print("Scanning: " + Host)
  Json = Grab(Host)
  for Object in Json:
    Grabbed = Object["name_value"].split("\n")
    for Url in Grabbed:
      if(Url not in List and "@" not in Url):
        with open(Name + ".txt","a", encoding = "utf-8") as File:
          File.write(Url + "\n")
        List.append(Url)
  else:
    print("Done: " + Host)
        
Analyse(Domain,"Result-1")
I,Last = 2, str()
while True:
  StrList = str(List).encode("utf-8")
  Hash = md5(StrList).hexdigest()
  if(Hash != Last):
    Last = Hash
    for Domain in List:
      Analyse(Domain,"Result-" + str(I) )
      sleep(2)
    else:
      I = I + 1
  else:
    break
else:
  print("Done :D")
