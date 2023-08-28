from tkinter import *
from configparser import ConfigParser
from tkinter import messagebox
import requests
import json

url= "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}"


config_file='config.ini'
config= ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']


def get_weather(city):
    result=requests.get(url.format(city,api_key))
    if result:
        json=result.json()                                            #City,country, celsius, fahrenheit, icon, weather
        city= json['name']
        country=json['sys']['country']
        kelvin_temp=json['main']['temp']
        celsius_temp= kelvin_temp-273.15
        fahr_temp= (kelvin_temp-273.15) * 9/5 + 32
        icon=json['weather'][0]['icon']
        weather=json['weather'][0]['main']
        final=(city,country,celsius_temp,fahr_temp,icon,weather)
        return final

    else:
        return None


def search():
    city=city_text.get()
    weather=get_weather(city)
    if weather:
        location_lab['text']= "{}, {}".format(weather[0], weather[1])
        img["file"]="Weather_icons/{}.png".format(weather[4])
        temp_lab['text']="{:.2f}°C, {:.2f}°F".format(weather[2],weather[3])
        weather_lab['text']= weather[5]
    else:
        messagebox.showerror('Error',"City NOT FOUND {}".format(city))
    
 


app=Tk()



app.title("Weather app")
app.geometry("700x350")

city_text=StringVar()
city_entry= Entry(app, textvariable=city_text,width=12,font=(15))
city_entry.pack()

search_but=Button(app,text="Search",width=12,command=search,font=('bold',18))
search_but.pack()

location_lab= Label(app,text="", font=('bold',18))
location_lab.pack()                                                    #display the location on the screen

img= PhotoImage(file='')
image=Label(app,image=img)
image.pack()

temp_lab=Label(app,text="",font=("bold",15))
temp_lab.pack()                                                        #display the Temperature on the screen


weather_lab=Label(app,text="",font=("bold",15))
weather_lab.pack()                                                     #display the Weather on the screen





app.mainloop()
