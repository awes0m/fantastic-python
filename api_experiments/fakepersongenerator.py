import requests as req

request= req.get('https://thispersondoesnotexist.com/')
print (request.text)