import sys
import pyperclip as clipboard
import json

SAVED_DATA="multi-clipboard\clipboard.json"

def save_data(filepath,data):
     try:
         with open(filepath, 'w') as f:
            json.dump(data, f)
     except:
        print("Error saving data")

def load_data(filepath):
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except:
        return {}


        
if len(sys.argv)==2:
     command=sys.argv[1]
     data=load_data(SAVED_DATA)
         # print(command)
     if command in ["save", "s","--save","--s"]:
          key=input("Enter the key: ")
          data[key]=clipboard.paste()
          print("Saving...")
          save_data(SAVED_DATA,data)
          print("Saved!")


     elif command in ["load", "l","--load","--l"]:
          key=input("Enter the key: ")
          print("Loading...")
          if key in data:
              clipboard.copy(data[key])
              print(f" [ {clipboard.paste()} ] copied to clipboard! \n paste CRTL+V to paste")
          else:
              print("Key not found!")

     elif command in ["list", "ls","--list","--ls"]:
          print("Listing...")
          print("{'key' :'value'}")
          print (data)
     else:
          print("Invalid command")
        
