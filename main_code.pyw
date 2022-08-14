from re import L
from threading import Thread
import ctypes, os
import datetime 
import elevate
import time
import PySimpleGUI as pg
import validators as vali 

elevate.elevate()

time_start = ['2:22', '11:25']
time_end = ['2:24', '11:37']

def checktime():
    for i in range(len(time_start)):

        datetime_time_start = datetime.datetime.strptime(time_start[i], '%H:%M')

        datetime_time_end = datetime.datetime.strptime(time_end[i], '%H:%M')
        if (datetime_time_start.hour * 60 + datetime_time_start.minute <= datetime.datetime.now().hour * 60 + datetime.datetime.now().minute) and (datetime.datetime.now().hour * 60 + datetime.datetime.now().minute <= datetime_time_end.hour * 60 + datetime_time_end.minute):
            return True

    return False  

"""

def checktime(time_start, time_end): #check xem thời gian hiện tại có trong thời gian gian không
    time_start_hour = int(time_start[:2])
    time_start_min = int(time_start[-2:])
    datetime_time_start = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, time_start_hour, time_start_min)
    
    time_end_hour = int(time_end[:2])
    time_end_min = int(time_end[-2:])
    datetime_time_end = datetime.datetime(datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day, time_end_hour, time_end_min)
 
    if datetime_time_start < datetime.datetime.now() < datetime_time_end:
        return True
    
    return False

"""
exe_list = ['notepad.exe']

def blockexe(): #block từ time_start -> time_end (2 cái này là string) vd: "18:00"
    if checktime():
        #print("exe still blocked")

        for exe in exe_list:
            cmd_string = "taskkill /f /im " + exe
            os.system(cmd_string) # os.system là để chạy command trên cmd
        



hosts_path = "C:\Windows\System32\drivers\etc\hosts"

redirect = "127.0.0.1"
website_list = ["www.facebook.com","facebook.com",
      "dub119.mail.live.com","www.dub119.mail.live.com",
      "www.gmail.com","gmail.com"]


def webblock():  
    if checktime():
        with open(hosts_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass
                else:
                    # mapping hostnames to your localhost IP address
                    file.write(redirect + " " + website + "\n")
    else:
        with open(hosts_path, 'r+') as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)

            # removing hostnmes from host file
            file.truncate()


spin_hour = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']
spin_min = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59']

layout = [
    [pg.Text("ADD BLOCK TIME:", key = '-TITLEADDTIME-')],
    [pg.Text("TIME START:"), pg.Spin(spin_hour, key = '-TIMESTARTH-'), pg.Text(':'), pg.Spin(spin_min, key = '-TIMESTARTM-')],
    [pg.Text("TIME END:"), pg.Spin(spin_hour, key = '-TIMEENDH-'), pg.Text(':'), pg.Spin(spin_min, key = '-TIMEENDM-')],
    [pg.Button("ADD TIME BLOCK", key = '-ADDTIMEBLOCK-')],
    [pg.Text('', key = '-ERRORTIME-')],

    [pg.Text("ADD WEBSITE URL TO BLOCK")],
    [pg.Text("WEBSITE URL:"), pg.Input()], 
    [pg.Button("ADD WEBSITE TO BLOCK")],
    [pg.Text('', key = '-ERRORURL-')],

    [pg.Text("ADD EXE TO BLOCK")],
    [pg.Text("EXE FILE NAME"), pg.Input()], 
    [pg.Button("ADD EXE TO BLOCK")],
    [pg.Text('', key = '-ERROREXE-')],
]

window = pg.Window('nBlocker', layout)
while True:
    #webblock()
    #blockexe()
    event, values = window.read()
    if event == pg.WIN_CLOSED:
        break
    if event == '-ADDTIMEBLOCK-':
        tmp1 = values['-TIMESTARTH-'] + ':' + values['-TIMESTARTM-']
        tmp2 = values['-TIMEENDH-'] + ':' + values['-TIMEENDM-']
        window['-TITLEADDTIME-'].update(tmp1 + tmp2)

window.close()




def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except AttributeError:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

"""
if __name__ == '__main__':
    main()
"""

