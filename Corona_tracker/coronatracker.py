import requests
import tkinter as tk
import datetime




def getData():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    totalCases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    total_recovered = str(json_data['recovered'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    updated_at = json_data['updated']
    dated = datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text="Total Cases "+totalCases+
                 "\n Total Deaths "+total_deaths+
                 "\n Total recovered "+total_recovered+
                 "\n \n Today: \n cases: "+today_cases+
                 "\n deaths: "+today_deaths+
                 "\n recovered: "+today_recovered)
    label2.config(text=dated)


canvas = tk.Tk()

canvas.geometry("400x400")
canvas.title("corona tracker App")

f = ("popins", 15, "bold")
button = tk.Button(canvas, text="Reload", command=getData)
button.pack(pady=10)

label = tk.Label(canvas, font=f)
label.pack(pady=20)

label2 = tk.Label(canvas, font=8)
label2.pack()
getData()

canvas.mainloop()
