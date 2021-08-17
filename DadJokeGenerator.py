import requests
import tkinter

url = 'https://icanhazdadjoke.com/'
search_url='https://icanhazdadjoke.com/'

#====================Logic=================
def calllogic():
    global url
    global search_url
    global e
    userInput=e.get() 

    response = requests.get(search_url,
    headers={"Accept":"application/json"},
    params={"term":userInput}
    )if len(userInput) != 0 else requests.get(url,
    headers={"Accept":"application/json"})      

    data= response.json()

    joke=data['joke']
    JokeDisplay.config(text=joke)
#--------------U-I------------#
m= tkinter.Tk()
m.wm_minsize(width=900, height=100)
m.title("DAD joke generator")
Headline=tkinter.Label(m,text="""\

██████████████████████████████████████████████████
█▄─▄▄▀██▀▄─██▄─▄▄▀█████▄─▄█─▄▄─█▄─█─▄█▄─▄▄─█─▄▄▄▄█
██─██─██─▀─███─██─███─▄█─██─██─██─▄▀███─▄█▀█▄▄▄▄─█
▀▄▄▄▄▀▀▄▄▀▄▄▀▄▄▄▄▀▀▀▀▄▄▄▀▀▀▄▄▄▄▀▄▄▀▄▄▀▄▄▄▄▄▀▄▄▄▄▄▀""")
e= tkinter.Entry(m)
e.insert(0,"Enter search term or Press generate for Random")
e.focus
e.bind("<FocusIn>", lambda x: e.selection_range(0, tkinter.END))
JokeDisplay=tkinter.Label(m, text="Your dad Joke Here!")
GenerateButton=tkinter.Button(m,text="Generate",command=calllogic)

Headline.pack()
e.pack()
JokeDisplay.pack()
GenerateButton.pack()
m.mainloop()

