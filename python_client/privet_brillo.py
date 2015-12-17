#!/usr/bin/python
import time
import json
import httplib
import urllib


#anonymously check the device info
data = {"X-Privet-Token": ""}
headers = {"Content-type": "application/json", "Accept": "text/plain" ,"Authorization":"Privet anonymous"}
conn = httplib.HTTPConnection('10.238.158.53',80)
conn.request("GET", "/privet/info", json.dumps(data), headers)
res=conn.getresponse()
print res.status,res.reason
print res.read()

#acess the auth page to get a token
Sheaders = {"Content-type": "application/json", "Accept": "text/plain" ,"Authorization":"Privet anonymous"}
Sconn = httplib.HTTPSConnection('10.238.158.53',443)
data = {"authCode": "1","mode":"anonymous","requestedScope": "auto"}
Sconn.request("POST", "/privet/v3/auth",json.dumps(data),Sheaders)
print data
res=Sconn.getresponse()
content=res.read()
print content

#add token to http header
s=json.loads(content)
token=s["accessToken"]
print token
Sheaders = {"Content-type": "application/json", "Accept": "application/json" ,"Authorization":"Privet "+token}
data1 = {}
Sconn1 = httplib.HTTPSConnection('10.238.158.53',443)
Sconn1.request("POST", "/privet/v3/state",json.dumps(data),Sheaders)
res=Sconn1.getresponse()
print res.read()

#using the token ,we can do something requrie privilege
data1 = {}
Sconn1 = httplib.HTTPSConnection('10.238.158.53',443)
Sconn1.request("POST", "/privet/v3/commands/list",json.dumps(data1),Sheaders)
res=Sconn1.getresponse()
print res.read()

#using the token ,we can rename the device
data1 = {"name":"helloworld"}
Sconn1 = httplib.HTTPSConnection('10.238.158.53',443)
Sconn1.request("POST", "/privet/v3/setup/start",json.dumps(data1),Sheaders)
res=Sconn1.getresponse()
print res.read()


#using the token ,we can call command of the device
data1 = {"name":"_sample._countdown"}
Sconn1 = httplib.HTTPSConnection('10.238.158.53',443)
Sconn1.request("POST", "/privet/v3/commands/execute",json.dumps(data1),Sheaders)
res=Sconn1.getresponse()
print res.read()


#failed to pairing
#so I modify the source code to get the prilege



# data1 = {"pairing":"pinCode","crypto":"p224_spake2"}
# Sconn1 = httplib.HTTPSConnection('10.238.158.53',443)
# Sconn1.request("POST", "/privet/v3/pairing/start",json.dumps(data1),Sheaders)
# res=Sconn1.getresponse()
# content= res.read()
# print content
# data=json.loads(content)


# pairData={"sessionId":data["sessionId"],"clientCommitment":data["deviceCommitment"]}
