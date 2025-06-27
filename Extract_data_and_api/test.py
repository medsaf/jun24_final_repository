import os
import requests


ip_address=os.getenv("FASTAPI")


def test_api():
     r=requests.get("http://"+ip_address+"/metrics")
     print("http://"+ip_address)
     assert r.status_code==200
