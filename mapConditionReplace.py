import os
import re

def replace_strings_in_files(folder_path, mod_path, replace_dict):
    for filename in os.listdir(folder_path):
        if (filename.startswith("Map") or filename.startswith("Common") or filename.startswith("Save")) and os.path.isfile(os.path.join(folder_path, filename)):
            with open(os.path.join(folder_path, filename), 'rb') as file:
                content = file.read()

            utf8_parts = re.findall(rb'\(\"[^\$\"]{3,30}\"\)', content)
            utf8_parts += re.findall(rb'== \"[^\$\"]{3,30}\"', content)
            if filename.startswith("Save"):
                utf8_parts += re.findall(rb'\".(.{3,30}\/[0-9]{1,2}\/[0-9]{1,2}\/[0-9]{1,2})', content)
            replaced = False

            savedspot = -1
            saveddiff = 0

            for part in utf8_parts:
                #print(part.decode())
                replacement = replace_dict.get(part)
                if replacement:
                    diff = len(part)-len(replace_dict[part])
                    #replacement += " ".encode('utf-8')*diff
                    print(filename+replacement.decode())
                    replaced = True
                    lensymbol = content.rfind(rb"$", 0, content.find(part))-1
                    lensymbol = max(content.rfind(rb"@", 0, content.find(part))-1, lensymbol)
                    if filename.startswith("Save"):
                        lensymbol = content.find(part)-1
                    if diff > 0:
                        #print(lensymbol)
                        #print(content[lensymbol-2])
                        replacement += rb" "*diff
                        diff = 0
                        #lensymbol = content.rfind(rb"$", lensymbol-30, lensymbol)-1
                        #lensymbol = max(content.rfind(rb"@", lensymbol-30, lensymbol)-1, lensymbol)
                    ifspot = content.rfind(rb"if", lensymbol-4, lensymbol)-1
                    elseifspot = content.rfind(rb"elseif", lensymbol-8, lensymbol)-1
                    notspot = content.rfind(rb"not", lensymbol-5, lensymbol)-1
                    if ifspot > 0:
                        lensymbol = ifspot
                        print("ifspot")
                    if elseifspot > 0:
                        lensymbol = elseifspot
                        print("elseifspot")
                    if notspot > 0:
                        lensymbol = notspot
                        print("notspot")
                    if ifspot < 0 and savedspot >= 0:
                        lensymbol = savedspot
                        savedspot = -1
                    elif ifspot < 0 and notspot < 0 and content.find(rb"$", lensymbol+2) < content.find(rb";", lensymbol+2):
                        savedspot = lensymbol
                        saveddiff = diff
                        print(lensymbol)
                        content = content.replace(part, replacement, 1)
                        continue
                    if diff != 0:
                        newbyte = bytes(chr(content[lensymbol]-(diff+saveddiff)),'utf-8')
                        content = content[:lensymbol]+newbyte+content[lensymbol+1:]
                    content = content.replace(part, replacement, 1)
                    saveddiff = 0
            #utf8_parts = re.findall(rb'.\$game_actors\[101\]\.have_ability\?\("[^;]*"\).*?;', content)
            #utf8_parts += re.findall(rb'.\$game_variables\[\d\] {0,}== {0,}"[^;]*".*?;', content)
            #for part in utf8_parts:
            #    replacement = part[1:]
            #    replacement = bytes(chr(len(part)+3),'utf-8')+replacement
            #    content = content.replace(part, replacement)

            #newContent = content.replace("ギルゴーン".encode(), "Gilgorn".encode())
            #newContent = newContent.replace("ロウラット".encode(), "Lauratt".encode())
            #if newContent != content:
            #    content = newContent
            #    replaced = True
            #    print("special case: "+filename)

            for key in replace_dict:
                if key.decode()[-1] == ';':
                    #print(key.decode())
                    matches = content.count(key)
                    if matches > 0:
                        print(str(matches)+" matches for "+key[2:-1].decode()+" in "+filename)
                        content = content.replace(key, replace_dict[key])
                
            if replaced:
                with open(os.path.join(mod_path, "Q_"+filename), 'wb') as modified_file:
                    modified_file.write(content)
                print("Modified "+filename)

def Troops(folder_path, mod_path, filename="Troops.rxdata"):
    with open(os.path.join(folder_path, filename), 'rb') as file:
        content = file.read()
    content = content.replace("オリビア".encode(), "Olivia".encode())
    with open(os.path.join(mod_path, "Q_"+filename), 'wb') as modified_file:
        modified_file.write(content)

if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
    folder_name = current_dir.split("\\")[-1].replace("_patch", "_translated")
    folder_path = os.path.join(parent_dir, folder_name+"\\Data")
    mod_path = folder_path
    mod_path = os.path.join(parent_dir, folder_name)
    #mod_path = folder_path
    
    replacements = {}

    lines = []
    with open("patch/Scripts.txt", 'r', encoding='utf-8') as trans_file:
        lines = trans_file.readlines()
    with open("patch/Armors.txt", 'r', encoding='utf-8') as trans_file:
        lines += trans_file.readlines()
    with open("patch/Classes.txt", 'r', encoding='utf-8') as trans_file:
        lines += trans_file.readlines()
    i = 0
    binary_replacements = {}
    while i < len(lines):
        if lines[i].strip() == "> BEGIN STRING":
            i += 1
            string = lines[i].strip().replace('"', '')
            i += 1
            while(lines[i][0] == ">"):
                i += 1
            if lines[i].strip():
                noquotes = lines[i].strip().replace('"', '')

                if lines[i].count("/") > 1 and not "\\" in lines[i]:
                    replacements[string] = lines[i].strip()
                else:
                    rep = "(\""+noquotes+"\")"
                    replacements["(\""+string+"\")"] = rep
                    rep = "== \""+noquotes+"\""
                    replacements["== \""+string+"\""] = rep

                if len(lines[i].strip()) < 30 and not "(" in lines[i] and not "\\" in lines[i]:
                    #a = string.split("/")[0].strip()
                    a = string.strip()
                    a = '"'.encode()+bytes([len(a.encode())+5])+a.encode()+';'.encode()
                    #b = lines[i].split("/")[0].strip()
                    b = lines[i].strip()
                    b = '"'.encode()+bytes([len(b.encode())+5])+b.encode()+';'.encode()
                    binary_replacements[a] = b
                    
                    a = string.strip().replace('"','')
                    a = '"'.encode()+bytes([len(a.encode())+5])+a.encode()+';'.encode()
                    b = lines[i].strip().replace('"','')
                    b = '"'.encode()+bytes([len(b.encode())+5])+b.encode()+';'.encode()
                    binary_replacements[a] = b
            i += 2
        else:
            i += 1

    
    for key in replacements.keys():
        binary_replacements[key.encode('utf-8')] = replacements[key].encode('utf-8')
    replace_strings_in_files(folder_path, mod_path, binary_replacements)
    Troops(folder_path, mod_path)
