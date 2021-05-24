import tkinter as tk
from tkinter import *
import sys
import os, glob
from collections import namedtuple
from ctypes import byref, create_unicode_buffer, windll
from ctypes.wintypes import DWORD
from itertools import count
from tkinter import ttk
import json
import tkinter.font as tkFont
from tkinter import LEFT
import ctypes
ctypes.CDLL(r"C:\Windows\System32\kernel32.dll")



window = tk.Tk()
window.title("Optimizepanel")
space = "                 "
window.geometry("400x550")
global label
global label2
global label3
global label4
global fontsize





# set the cwd to 'OptimizePanel2.0'
#os.chdir('optimizepanel')

with open('assets\\config.json') as json_file:
    data = json.load(json_file)
    for p in data['options']:
        Arial = tkFont.Font(family="Arial", size=p['fontsize'])
        Courier = tkFont.Font(family="Courier", size=p['fontsize'])

label = tk.Label(text="Welcome to the Optimizepanel!")
label.place(relx=0.5, rely=0.1, anchor='center')



def cleancache():
    for file in glob.glob("assets\\*.txt"):
        os.remove(file)


def donothing():
    x = 0


def openoptions():
    global optionsWindow
    optionsWindow = Toplevel(window)
    optionsWindow.title("Graphical Options")
    optionsWindow.geometry("400x400")
    optionsWindow.attributes('-alpha', 0.9)
    optionsWindow.iconbitmap('logo.ico')
    global label2
    global label3
    global label4
    label2 = tk.Label(optionsWindow, text="Background color:")
    label2.place(relx=0.1, rely=0.1)
    label3 = tk.Label(optionsWindow, text="Font:")
    label3.place(relx=0.1, rely=0.3)
    label4 = tk.Label(optionsWindow, text="Font size:")
    label4.place(relx=0.1, rely=0.5)
    
    btn = ttk.Button(optionsWindow, text="Save changes",command=checkcmbo)
    btn.place(relx="0.75",rely="0.9")
    global cmb
    cmb = ttk.Combobox(optionsWindow, width="20", values=("White","Black","Grey", "Cyan"))
    cmb.place(relx="0.5",rely="0.1")

    global cmb2
    cmb2= ttk.Combobox(optionsWindow, width="20", values=("Arial","Courier"))
    cmb2.place(relx="0.5",rely="0.3")

    global cmb3
    cmb3= ttk.Combobox(optionsWindow, width="20", values=("1","2", "3", "4", "5", "6", "7","8", "9", "10", "11", "12", "13","14", "15", "16", "17", "18","19", "20"))
    cmb3.place(relx="0.5",rely="0.5")
    with open('assets\\config.json') as json_file:
        data = json.load(json_file)
        for p in data['options']:
            Arial = tkFont.Font(family="Arial", size=p['fontsize'])
            Courier = tkFont.Font(family="Courier", size=p['fontsize'])
            if p['fonts'] == 1:
                label2.configure(font=Arial)
                label3.configure(font=Arial)
                label4.configure(font=Arial)
            if p['fonts'] == 2:
                label2.configure(font=Courier)
                label3.configure(font=Courier)
                label4.configure(font=Courier)
            if p['background'] == 'White':
                optionsWindow['background']='#ffffff'
            if p['background'] == 'Grey':
                optionsWindow['background']='#626262'
            if p['background'] == 'Black':
                optionsWindow['background']='#000000'
            if p['background'] == "Cyan":
                optionsWindow['background']='#319f9c'
            


