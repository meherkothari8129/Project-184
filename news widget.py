from tkinter import *
from tkinter import ttk
import psutil 
from psutil._common import BatteryTime

root = Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)
style = ttk.Style(root)
style.layout('ProgressBarStyle',
             [('Horizontal.Progress.trough',
               {'children': [('Horizontal.Progress.pbar',
                              {'side':'right','sticky':'ns'})],
                'sticky':'nsew'}),
              ('Horizontal.Progressbar.label', {'sticky':''})])
bar = ttk.Progressbar(root, maximum = 100, style = 'ProgressBarStyle')
bar.place(relx = 0.5, rely = 0.2, anchor = CENTER)

battery_life = Label(root, font = 'arial 15 bold', bg ='black', fg="white")
battery_life.place(relx=0.5,rely=0.5, anchor=CENTER)

def convertTime(seconds): 
    minutes, seconds = divmod(seconds, 60) 
    hours, minutes = divmod(minutes, 60) 
    return str(hours)+" : "+str(minutes)+" : "+str(seconds)

def getBatterylife(): 
    battery = psutil.sensors_battery() 
    bar['value'] = battery.percent 
    style.configure('ProgressBarStyle', text=str(battery.percent)+' %') 
    battery_left = convertTime(battery.secsleft) 
    if battery.secsleft == BatteryTime.POWER_TIME_UNLIMITED: 
        battery_life['text'] = 'Unplugged the battery! \n And Rerun the code again.' 
    elif battery.secsleft == BatteryTime.POWER_TIME_UNKNOWN: 
        battery_life['text'] ='Battery life did not detected. \n Please, Run the code again!' 
    else: 
        battery_life['text'] ="Battery Life : "+battery_left 
        root.after(1000, getBatterylife)
        
getBatterylife()
root.mainloop()



