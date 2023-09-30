# Script to add back button for files
import os
import re

imagePath = 'img/back.svg'
rootFolder = 'DesignPatterns'

def button(imgSrc: str, pagePath: str):
    return f'[<img src="{imgSrc}" style="width:8em;">]({pagePath})'

for (dirpath, dirnames, filenames) in os.walk(rootFolder):
    # print(f'{dirpath}:\n  {dirnames}\n  {filenames}')
    for name in filenames:
        with open(f'{dirpath}/{name}', 'r+') as f:
            string = f.read()
            match = re.findall(r'\((.*?\.md)\)', string)
            if match is None: continue
            for i in match:
                print(i)
