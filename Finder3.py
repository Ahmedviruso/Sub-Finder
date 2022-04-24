# Don't forget to delete all "result" files when u want to scan again

# Subdomain Finder v3 By AhmedViruso
# Interpreter: Python 3.10.4
# Os: Windows 10 Home
# 2022 - 04 - 24

from urllib3 import PoolManager,disable_warnings
from json import loads
from time import sleep

disable_warnings()
Domain = input("Enter Domain -> ").strip()
Http = PoolManager()

def Grab(Value):
  Request = Http.request("GET","https://crt.sh?q={}&output=json".format(Value))
  Response = loads(Request.data)
  return Response

List = []
def Analyse(Host,Name):
  print("Scanning: {}".format(Host))
  Json = Grab(Host)
  for Object in Json:
    Grabbed = Object["name_value"].split("\n")
    for Url in Grabbed:
      if(Url not in List and "@" not in Url):
        with open(Name + ".txt","a", encoding = "utf-8") as File:
          File.write(Url + "\n")
        List.append(Url)
  else:
    print("Done: {}".format(Host))
        
Analyse(Domain,"Result-1")

Num = 1
while True:
  try:
    File = open("Result-{}.txt".format(Num) , "r", encoding = "utf-8")
    Domains = File.readlines()
    File.close()
    Num += 1
  except Exception:
    break
  for Domain in Domains:
    Analyse(Domain.strip(),"Result-{}".format(Num))
    sleep(2)

print("Done All")
