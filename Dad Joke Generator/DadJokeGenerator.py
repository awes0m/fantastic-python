import requests
import tkinter as tk
from tkinter import messagebox

url = 'https://icanhazdadjoke.com/'
search_url='https://icanhazdadjoke.com/search'

#====================Logic=================
def randomDadJoke():
    global url
    global search_url
    global e
    response=requests.get(url,headers={"Accept":"application/json"})      

    data= response.json()
    

    joke=data['joke']
    messagebox.showinfo("You have been served ",joke)

def generateDadJoke():
    global search_url,e

    userInput=e.get()
    response = requests.get(
    search_url,
    headers={"Accept":"application/json"},
    params={"term": userInput},
    ).json()
    jokeCount=0
    results=response['results']
    jokeCount=len(results)
    joke = results[0]['joke']

    if jokeCount>1:
        messagebox.showinfo("You have been served",f"There are {jokeCount} jokes\n Here's One: \n{results[0]['joke']}")
    elif jokeCount==1:
        messagebox.showinfo("You have been served",f"There is ONE Joke\n {joke}")
    else:
        messagebox.showinfo("You have been served",f"Sorry coudn't find a joke with your term {userInput}")

#--------------U-I------------#
m= tk.Tk()
m.wm_minsize(width=900, height=100)
m.title("DAD joke generator")
Headline=tk.Label(m,text="""\

██████████████████████████████████████████████████
█▄─▄▄▀██▀▄─██▄─▄▄▀█████▄─▄█─▄▄─█▄─█─▄█▄─▄▄─█─▄▄▄▄█
██─██─██─▀─███─██─███─▄█─██─██─██─▄▀███─▄█▀█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")


RandomGenerateButton=tk.Button(m,text="Random Joke",command=randomDadJoke)
e= tk.Entry(m)
e.focus
e.bind("<FocusIn>", lambda x: e.selection_range(0, tk.END))
GenerateButton=tk.Button(m,text="Generate with Random String",command=generateDadJoke)



Headline.pack()
RandomGenerateButton.pack()
e.pack()
GenerateButton.pack()
m.mainloop()