def startservice():
    newWindow = Toplevel(window)
    newWindow.title("Start a service")
    newWindow.geometry("250x100")
    newWindow.iconbitmap('logo.ico')
    newWindow.bind('<Return>', go)
    global e1
    e1 = tk.Entry(newWindow)
    e1.grid(row=0, column=1)
    e1.place(relx=0.5, rely=0.3, anchor='center')

    B5 = tk.Button(newWindow, text = "Starta ett program eller en tjänst", command = runservice)
    B5.place(relx=0.5, rely=0.6, anchor='center')
    with open('assets\\config.json') as json_file:
        data = json.load(json_file)
        for p in data['options']:
            if p['background'] == 'White':
                newWindow['background']='#ffffff'
            if p['background'] == 'Grey':
                newWindow['background']='#626262'
            if p['background'] == 'Black':
                newWindow['background']='#000000'
            if p['background'] == "Cyan":
                newWindow['background']='#319f9c'



def checkcmbo():
    if cmb.get() == "White":
        window['background']='#FFFFFF'
        optionsWindow['background']='#FFFFFF'
    if cmb.get() == "Grey":
        window['background']='#626262'
        optionsWindow['background']='#626262'
    if cmb.get() == "Black":
        window['background']='#000000'
        optionsWindow['background']='#000000'
    if cmb.get() == "Cyan":
        window['background']='#319f9c'
        optionsWindow['background']='#319f9c'

    global background
    background = cmb.get()
    global fontsize
    fontsize = cmb3.get()

    if cmb2.get() == "Arial" and cmb3.get() == "1":
        global fonts
        fonts = 1
        label.config(font=("Arial", 1))
    if cmb2.get() == "Arial" and cmb3.get() == "2":
        fonts = 1
        label.config(font=("Arial", 2))
    if cmb2.get() == "Arial" and cmb3.get() == "3":
        fonts = 1
        label.config(font=("Arial", 3))
    if cmb2.get() == "Arial" and cmb3.get() == "4":
        fonts = 1
        label.config(font=("Arial", 4))
    if cmb2.get() == "Arial" and cmb3.get() == "5":
        fonts = 1
        label.config(font=("Arial", 5))
    if cmb2.get() == "Arial" and cmb3.get() == "6":
        fonts = 1
        label.config(font=("Arial", 6))
    if cmb2.get() == "Arial" and cmb3.get() == "7":
        fonts = 1
        label.config(font=("Arial", 7))
    if cmb2.get() == "Arial" and cmb3.get() == "8":
        fonts = 1
        label.config(font=("Arial", 8))
    if cmb2.get() == "Arial" and cmb3.get() == "9":
        fonts = 1
        label.config(font=("Arial", 9))
    if cmb2.get() == "Arial" and cmb3.get() == "10":
        fonts = 1
        label.config(font=("Arial", 10))
    if cmb2.get() == "Arial" and cmb3.get() == "11":
        fonts = 1
        label.config(font=("Arial", 11))
    if cmb2.get() == "Arial" and cmb3.get() == "12":
        fonts = 1
        label.config(font=("Arial", 12))
    if cmb2.get() == "Arial" and cmb3.get() == "13":
        fonts = 1
        label.config(font=("Arial", 13))
    if cmb2.get() == "Arial" and cmb3.get() == "14":
        fonts = 1
        label.config(font=("Arial", 14))
    if cmb2.get() == "Arial" and cmb3.get() == "15":
        fonts = 1
        label.config(font=("Arial", 15))
    if cmb2.get() == "Arial" and cmb3.get() == "16":
        fonts = 1
        label.config(font=("Arial", 16))
    if cmb2.get() == "Arial" and cmb3.get() == "17":
        fonts = 1
        label.config(font=("Arial", 17))
    if cmb2.get() == "Arial" and cmb3.get() == "18":
        fonts = 1
        label.config(font=("Arial", 18))
    if cmb2.get() == "Arial" and cmb3.get() == "19":
        fonts = 1
        label.config(font=("Arial", 19))
    if cmb2.get() == "Arial" and cmb3.get() == "20":
        fonts = 1
        label.config(font=("Arial", 20))
    if cmb2.get() == "Courier" and cmb3.get() == "1":
        fonts = 2
        label.config(font=("Courier", 1))
    if cmb2.get() == "Courier" and cmb3.get() == "2":
        fonts = 2
        label.config(font=("Courier", 2))
    if cmb2.get() == "Courier" and cmb3.get() == "3":
        fonts = 2
        label.config(font=("Courier", 3))
    if cmb2.get() == "Courier" and cmb3.get() == "4":
        fonts = 2
        label.config(font=("Courier", 4))
    if cmb2.get() == "Courier" and cmb3.get() == "5":
        fonts = 2
        label.config(font=("Courier", 5))
    if cmb2.get() == "Courier" and cmb3.get() == "6":
        fonts = 2
        label.config(font=("Courier", 6))
    if cmb2.get() == "Courier" and cmb3.get() == "7":
        fonts = 2
        label.config(font=("Courier", 7))
    if cmb2.get() == "Courier" and cmb3.get() == "8":
        fonts = 2
        label.config(font=("Courier", 8))
    if cmb2.get() == "Courier" and cmb3.get() == "9":
        fonts = 2
        label.config(font=("Courier", 9))
    if cmb2.get() == "Courier" and cmb3.get() == "10":
        fonts = 2
        label.config(font=("Courier", 10))
    if cmb2.get() == "Courier" and cmb3.get() == "11":
        fonts = 2
        label.config(font=("Courier", 11))
    if cmb2.get() == "Courier" and cmb3.get() == "12":
        fonts = 2
        label.config(font=("Courier", 12))
    if cmb2.get() == "Courier" and cmb3.get() == "13":
        fonts = 2
        label.config(font=("Courier", 13))
    if cmb2.get() == "Courier" and cmb3.get() == "14":
        fonts = 2
        label.config(font=("Courier", 14))
    if cmb2.get() == "Courier" and cmb3.get() == "15":
        fonts = 2
        label.config(font=("Courier", 15))
    if cmb2.get() == "Courier" and cmb3.get() == "16":
        fonts = 2
        label.config(font=("Courier", 16))
    if cmb2.get() == "Courier" and cmb3.get() == "17":
        fonts = 2
        label.config(font=("Courier", 17))
    if cmb2.get() == "Courier" and cmb3.get() == "18":
        fonts = 2
        label.config(font=("Courier", 18))
    if cmb2.get() == "Courier" and cmb3.get() == "19":
        fonts = 2
        label.config(font=("Courier", 19))
    if cmb2.get() == "Courier" and cmb3.get() == "20":
        fonts = 2
        label.config(font=("Courier", 20))
    


    
        
    savedata(background, fonts, fontsize)
    with open('assets\\config.json') as json_file:
        data = json.load(json_file)
        for p in data['options']:

            if p['fonts'] == 1 and p['fontsize'] == "1":
                fonts = 1
                label2.config(font=("Arial", 1))
                label3.config(font=("Arial", 1))
                label4.config(font=("Arial", 1))
                print("ja")
            if p['fonts'] == 1 and p['fontsize'] == "2":
                fonts = 1
                label2.config(font=("Arial", 2))
                label3.config(font=("Arial", 2))
                label4.config(font=("Arial", 2))
            if p['fonts'] == 1 and p['fontsize'] == "3":
                fonts = 1
                label2.config(font=("Arial", 3))
                label3.config(font=("Arial", 3))
                label4.config(font=("Arial", 3))
            if p['fonts'] == 1 and p['fontsize'] == "4":
                fonts = 1
                label2.config(font=("Arial", 4))
                label3.config(font=("Arial", 4))
                label4.config(font=("Arial", 4))
            if p['fonts'] == 1 and p['fontsize'] == "5":
                fonts = 1
                label2.config(font=("Arial", 5))
                label3.config(font=("Arial", 5))
                label4.config(font=("Arial", 5))
            if p['fonts'] == 1 and p['fontsize'] == "6":
                fonts = 1
                label2.config(font=("Arial", 6))
                label3.config(font=("Arial", 6))
                label4.config(font=("Arial", 6))
            if p['fonts'] == 1 and p['fontsize'] == "7":
                fonts = 1
                label2.config(font=("Arial", 7))
                label3.config(font=("Arial", 7))
                label4.config(font=("Arial", 7))
            if p['fonts'] == 1 and p['fontsize'] == "8":
                fonts = 1
                label2.config(font=("Arial", 8))
                label3.config(font=("Arial", 8))
                label4.config(font=("Arial", 8))
            if p['fonts'] == 1 and p['fontsize'] == "9":
                fonts = 1
                label2.config(font=("Arial", 9))
                label3.config(font=("Arial", 9))
                label4.config(font=("Arial", 9))
            if p['fonts'] == 1 and p['fontsize'] == "10":
                fonts = 1
                label2.config(font=("Arial", 10))
                label3.config(font=("Arial", 10))
                label4.config(font=("Arial", 10))
            if p['fonts'] == 1 and p['fontsize'] == "11":
                fonts = 1
                label2.config(font=("Arial", 11))
                label3.config(font=("Arial", 11))
                label4.config(font=("Arial", 11))
            if p['fonts'] == 1 and p['fontsize'] == "12":
                fonts = 1
                label2.config(font=("Arial", 12))
                label3.config(font=("Arial", 12))
                label4.config(font=("Arial", 12))
            if p['fonts'] == 1 and p['fontsize'] == "13":
                fonts = 1
                label2.config(font=("Arial", 13))
                label3.config(font=("Arial", 13))
                label4.config(font=("Arial", 13))
            if p['fonts'] == 1 and p['fontsize'] == "14":
                fonts = 1
                label2.config(font=("Arial", 14))
                label3.config(font=("Arial", 14))
                label4.config(font=("Arial", 14))
            if p['fonts'] == 1 and p['fontsize'] == "15":
                fonts = 1
                label2.config(font=("Arial", 15))
                label3.config(font=("Arial", 15))
                label4.config(font=("Arial", 15))
            if p['fonts'] == 1 and p['fontsize'] == "16":
                fonts = 1
                label2.config(font=("Arial", 16))
                label3.config(font=("Arial", 16))
                label4.config(font=("Arial", 16))
            if p['fonts'] == 1 and p['fontsize'] == "17":
                fonts = 1
                label2.config(font=("Arial", 17))
                label3.config(font=("Arial", 17))
                label4.config(font=("Arial", 17))
            if p['fonts'] == 1 and p['fontsize'] == "18":
                fonts = 1
                label2.config(font=("Arial", 18))
                label3.config(font=("Arial", 18))
                label4.config(font=("Arial", 18))
            if p['fonts'] == 1 and p['fontsize'] == "19":
                fonts = 1
                label2.config(font=("Arial", 19))
                label3.config(font=("Arial", 19))
                label4.config(font=("Arial", 19))
            if p['fonts'] == 1 and p['fontsize'] == "20":
                fonts = 1
                label2.config(font=("Arial", 20))
                label3.config(font=("Arial", 20))
                label4.config(font=("Arial", 20))

            if p['fonts'] == 2 and p['fontsize'] == "1":
                fonts = 2
                label2.config(font=("Courier", 1))
                label3.config(font=("Courier", 1))
                label4.config(font=("Courier", 1))
            if p['fonts'] == 2 and p['fontsize'] == "2":
                fonts = 2
                label2.config(font=("Courier", 2))
                label3.config(font=("Courier", 2))
                label4.config(font=("Courier", 2))
            if p['fonts'] == 2 and p['fontsize'] == "3":
                fonts = 2
                label2.config(font=("Courier", 3))
                label3.config(font=("Courier", 3))
                label4.config(font=("Courier", 3))
            if p['fonts'] == 2 and p['fontsize'] == "4":
                fonts = 2
                label2.config(font=("Courier", 4))
                label3.config(font=("Courier", 4))
                label4.config(font=("Courier", 4))
            if p['fonts'] == 2 and p['fontsize'] == "5":
                fonts = 2
                label2.config(font=("Courier", 5))
                label3.config(font=("Courier", 5))
                label4.config(font=("Courier", 5))
            if p['fonts'] == 2 and p['fontsize'] == "6":
                fonts = 2
                label2.config(font=("Courier", 6))
                label3.config(font=("Courier", 6))
                label4.config(font=("Courier", 6))
            if p['fonts'] == 2 and p['fontsize'] == "7":
                fonts = 2
                label2.config(font=("Courier", 7))
                label3.config(font=("Courier", 7))
                label4.config(font=("Courier", 7))
            if p['fonts'] == 2 and p['fontsize'] == "8":
                fonts = 2
                label2.config(font=("Courier", 8))
                label3.config(font=("Courier", 8))
                label4.config(font=("Courier", 8))
            if p['fonts'] == 2 and p['fontsize'] == "9":
                fonts = 2
                label2.config(font=("Courier", 9))
                label3.config(font=("Courier", 9))
                label4.config(font=("Courier", 9))
            if p['fonts'] == 2 and p['fontsize'] == "10":
                fonts = 2
                label2.config(font=("Courier", 10))
                label3.config(font=("Courier", 10))
                label4.config(font=("Courier", 10))
            if p['fonts'] == 2 and p['fontsize'] == "11":
                fonts = 2
                label2.config(font=("Courier", 11))
                label3.config(font=("Courier", 11))
                label4.config(font=("Courier", 11))
            if p['fonts'] == 2 and p['fontsize'] == "12":
                fonts = 2
                label2.config(font=("Courier", 12))
                label3.config(font=("Courier", 12))
                label4.config(font=("Courier", 12))
            if p['fonts'] == 2 and p['fontsize'] == "13":
                fonts = 2
                label2.config(font=("Courier", 13))
                label3.config(font=("Courier", 13))
                label4.config(font=("Courier", 13))
            if p['fonts'] == 2 and p['fontsize'] == "14":
                fonts = 2
                label2.config(font=("Courier", 14))
                label3.config(font=("Courier", 14))
                label4.config(font=("Courier", 14))
            if p['fonts'] == 2 and p['fontsize'] == "15":
                fonts = 2
                label2.config(font=("Courier", 15))
                label3.config(font=("Courier", 15))
                label4.config(font=("Courier", 15))
            if p['fonts'] == 2 and p['fontsize'] == "16":
                fonts = 2
                label2.config(font=("Courier", 16))
                label3.config(font=("Courier", 16))
                label4.config(font=("Courier", 16))
            if p['fonts'] == 2 and p['fontsize'] == "17":
                fonts = 2
                label2.config(font=("Courier", 17))
                label3.config(font=("Courier", 17))
                label4.config(font=("Courier", 17))
            if p['fonts'] == 2 and p['fontsize'] == "18":
                fonts = 2
                label2.config(font=("Courier", 18))
                label3.config(font=("Courier", 18))
                label4.config(font=("Courier", 18))
            if p['fonts'] == 2 and p['fontsize'] == "19":
                fonts = 2
                label2.config(font=("Courier", 19))
                label3.config(font=("Courier", 19))
                label4.config(font=("Courier", 19))
            if p['fonts'] == 2 and p['fontsize'] == "20":
                fonts = 2
                label2.config(font=("Courier", 20))
                label3.config(font=("Courier", 20))
                label4.config(font=("Courier", 20))

