import os
import re
import time
from pathlib import Path

def sync(files, update, txstrdir=0):
    for file in files:
        lines = []
        with file.open(encoding='utf-8', errors='replace') as f:
            lines = f.readlines()
    
        with file.open('w', encoding='utf-8') as outfile:
            i = 0
            while i < len(lines):
                if lines[i].strip() == "> BEGIN STRING":
                    i += 1
                    string = lines[i].strip()
                    i += 1
                    while(lines[i][0] != ">"):
                        string += "\n"+lines[i].strip()
                        i += 1
                    while(lines[i][0] == ">"):
                        i += 1
                    trans = update.get(string)
                    if not trans and "/" in string and "サック" in string:
                        print(string[0:string.find("/")])
                    if not trans and "/" in string and update.get(string[0:string.find("/")]):
                        trans = update.get(string.split("/")[0].strip())+string[string.find("/"):]
                    elif not trans and False:
                        for t in update.keys():
                            if string.strip() in t and len(t)-len(string) < 10:
                                string = t
                                print(string)
                        trans = update.get(string)
                        if trans:
                            trans = trans.replace('"',"").replace("「","")
                    elif not trans and "/" in string and len(string)>3 and False:
                        for t in update.keys():
                            if t.strip() in string and len(t)>3:
                                trans = string.replace(t.strip(), update[t].strip())
                                print(trans)
                                break
                    if trans and lines[i]!=trans:
                        #print(lines[i].strip()+" replaced by "+trans.strip())
                        lines[i] = trans+"\n"
                    else:
                        if string[0]=='"' and txstrdir==0:
                            noquote = string.replace('"','')
                            trans = update.get(noquote)
                            if trans:
                                lines[i] = string.replace(noquote.strip(), trans.strip())
                                #print("Text to string: "+lines[i].strip())
                        elif txstrdir!=0:
                            withquote = '"'+string.strip()+'"'+"\n"
                            trans = update.get(withquote)
                            if trans:
                                lines[i] = trans.replace('"','')
                                #print("String to text: "+lines[i].strip())

                    i += 2
                else:
                    i += 1
                
            outfile.writelines(lines)

if __name__ == "__main__":
    current_dir = Path.cwd()
    translations = {}

    #main_files = [current_dir / "patch" / "Scripts.txt", current_dir / "patch" / "Skills.txt"]
    main_files = []
    for file in (current_dir / "SQ1patch").rglob("*.txt"):
        if not "Unused" in str(file) and "ScriptsSR" in str(file):
            main_files.append(file)

    print("===Reading current translations===")
    for translations_file in main_files:
        #print(translations_file.as_posix())
        lines = []
        with translations_file.open('r', encoding='utf-8') as trans_file:
            lines = trans_file.readlines()
        i = 0
        while i < len(lines):
            if lines[i].strip() == "> BEGIN STRING":
                i += 1
                string = lines[i].strip()
                i += 1
                while(lines[i][0] != ">"):
                    string += "\n"+lines[i].strip()
                    i += 1
                while(lines[i][0] == ">"):
                    i += 1
                if lines[i].strip():
                    multiline = lines[i].strip()
                    while not lines[i+1][0]==">":
                        i+=1
                        multiline += "\n"+lines[i].strip()
                    #stripped = multiline
                    stripped = multiline.split("/")[0]+"\n" if "/" in multiline else multiline
                    string = string.split("/")[0]+"\n" if "/" in string else string
                    if string == '"き"':
                        print(stripped)
                    #string = string.replace('"','')
                    #stripped = stripped.replace('"','')
                    #string = string.replace("\\\\", "\\")
                    #stripped = stripped.replace("\\\\", "\\")
                    translations[string] = stripped
                    #print(string.strip()+" = "+lines[i].strip())

                i += 2
            else:
                i += 1

    print("===Updating mod translations===")
    #main_files = [current_dir / "patch" / "Scripts.txt"]
    #main_files = [current_dir / "patch" / "States.txt"]
    main_files = [current_dir / "patch" / "Scripts.txt"]
    #for file in (current_dir / "patch").rglob("*.txt"):
    #    main_files.append(file)
        
    sync(main_files, translations, 0)
    #sync(main_files, translations, 1)
