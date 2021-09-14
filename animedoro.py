from tkinter import *
from selenium import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
from plyer import notification 

root = Tk()
root.title("Animedoro")
root.config(bg='green2')
root.geometry('300x120')
root.resizable(False,False)

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

def start():
    website = websiteval.get()
    rawstudytime = int(studytimeval.get())
    timecurrent = round(time.time() * 1000)
    studytime = rawstudytime*3600
    studytitle = 'Study time starts'
    studymessage = 'Your Study time is going to start pay attention and use your brain wisely'
    animetitle = 'Anime time starts'
    animemessage = 'Anime time starts enjoy'
    while True:
        notification.notify(title=studytitle,message=studymessage,timeout=10,toast=False)
        study = int(studytime)
        time.sleep(study)
        notification.notify(title=animetitle, message=animemessage,timeout=10,toast=False)
        anime = int(study + 1800)
        time.sleep(anime)
        animeopen = driver.get(website)

websiteval = StringVar()
studytimeval = StringVar()

studytimelabel = Label(root,text='study time',font=('helvetica',10,'bold'),bg='green2',fg='black')
studytimelabel.place(x=8,y=8)

studytimeentry = Entry(root,font=('helvetica',10,'bold'),relief=FLAT, textvariable=studytimeval)
studytimeentry.place(x=112,y=8)

websitelabel = Label(root,text='website',font=('helvetica',10,'bold'),bg='green2',fg='black')
websitelabel.place(x=8,y=40)

websiteentry = Entry(root,font=('helvetica',10,'bold'),relief=FLAT,textvariable=websiteval)
websiteentry.place(x=112,y=40)

startinsidebtn = Button(root,text='Start',font=('helvetica',10,'bold'),bg='black',fg='green2',activebackground='green2',
activeforeground='black',width=20,command=start)
startinsidebtn.place(x=70,y=70)

root.mainloop()