def savedata(background, fonts, fontsize):
    data = {}
    data['options'] = []
    data['options'].append({
        'background': background,
        'fonts': fonts,
        'fontsize': fontsize
        })


    with open('assets\\config.json', 'w') as outfile:
        json.dump(data, outfile)
        print("Settings saved!")
        




#Meny 1
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

filemenu.add_separator()
filemenu.add_command(label="Exit", command=sys.exit)
menubar.add_cascade(label="File", menu=filemenu)
filemenu.add_separator()

#Meny 2
menubar2 = Menu(window)
filemenu2 = Menu(menubar, tearoff=0)

filemenu2.add_separator()
filemenu2.add_command(label="Graphics", command=openoptions)
menubar.add_cascade(label="Options", menu=filemenu2)
filemenu2.add_separator()




    

def listallservices():
    import subprocess
    cmd = 'WMIC PROCESS get Caption,Processid'
    proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    cleancache()
    for line in proc.stdout:
        print(line, file=open("assets\\activeapplications.txt", "a"))
    os.startfile('assets\\activeapplications.txt')



def runservice():
    try:
        os.startfile(e1.get() + ".exe")
    except Exception as e:
        print(str(e))

def go(events):
    runservice()


    
    

def listallinstalledservices():
    # Deletes list of allready installed application from earlier run
        # Creates a new InstalledApplications.txt
        cleancache()
        open("InstalledApplications.txt", "w")
        # This scripts allows to get a list of all installed products in a windows
        # machine. The code uses ctypes becuase there were a number of issues when
        # trying to achieve the same win win32com.client

        # defined at http://msdn.microsoft.com/en-us/library/aa370101(v=VS.85).aspx
        UID_BUFFER_SIZE = 39
        PROPERTY_BUFFER_SIZE = 256
        ERROR_MORE_DATA = 234
        ERROR_INVALID_PARAMETER = 87
        ERROR_SUCCESS = 0
        ERROR_NO_MORE_ITEMS = 259
        ERROR_UNKNOWN_PRODUCT = 1605

        # diff propoerties of a product, not all products have all properties
        PRODUCT_PROPERTIES = [u'Language',
                              u'ProductName',
                              u'PackageCode',
                              u'Transforms',
                              u'AssignmentType',
                              u'PackageName',
                              u'InstalledProductName',
                              u'VersionString',
                              u'RegCompany',
                              u'RegOwner',
                              u'ProductID',
                              u'ProductIcon',
                              u'InstallLocation',
                              u'InstallSource',
                              u'InstallDate',
                              u'Publisher',
                              u'LocalPackage',
                              u'HelpLink',
                              u'HelpTelephone',
                              u'URLInfoAbout',
                              u'URLUpdateInfo',]

        # class to be used for python users :)
        Product = namedtuple('Product', PRODUCT_PROPERTIES)

        def get_property_for_product(product, property, buf_size=PROPERTY_BUFFER_SIZE):
            """Retruns the value of a fiven property from a product."""
            property_buffer = create_unicode_buffer(buf_size)
            size = DWORD(buf_size)
            result = windll.msi.MsiGetProductInfoW(product, property, property_buffer, byref(size))
            if result == ERROR_MORE_DATA:
                return get_property_for_product(product, property,
                        2 * buf_size)
            elif result == ERROR_SUCCESS:
                return property_buffer.value
            else:
                return None

        def populate_product(uid):
            """Return a Product with the different present data."""
            properties = []
            for property in PRODUCT_PROPERTIES:
                properties.append(get_property_for_product(uid, property))
            return Product(*properties)

        def get_installed_products_uids():
            """Returns a list with all the different uid of the installed apps."""
            # enum will return an error code according to the result of the app
            products = []
            for i in count(0):
                uid_buffer = create_unicode_buffer(UID_BUFFER_SIZE)
                result = windll.msi.MsiEnumProductsW(i, uid_buffer)
                if result == ERROR_NO_MORE_ITEMS:
                    # done interating over the collection
                    break
                products.append(uid_buffer.value)
            return products

        def get_installed_products():
            """Returns a collection of products that are installed in the system."""
            products = []
            for puid in  get_installed_products_uids():
                products.append(populate_product(puid))
            return products

        def is_product_installed_uid(uid):
            """Return if a product with the given id is installed.
            uid Most be a unicode object with the uid of the product using
            the following format {uid}
            """
            # we try to get the VersisonString for the uid, if we get an error it means
            # that the product is not installed in the system.
            buf_size = 256
            uid_buffer = create_unicode_buffer(uid)
            property = u'VersionString'
            property_buffer = create_unicode_buffer(buf_size)
            size = DWORD(buf_size)
            result = windll.msi.MsiGetProductInfoW(uid_buffer, property, property_buffer,
                                                   byref(size))
            if result == ERROR_UNKNOWN_PRODUCT:
                return False
            else:
                return True

        apps=get_installed_products()
        for app in apps:
            print(app.InstalledProductName, file=open("assets\\InstalledApplications.txt", "a"))

        print(file=open("assets\\InstalledApplications.txt", "a"))
        os.startfile('assets\\InstalledApplications.txt')

