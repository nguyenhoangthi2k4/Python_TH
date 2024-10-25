from tkinter import *
import requests
import json
from PIL import Image, ImageTk
from datetime import datetime
import ctypes

def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = screen_width//2 - width//2
    y = screen_height//2 - height//2
    root.geometry(f"{width}x{height}+{x}+{y}")

def update_time():
    dt = datetime.now()
    lblTime.config(text=dt.strftime("%H:%M:%S %p"))
    lblTime.after(1000, update_time)
        
def ApiCall():
    # API call
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="
							+ entryCityName.get() + "&units=metric&appid="+"031e0686c48695f389de4f465967f35a")
   
    api = json.loads(api_request.content)

    # Country names and Coordinates
    country = api['sys']
    Country = country['country']

    CityName = api['name']
    
    coord = api['coord']
    Longitude = coord['lon']
    Latitude = coord['lat']

    #Temperatures
    temp = api['main']
    Temp = temp['temp']
    HumiValue = temp['humidity']
    MaxTempValue = temp['temp_max']
    MinTempValue = temp['temp_min']

    # Configuration
    lblCityName.config(text=CityName)
    lblCountry.config(text=Country)

    lblLongitude.config(text=Longitude)
    lblLatitude.config(text=Latitude)

    lblTempValue.config(text=Temp)
    lblHumiValue.config(text=HumiValue)
    lblMaxTempValue.config(text=MaxTempValue)
    lblMinTempValue.config(text=MinTempValue)

if __name__ == "__main__":
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
    # Root
    root = Tk()
    root.title("Weather App")
    root.config(bg="white")
    center_window(root, 800, 800)
   
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)
    root.grid_columnconfigure(2, weight=1)
  
    root.grid_rowconfigure(0, weight=1)
    root.grid_rowconfigure(1, weight=1)
    root.grid_rowconfigure(2, weight=1)
    root.grid_rowconfigure(3, weight=1)      

    # Search city
    strCityName = StringVar()
    strCityName.set('Long Xuyen')
    entryCityName = Entry(root, textvariable=strCityName, width=30, relief="ridge", borderwidth=2)
    entryCityName.grid(row=0, columnspan=2, pady=20, padx=10, sticky="ew")

    # Search button    
    imgSearch = ImageTk.PhotoImage(Image.open(r'D:\python\Tkinter\Search.png').resize((40,40)))
    btnCityName = Button(root, image=imgSearch, height=40, command=ApiCall)
    btnCityName.grid(row=0, column=2, pady=20, sticky="")
    
    # Dates time
    frameDT = Frame(root,bg="white")
    dt = datetime.now()
    lblDate = Label(frameDT, bg="white", text=dt.strftime("%A, %d %b %Y") ,font=("PRISTINA", 25, "bold"), fg="red")
    lblDate.grid(row=0, column=0, sticky="w", padx=15)
    lblTime = Label(frameDT, bg="white", text=dt.strftime("%H:%M:%S %p"), font=("digital-7", 15, "bold"), fg="red")
    lblTime.grid(row=1, column=0, sticky="wn", padx=15)
    update_time()

    # Change theme for time
    hour = int(dt.strftime("%H"))
    if hour >= 19 or hour <= 5:
        imgMoon = ImageTk.PhotoImage(Image.open(r'D:\python\Tkinter\moon.png'))
        lblImage = Label(frameDT, image=imgMoon)
        lblImage.grid(row=0, rowspan=2,column=2)
    else:
        imgSun = ImageTk.PhotoImage(Image.open(r'D:\python\Tkinter\sun.png'))
        lblImage = Label(frameDT, image=imgSun)
        lblImage.grid(row=0, rowspan=2,column=2)    

    frameDT.grid(row=1, columnspan=2)
    
    # Country names and Coordinates
    frameInfo = Frame(root, bg="white")

    lblCityName = Label(frameInfo, bg="white", text="...", font=("",15))
    lblCityName.grid(row=0, column=0, padx=15, pady=15, sticky="w")

    lblCountry = Label(frameInfo, bg="white", text="...", font=("",15))
    lblCountry.grid(row=0, column=1, padx=15, pady=15, sticky="e")

    lblLongitude = Label(frameInfo, bg="white", text="...", font=("",15))
    lblLongitude.grid(row=1, column=0, padx=15, pady=15, sticky="w")

    lblLatitude = Label(frameInfo, bg="white", text="...", font=("",15))
    lblLatitude.grid(row=1, column=1, padx=15, pady=15, sticky="e")

    frameInfo.grid(row=2, column=0,sticky="ns")
    
    # Temperature
    frmTemp = Frame(root, bg="white")
    
    lblTemp = Label(frmTemp, bg="white", text='Temp:', font=("",15))
    lblTemp.grid(row=0, column=0, sticky="w")

    lblTempValue = Label(frmTemp, bg="white", text='...', font=("",15))
    lblTempValue.grid(row=0, column=1, sticky="w")

    lblHumidity = Label(frmTemp, bg="white", text="Humidity: ", font=("",15))
    lblHumidity.grid(row=1, column=0, sticky="w")

    lblHumiValue = Label(frmTemp, bg="white", text="...", font=("",15))
    lblHumiValue.grid(row=1, column=1)
 
    lblMaxTemp = Label(frmTemp, bg="white", text="MaxTemp: ", font=("",15))
    lblMaxTemp.grid(row=2, column=0, sticky="w")
    
    lblMaxTempValue = Label(frmTemp, bg="white", text="...", font=("",15))
    lblMaxTempValue.grid(row=2, column=1)

    lblMinTemp = Label(frmTemp, bg="white", text="MinTemp: ", font=("",15))
    lblMinTemp.grid(row=3, column=0, sticky="w")

    lblMinTempValue = Label(frmTemp, bg="white", text="...", font=("",15))
    lblMinTempValue.grid(row=3, column=1)

    frmTemp.grid(row=2, column=1,sticky="wns") 

    # Image
    imgLogo = ImageTk.PhotoImage(Image.open(r'D:\python\Tkinter\logo.png'))
    lblLogo = Label(root, image=imgLogo).grid(row=3, column=0, sticky="")
    
    root.mainloop()

