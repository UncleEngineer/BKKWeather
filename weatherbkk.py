# Create By Uncle Engineer
# www.facebook.com/UncleEngineer

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as req
from tkinter import *
from tkinter import ttk

def checkweather():
    
    url = 'https://www.tmd.go.th/province.php?id=37'
    # id=37 for bangkok
    webopen = req(url)
    page_html = webopen.read()
    webopen.close()
    page_soup = soup(page_html, "html.parser")
    data = page_soup.findAll('td',{'class':'strokeme'})
    temp = data[0].text
    temptext.set(temp)
    
    

GUI = Tk()
GUI.title('Uncle Engineer BKK Temp')
GUI.geometry('500x200')

temptext = StringVar()

L0 = ttk.Label(GUI, text='อุณหภูมิกรุงเทพตอนนี้', font=('TH Sarabun New',25) )
L0.pack(padx=10,pady=10)

L1 = ttk.Label(GUI, textvariable=temptext, foreground='green', font=('tohama',25) )
L1.pack(padx=10,pady=10)

B1 = ttk.Button(GUI, text='Update', command=checkweather)
B1.pack(padx=10,pady=10)

GUI.mainloop()