def shutdown():
    try:
        os.system('TASKKILL /F /IM ' + e2.get() + ".exe")
    except Exception as e:
        print(str(e))

def shut(events):
    shutdown()

def shutdownservice():
    shutdownWindow = Toplevel(window)
    shutdownWindow.title("Shutdown a service")
    shutdownWindow.geometry("250x100")
    shutdownWindow.iconbitmap('logo.ico')
    shutdownWindow.bind('<Return>', shut)
    global e2
    e2 = tk.Entry(shutdownWindow)
    e2.grid(row=0, column=1)
    e2.place(relx=0.5, rely=0.3, anchor='center')

    B6 = tk.Button(shutdownWindow, text = "Stäng av ett program eller en tjänst", command = shutdown)
    B6.place(relx=0.5, rely=0.6, anchor='center')
    with open('assets\\config.json') as json_file:
        data = json.load(json_file)
        for p in data['options']:
            if p['background'] == 'White':
                shutdownWindow['background']='#ffffff'
            if p['background'] == 'Grey':
                shutdownWindow['background']='#626262'
            if p['background'] == 'Black':
                shutdownWindow['background']='#000000'
            if p['background'] == "Cyan":
                shutdownWindow['background']='#319f9c'

B = tk.Button(window, text = "Lista alla aktiva program och tjänster", command = listallservices, width=35)
B.place(relx=0.5, rely=0.2, anchor='center')

