import http.client
import json
import tkinter as tk
from tkinter import *
from tkinter.tix import *

#windows

window = tk.Tk()
window.title('CoronaV Info')
window.geometry('1600x625')
window.resizable(False, False)
window.config(bg='#272727')

def new_window():
    nw = tk.Tk()
    nw.title("Список достпних країн")
    nw.config(bg='#272727')
    nw.resizable(False, False)
    j=0
    d=0
    for i in range(48):
        tk.Label(nw,text = data[i]['Country'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White', pady=5, padx=5).grid(row  = j, column =d, padx = 9, pady = 3)
        d+=1
        if d%5==0:
            d=0
            j+=1



#Main name
tk.Label(window, text = 'Статистика по Covid-19 в європейському регіоні', font = ('Arial', 18, 'bold'), bg = '#272727', fg = 'White').grid(padx = 10, row = 0, column = 0, columnspan = 6, sticky='w')


#This function for data updating
def update():
    conn = http.client.HTTPSConnection("vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com")

    headers = {
    'x-rapidapi-key': "41c851d4cfmsha75a2dfa0a6b7bep1b6cbejsn295149a3a249",
    'x-rapidapi-host': "vaccovid-coronavirus-vaccine-and-treatment-tracker.p.rapidapi.com"
    }

    conn.request("GET", "/api/npm-covid-data/europe", headers=headers)

    res = conn.getresponse()
    data = res.read()
    data1 = json.loads(data)

    with open('data.json', 'w') as file:
        json.dump(data1, file, indent=2)
    load()

#This function contains table with information
def load():
    with open('data.json', 'r') as file:
        data = json.load(file)
    #Russia:
    tk.Label(text = data[0]['Country'], width = 20, font =('Arial', 12, 'bold'), bg = '#272727', fg = 'White').grid(row  = 1, column = 0, padx = 9, pady = 3)
    tk.Label(text = "Випадків захворювання", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 2, column = 0, padx = 9, pady = 3)
    tk.Label(text = data[0]['NewCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 3, column = 0, padx = 9, pady = 3)
    tk.Label(text = "Всього випадків", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 4, column = 0, padx = 9, pady = 3)
    tk.Label(text = data[0]['TotalCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 5, column = 0, padx = 9, pady = 3)
    tk.Label(text = "Смертей за день", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 6, column = 0, padx = 9, pady = 3)
    tk.Label(text = data[0]['NewDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 7, column =0, padx = 9, pady = 3)
    tk.Label(text = "Смертей всього", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 8, column = 0, padx = 9, pady = 3)
    tk.Label(text = data[0]['TotalDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 9, column = 0, padx = 9, pady = 3)
    tk.Label(text = "Зроблено тестів", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 10, column = 0, padx = 9, pady = 3)
    tk.Label(text = data[0]['TotalTests'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 11, column = 0, padx = 9, pady = 3)
    #Ukraine :3
    tk.Label(text = data[7]['Country'], width = 20, font =('Arial', 12, 'bold'), bg = '#272727', fg = 'White').grid(row  = 1, column = 1, padx = 9, pady = 3)
    tk.Label(text = "Випадків захворювання", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 2, column = 1, padx = 9, pady = 3)
    tk.Label(text = data[7]['NewCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 3, column = 1, padx = 9, pady = 3)
    tk.Label(text = "Всього випадків", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 4, column = 1, padx = 9, pady = 3)
    tk.Label(text = data[7]['TotalCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 5, column = 1, padx = 9, pady = 3)
    tk.Label(text = "Смертей за день", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 6, column = 1, padx = 9, pady = 3)
    tk.Label(text = data[7]['NewDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 7, column =1, padx = 9, pady = 3)
    tk.Label(text = "Смертей всього", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 8, column = 1, padx = 9, pady = 3)
    tk.Label(text = data[7]['TotalDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 9, column = 1, padx = 9, pady = 3)
    tk.Label(text = "Зроблено тестів", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 10, column = 1, padx = 9, pady = 3)
    tk.Label(text = data[7]['TotalTests'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 11, column = 1, padx = 9, pady = 3)
    #France
    tk.Label(text = data[1]['Country'], width = 20, font =('Arial', 12, 'bold'), bg = '#272727', fg = 'White').grid(row  = 1, column = 2, padx = 9, pady = 3)
    tk.Label(text = "Випадків захворювання", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 2, column = 2, padx = 9, pady = 3)
    tk.Label(text = data[1]['NewCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 3, column = 2, padx = 9, pady = 3)
    tk.Label(text = "Всього випадків", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 4, column = 2, padx = 9, pady = 3)
    tk.Label(text = data[1]['TotalCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 5, column = 2, padx = 9, pady = 3)
    tk.Label(text = "Смертей за день", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 6, column = 2, padx = 9, pady = 3)
    tk.Label(text = data[1]['NewDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 7, column =2, padx = 9, pady = 3)
    tk.Label(text = "Смертей всього", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 8, column = 2, padx = 9, pady = 3)
    tk.Label(text = data[1]['TotalDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 9, column = 2, padx = 9, pady = 3)
    tk.Label(text = "Зроблено тестів", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 10, column = 2, padx = 9, pady = 3)
    tk.Label(text = data[1]['TotalTests'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 11, column = 2, padx = 9, pady = 3)
    #Germany
    tk.Label(text = data[5]['Country'], width = 20, font =('Arial', 12, 'bold'), bg = '#272727', fg = 'White').grid(row  = 1, column = 3, padx = 9, pady = 3)
    tk.Label(text = "Випадків захворювання", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 2, column = 3, padx = 9, pady = 3)
    tk.Label(text = data[5]['NewCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 3, column = 3, padx = 9, pady = 3)
    tk.Label(text = "Всього випадків", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 4, column = 3, padx = 9, pady = 3)
    tk.Label(text = data[5]['TotalCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 5, column = 3, padx = 9, pady = 3)
    tk.Label(text = "Смертей за день", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 6, column = 3, padx = 9, pady = 3)
    tk.Label(text = data[5]['NewDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 7, column =3, padx = 9, pady = 3)
    tk.Label(text = "Смертей всього", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 8, column = 3, padx = 9, pady = 3)
    tk.Label(text = data[5]['TotalDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 9, column = 3, padx = 9, pady = 3)
    tk.Label(text = "Зроблено тестів", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 10, column = 3, padx = 9, pady = 3)
    tk.Label(text = data[5]['TotalTests'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 11, column = 3, padx = 9, pady = 3)
    #Italy
    tk.Label(text = data[3]['Country'], width = 20, font =('Arial', 12, 'bold'), bg = '#272727', fg = 'White').grid(row  = 1, column = 4, padx = 9, pady = 3)
    tk.Label(text = "Випадків захворювання", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 2, column = 4, padx = 9, pady = 3)
    tk.Label(text = data[3]['NewCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 3, column = 4, padx = 9, pady = 3)
    tk.Label(text = "Всього випадків", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 4, column = 4, padx = 9, pady = 3)
    tk.Label(text = data[3]['TotalCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 5, column = 4, padx = 9, pady = 3)
    tk.Label(text = "Смертей за день", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 6, column = 4, padx = 9, pady = 3)
    tk.Label(text = data[3]['NewDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 7, column =4, padx = 9, pady = 3)
    tk.Label(text = "Смертей всього", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 8, column = 4, padx = 9, pady = 3)
    tk.Label(text = data[3]['TotalDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 9, column = 4, padx = 9, pady = 3)
    tk.Label(text = "Зроблено тестів", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 10, column = 4, padx = 9, pady = 3)
    tk.Label(text = data[3]['TotalTests'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 11, column = 4, padx = 9, pady = 3)
load()
with open('data.json', 'r') as file:
    data = json.load(file)
#Searching countries
def your_counntry():
    val = my_country.get()
    for i in range(48):
        if val == data[i]['Country']:
            tk.Label(text = data[i]['Country'], width = 20, font =('Arial', 12, 'bold'), bg = '#272727', fg = 'White').grid(row  = 1, column = 5, padx = 9, pady = 3)
            tk.Label(text = "Випадків захворювання", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 2, column = 5, padx = 9, pady = 3)
            tk.Label(text = data[i]['NewCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 3, column = 5, padx = 9, pady = 3)
            tk.Label(text = "Всього випадків", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 4, column = 5, padx = 9, pady = 3)
            tk.Label(text = data[i]['TotalCases'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 5, column = 5, padx = 9, pady = 3)
            tk.Label(text = "Смертей за день", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 6, column = 5, padx = 9, pady = 3)
            tk.Label(text = data[i]['NewDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 7, column =5, padx = 9, pady = 3)
            tk.Label(text = "Смертей всього", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 8, column = 5, padx = 9, pady = 3)
            tk.Label(text = data[i]['TotalDeaths'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 9, column = 5, padx = 9, pady = 3)
            tk.Label(text = "Зроблено тестів", width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 10, column = 5, padx = 9, pady = 3)
            tk.Label(text = data[i]['TotalTests'], width = 20, font =('Arial', 12), bg = '#272727', fg = 'White').grid(row  = 11, column = 5, padx = 9, pady = 3)
            break

#Buttons
tk.Button(text = 'Оновити', font = ('Arial', 15, 'bold'), fg ='White', bg = '#272727', command=update).grid(row = 14, column = 0, padx = 10 ,sticky = 'w', stick = 'we', pady = 10)
tk.Button(text = 'Знайти', font = ('Arial', 15, 'bold'), fg ='White', bg = '#272727', command=your_counntry).grid(row = 13, column = 0, padx = 10 ,sticky = 'w', stick = 'we', pady = 10)
tk.Button(text = 'Доступні країни', font = ('Arial', 15, 'bold'), fg ='White', bg = '#272727', command=new_window).grid(row = 15, column = 0, padx = 10 ,sticky = 'w', stick = 'we', pady = 10)

#Enter country
my_country = tk.Entry(font =('Arial',15,'bold'), fg = 'white', bg = '#272727')
my_country.grid(row = 13, column = 1, padx = 9 ,sticky = 'w', stick = 'we', pady = 10)
tk.Label(text = 'Введіть назву країни англійською мовою (Лише країни європейського регіону)', font = ('Arial', 15, 'bold'), fg ='White', bg = '#272727').grid(row  = 14, column = 1, columnspan=4, sticky = 'wn', padx = 9)



window.mainloop()