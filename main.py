import os.path
import random
import string
import tkinter
from tkinter import ttk
from tkinter import filedialog
import json
from tkinter import messagebox
import base64


keys = {}
mirrorKeys = {}

for i in string.printable:
    keys[i] = len(keys)

for i in string.printable:
    mirrorKeys[len(mirrorKeys)] = i

def encode(text : str):
    splnum = ""
    for i in range(1,10): # В ЭТОЙ СТРОКЕ ГЕНЕРАЦИЯ ГОВНА
        splnum += str(len(keys) + random.randint(
        10,
        1000
    ))
    endstr = ""

    for char in text:
        endstr = endstr + str(keys[char]) + str(splnum)

    return [endstr,splnum]

def decode(text : str,splnum : int):
    decodestr = ""
    for i in text.split(str(splnum)):
        for v in keys.keys():
            if str(keys[v]) == i:
                decodestr = decodestr + v

    return decodestr

def save_file(data,key,keyName):
    file_path = filedialog.asksaveasfilename(
        defaultextension=key,
        filetypes=[(keyName, "*"+key), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path,"w") as f:
            f.write(str(data))

def open_file(key,keyName):
    file_path = filedialog.askopenfilename(
        defaultextension=key,
        filetypes=[(keyName, "*"+key), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path,"r") as f:
            return [file_path,f.read()]

# save_file(str(keys),"help","help by gleb")

def createWindow(name : str):
    win = tkinter.Tk()
    win.geometry("250x200")
    win.title(name)

    if name == "encode":

        def encd():
            data = encode(obj1.get('1.0', 'end'))
            save_file(data[0],"gss","glebka super seckret")
            save_file(data[1],"gsk","glebka super key")

        obj1 = tkinter.Text(win,height=10)
        obj1.pack()
        obj2 = ttk.Button(win,text=name,width=55,command=encd)
        obj2.pack()
    else:
        def sel1():
            if not os.path.exists("temp.json"):
                with open("temp.json", "w") as f:
                    f.write(json.dumps({"gss": "", "gsk": ""}))
            fil1 = open_file("gss","glebka super seckret")
            with open("temp.json", "r",encoding="utf-8") as f:
                tdata = json.load(f)
            tdata["gss"] = fil1[0]
            with open("temp.json", "w",encoding="utf-8") as f:
                f.write(json.dumps(tdata))
            obj2.config(text=fil1[0])
        def sel2():
            if not os.path.exists("temp.json"):
                with open("temp.json", "w") as f:
                    f.write(json.dumps({"gss": "", "gsk": ""}))
            fil2 = open_file("gsk","glebka super key")
            with open("temp.json", "r",encoding="utf-8") as f:
                tdata = json.load(f)
            tdata["gsk"] = fil2[0]
            with open("temp.json", "w",encoding="utf-8") as f:
                f.write(json.dumps(tdata))
            obj4.config(text=fil2[0])
        def decol():
            if not os.path.exists("temp.json"):
                with open("temp.json", "w") as f:
                    f.write(json.dumps({"gss": "", "gsk": ""}))

            with open("temp.json", "r",encoding="utf-8") as f:
                tdata = json.load(f)

            if os.path.isfile(tdata["gss"]) and os.path.isfile(tdata["gsk"]):
                with open(tdata["gss"],"r") as f:
                    gss = f.read()
                with open(tdata["gsk"],"r") as f:
                    gsk = f.read()

                endString = ""
                for i in gss.split(gsk):
                    if i == "":
                        break
                    else:
                        endString += mirrorKeys.get(int(i),"")
                else:
                    return
                messagebox.showinfo("Decoded",endString)


        obj1 = ttk.Label(win,text="Secret",width=55)
        obj2 = ttk.Button(win,text="Select File",width=55,command=sel1)
        obj3 = ttk.Label(win, text="Key", width=55)
        obj4 = ttk.Button(win, text="Select File", width=55,command=sel2)
        obj5 = ttk.Label(win, text=name, width=55)
        obj6 = ttk.Button(win, text=name, width=55,command=decol)

        obj1.pack()
        obj2.pack()
        obj3.pack()
        obj4.pack()
        obj5.pack()
        obj6.pack()


    win.mainloop()

def cwe():
    name = "encode"
    createWindow(name)

def cwd():
    name = "decode"
    createWindow(name)

root = tkinter.Tk()
root.title("GEAD")
root.geometry("250x50")

encodemainbtn = ttk.Button(root,text="encode",width=55,command=cwe)
decodemainbtn = ttk.Button(root,text="decode",width=55,command=cwd)
encodemainbtn.pack()
decodemainbtn.pack()

root.mainloop()