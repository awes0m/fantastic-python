import requests as req
import cv2

# get AI generated image from thisartdoesnotexist.com
request= req.get('https://thisartworkdoesnotexist.com/')

# Save image in set directory
# Read RGB image
img=cv2.imread(request)

# Output img with window name as 'image'
cv2.imshow('image',img)

# Maintain output window utill
# user presses a key
cv2.waitKey(0)

# Destroying present windows on screen