B2 = tk.Button(window, text = "Starta ett program eller tjänst", command = startservice, width=35)
B2.place(relx=0.5, rely=0.3, anchor='center')

B3 = tk.Button(window, text = "Lista alla installerade program och tjänster", command = listallinstalledservices, width=35)
B3.place(relx=0.5, rely=0.4, anchor='center')

B4 = tk.Button(window, text = "Stäng av ett program eller en tjänst", command = shutdownservice, width=35)
B4.place(relx=0.5, rely=0.5, anchor="center")


def loadpresets():
    with open('assets\\config.json') as json_file:
        data = json.load(json_file)
        for p in data['options']:
            print("----Loading Presets----")
            if p['background'] == "":
                print("No background preset found!")
            else:
                print('Background: ' + p['background'])
            if p['background'] == 'White':
                window['background']='#ffffff'
            if p['background'] == 'Grey':
                window['background']='#626262'
            if p['background'] == 'Black':
                window['background']='#000000'
            if p['background'] == "Cyan":
                window['background']='#319f9c'
                print("Cyan")
            if p['fonts'] == "":
                print("No fonts preset found!")
            else:
                print('Fonts: ', + p['fonts'])
            if p['fonts'] == 1:
                label.configure(font=Arial)
            if p['fonts'] == 2:
                label.configure(font=Courier)
            print("----Presets Configured!----")
            print('')



window.attributes('-alpha', 0.9)
window.config(menu=menubar)
window.iconbitmap('logo.ico')
cleancache()
loadpresets()
window.mainloop()
