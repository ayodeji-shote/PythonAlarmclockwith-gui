# Necessary modules for the alarm clock
from tkinter import *
import datetime
import time
import winsound


def alarm(alarmset):
    while True:
        time.sleep(1)
        current = datetime.datetime.now()
        now = current.strftime("%H:%M:%S")
        date = current.strftime("%Y-%m-%d")
        print("The date you set is :", date)
        print(now)
        if now == alarmset:
            print("Wake up ")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break


def currenttime():
    alarmset = f"{hour.get()} : {min.get()} : {sec.get()}"
    alarm(alarmset)

clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")
time_format = Label(clock, text="Enter time in 24 hour format!",
										fg="white", bg="black", font="Arial").place(x=60, y=120)
addTime = Label(clock, text="Hour  Min   Sec", font=60).place(x=110)
setYourAlarm = Label(clock, text="When to wake you up", fg="blue",
											relief="solid", font=("Helevetica", 7, "bold")).place(x=0, y=29)
# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()
# Takes the users time input 
submit = Button(clock, text="Set Alarm", fg="blue",
								width=10, command=currenttime).place(x=130, y=70)
# Time required to set the alarm clock:
hourTime = Entry(clock, textvariable=hour, bg="white",
									width=11).place(x=130, y=40)
minTime = Entry(clock, textvariable=min, bg="white",
								width=11).place(x=170, y=40)
secTime = Entry(clock, textvariable=sec, bg="white",
								width=11).place(x=230, y=40)
clock.mainloop()
