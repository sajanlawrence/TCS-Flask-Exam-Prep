import urllib
from urllib import request

'''post method request
course1 = {"course_name":"Artificial Intelligence"}
data = urllib.parse.urlencode(course1)
data = data.encode("ascii")

request1 = request.Request('http://127.0.0.1:5000/Courses/1',data=data,method="POST")
try:
    response1 = request.urlopen(request1)
    print(response1.read())
except urllib.error.HTTPError as e:
    print(e.code,e.read())

course2 = {"course_name":"Machine Learning"}
data = urllib.parse.urlencode(course2)
data = data.encode("ascii")
request2 = request.Request("http://127.0.0.1:5000/Courses/2",data = data,method="POST")
try:
    response2 = request.urlopen(request2)
    print(response2.read())
except urllib.error.HTTPError as e:
    print(e.code,e.read())
'''
request3 = request.Request("http://127.0.0.1:5000/course/4",method="GET")
try:
    response3 = request.urlopen(request3)
    print(response3.read())
except urllib.error.HTTPError as e:
    print(e.code,e.read())


request7 = request.Request('http://127.0.0.1:5000/Courses/2', method='DELETE')
try:
    response7 = request.urlopen(request7)
    print(response7.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())


course = {'course_name' : 'Microservices'}
data = urllib.parse.urlencode(course)
data = data.encode('ascii')
request9 = request.Request('http://127.0.0.1:5000/Courses/3', data=data, method='PUT')
try:
    response9 = request.urlopen(request9)
    print(response9.read())
except urllib.error.HTTPError as e:
    print(e.code, e.read())