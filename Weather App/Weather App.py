import tkinter
import requests
from tkinter import BOTH, IntVar
from io import BytesIO
import PIL
from PIL import ImageTk, Image

root = tkinter.Tk()

root.title('Weather App')
root.iconbitmap('weather.ico')
root.resizable(0, 0)
root.geometry('400x400')

# fonts
sky_color = "#76c3ef"
grass_color = '#aad207'
output_color = "#dcf0fb"
input_color = '#ecf2ae'
large_font = ('SimSun', 14)
small_font = ('SimSun', 10)


def search():
    ''' use open whether api to access the wesbite'''
    global response
    URL = 'https://api.openweathermap.org/data/2.5/weather'
    api_key = 'YOUR API KEY TAKE IT FROM OPENWEATHER.ORG'

    # based on name and zip make the query string
    if search_method.get() == 1:
        querystring = {'q': city_entry.get(), 'appid': api_key,
                       'units': 'metric'}
    elif search_method.get() == 2:
        querystring = {'zip': city_entry.get(), 'appid': api_key,
                       'units': 'metric'}

    # get the api response
    response = requests.request('GET', URL, params=querystring)
    # convert the following into json format
    response = response.json()
    # dictionary format has been achived
    'print(response)'
    # example response for chennai
    """{'coord': {'lon': 80.28, 'lat': 13.09}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 
    'base': 'stations', 'main': {'temp': 300.15, 'feels_like': 306.47, 'temp_min': 300.15, 'temp_max': 300.15, 'pressure': 1011, 'humidity': 94}, 
    'visibility': 3000, 'wind': {'speed': 1, 'deg': 0}, 'clouds': {'all': 90}, 
    'dt': 1605455043, 'sys': {'type': 1, 'id': 9218, 'country': 'IN', 'sunrise': 1605400674, 'sunset': 1605442160}, 
    'timezone': 19800, 'id': 1264527, 'name': 'Chennai', 'cod': 200}"""
    getweather()
    geticon()


def getweather():
    '''grab the info from api response'''
    city_name = response['name']
    city_lat = str(response['coord']['lat'])
    city_lon = str(response['coord']['lon'])

    main_w = response['weather'][0]['main']
    desc = response['weather'][0]['description']

    temp = str(response['main']['temp'])
    feels = str(response['main']['feels_like'])

    tempmin = str(response['main']['temp_min'])
    tempmax = str(response['main']['temp_max'])
    humid = str(response['main']['humidity'])

    # enter the value in gui
    city_info.config(text=city_name + "(" + city_lat + ", " +
                     city_lon + ")", font=large_font, bg=output_color)
    whether_lab.config(text='Weather: ' + main_w + ", " +
                       desc, font=small_font, bg=output_color)
    temp_label.config(text='Temperature: ' + temp + " C",
                      font=small_font, bg=output_color)
    feelslike_lab.config(text='Feels like: '+feels + " C",
                         font=small_font, bg=output_color)
    tempmin_lab.config(text="Min temp: " + tempmin + " C",
                       font=small_font, bg=output_color)
    tempmax_lab.config(text="Max temp: " + tempmax + " C",
                       font=small_font, bg=output_color)
    humidity_lab.config(text="Humidity: " + humid,
                        font=small_font, bg=output_color)


def geticon():
    global img

    icon_id = response['weather'][0]['icon']

    url = 'https://openweathermap.org/img/wn/{icon}.png'.format(icon=icon_id)

    img_resp = requests.request('GET', url)
    img_data = img_resp.content
    img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
    iconlab.config(image=img)


# frames
sky_frame = tkinter.Frame(root, bg=sky_color, height=250)
grass_frame = tkinter.Frame(root, bg=grass_color)
sky_frame.pack(fill=BOTH, expand=True)
grass_frame.pack(fill=BOTH, expand=True)

output_frame = tkinter.LabelFrame(
    sky_frame, bg=output_color, width=325, height=225)
input_frame = tkinter.LabelFrame(grass_frame, bg=input_color, width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15, ipadx=10)

# output frame layout
city_info = tkinter.Label(output_frame, bg=output_color)
whether_lab = tkinter.Label(output_frame, bg=output_color)
temp_label = tkinter.Label(output_frame, bg=output_color)
feelslike_lab = tkinter.Label(output_frame, bg=output_color)
tempmin_lab = tkinter.Label(output_frame, bg=output_color)
tempmax_lab = tkinter.Label(output_frame, bg=output_color)
humidity_lab = tkinter.Label(output_frame, bg=output_color)
iconlab = tkinter.Label(output_frame, bg=output_color)

city_info.pack(pady=(3, 0))
whether_lab.pack(pady=(0, 2))
temp_label.pack(pady=(0, 2))
feelslike_lab.pack(pady=(0, 2))
tempmin_lab.pack(pady=(0, 2))
tempmax_lab.pack(pady=(0, 1))
humidity_lab.pack()
iconlab.pack(pady=8)

# input frame
city_entry = tkinter.Entry(input_frame, width=20, font=large_font)
submit_button = tkinter.Button(
    input_frame, text='Submit', font=large_font, bg=input_color, command=search)

search_method = IntVar()
search_method.set(1)
search_city = tkinter.Radiobutton(input_frame, text='Search By City Name',
                                  variable=search_method, value=1, font=small_font, bg=input_color)
search_zip = tkinter.Radiobutton(input_frame, text='Search By Zip Code',
                                 variable=search_method, value=2, font=small_font, bg=input_color)

city_entry.grid(row=0, column=0, padx=10, pady=(10, 0))
submit_button.grid(row=0, column=1, padx=10,
                   pady=(10, 0), sticky='e', ipadx=15)
search_city.grid(row=1, column=0, pady=2, sticky='w')
search_zip.grid(row=1, column=0, pady=2, padx=5, sticky='e', columnspan=2)


# run the windows main loop
root.mainloop()
