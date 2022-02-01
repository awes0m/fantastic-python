import requests as req

url = 'https://haveibeenpwned.com/api/v2/breachedaccount/'
request= req.get('https://thispersondoesnotexist.com/')
print (request.text)