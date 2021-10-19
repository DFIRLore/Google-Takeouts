import json
import contextlib

with open("Installs.json", "r") as file:
    listinput = json.load(file)

    for i in (listinput):
        print(f"Title: {i['install']['doc']['title']}")
        print(f"Installed on: {i['install']['firstInstallationTime']}")

file_path = 'data.txt'
with open('data.txt', 'w') as o:
    with contextlib.redirect_stdout(o):
        for i in (listinput):
            print(f"Title: {i['install']['doc']['title']}")
            print(f"Installed on: {i['install']['firstInstallationTime']}")
        
        
        
    
