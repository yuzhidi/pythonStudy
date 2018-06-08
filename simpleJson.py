import json
#!/usr/bin/python
import json

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

print data[0]
json = json.dumps(data)
print json

data =  { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 }
print data['b']
# print data['w']
