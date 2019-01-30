import xmltodic

with open('sample.xml') as file:
    res = xmltodic.parse(file.read())

print(res['data']['country'][0]['rank'])


