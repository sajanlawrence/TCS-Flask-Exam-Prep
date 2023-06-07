import urllib
from urllib import request
'''
details = {"PrincipalAmount":"Hello","Rate":13,"Period":6.2}
data = urllib.parse.urlencode(details)
data = data.encode("ascii")
request1 = request.Request("http://127.0.0.1:5000/",data=data,method="POST")

try:
    response1 = request.urlopen(request1)
    print(response1.read())
except urllib.error.HTTPError as e:
    print(e.code,e.read())
'''
data1 = {'principal_amount' : 'hey',
        'period' : 5.7,
        'rate' : 8.4}
data = urllib.parse.urlencode(data1)
data = data.encode('ascii')

request2 = request.Request('http://127.0.0.1:5000/simpleInterest/', method='POST', data=data)
try:
    response2 = request.urlopen(request2)
    print(response2.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())