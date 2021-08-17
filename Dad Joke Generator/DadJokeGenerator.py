import requests
import tkinter as tk

url = 'https://icanhazdadjoke.com/'
search_url='https://icanhazdadjoke.com/search'

#====================Logic=================
def randomDadJoke():
    global url
    global search_url
    global e
    userInput=e.get() 

    response = requests.get(search_url,
    headers={"Accept":"application/json"},
    params={"term":userInput},
    )if len(userInput) != 0 else requests.get(url,
    headers={"Accept":"application/json"})      

    data= response.json()
    print (data)

    joke=data['joke']
    JokeDisplay.config(text=joke)

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
        JokeDisplay.config(text=f"There are {jokeCount} jokes\n Here's One: \n{results[0]['joke']}")
    elif jokeCount==1:
        JokeDisplay.config(text=f"There is ONE Joke\n {joke}")
    else:
        JokeDisplay.config(text=f"Sorry coudn't find a joke with your term {userInput}")

#--------------U-I------------#
m= tk.Tk()
m.wm_minsize(width=900, height=100)
m.title("DAD joke generator")
Headline=tk.Label(m,text="""\

██████████████████████████████████████████████████
█▄─▄▄▀██▀▄─██▄─▄▄▀█████▄─▄█─▄▄─█▄─█─▄█▄─▄▄─█─▄▄▄▄█
██─██─██─▀─███─██─███─▄█─██─██─██─▄▀███─▄█▀█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")

JokeDisplay=tk.Label(m, text="Your dad Joke Here!",font=("Helvetica", "12", "bold italic"))
JokeDisplay.config(padx=30,pady=30)
RandomGenerateButton=tk.Button(m,text="Random Joke",command=randomDadJoke)
e= tk.Entry(m)
e.focus
e.bind("<FocusIn>", lambda x: e.selection_range(0, tk.END))
GenerateButton=tk.Button(m,text="Generate with Random String",command=generateDadJoke)
# GenerateButton.config(padx=2,pady=2)
# RandomGenerateButton.config(padx=2,pady=2)


Headline.grid(row=0,column=0,columnspan=3)
JokeDisplay.grid(row=1,column=0,columnspan=3)
RandomGenerateButton.grid(row=2,column=1)

e.grid(row=2,column=4,columnspan=2)
GenerateButton.grid(row=3,column=4)


m.mainloop()

