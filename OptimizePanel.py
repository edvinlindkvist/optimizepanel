import sys
import os, glob
from datetime import datetime, date
from PyQt5 import QtGui, QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QMovie, QIcon, QPixmap, QColor
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QColorDialog, QFrame, QLabel, QInputDialog, QLineEdit, QLayout, QPushButton
from PyQt5.QtCore import pyqtSlot, QSize
from collections import namedtuple
from ctypes import byref, create_unicode_buffer, windll
from ctypes.wintypes import DWORD
from itertools import count

def cleancache():
    for file in glob.glob("*.txt"):
        os.remove(file)
        

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.title = 'MultiMenu'
        self.left = (1920/2)-250
        self.top = 300
        self.width = 250
        self.height = 250
        self.initUI()
        app.setStyle('Fusion')

    def updateUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    def initUI(self):
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(qApp.quit)

        openAct = QAction(QIcon('open.png'), '&Open', self)
        openAct.setShortcut('Ctrl+E')
        openAct.setStatusTip('Open application')
        openAct.triggered.connect(self.on_click3)

        self.statusBar()

        #Flik "File"
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(exitAct)
        #Flik "Edit"
        menubar2 = self.menuBar()
        fileMenu = menubar2.addMenu('&Edit')
        fileMenu.addAction(openAct)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #Alla LABL
        self.labl = QLabel(self)
        self.labl.move(85,20)
        self.labl2 = QLabel(self)
        self.labl2.move(50,70)
        self.labl3 = QLabel(self)
        self.labl3.move(50,90)
        self.labl4 = QLabel(self)
        self.labl4.move(50,110)
        self.labl5 = QLabel(self)
        self.labl5.move(50,130)
        self.labl6 = QLabel(self)
        self.labl6.move(50,150)
        self.labl7 = QLabel(self)
        self.labl7.move(50,200)
        self.labl.setText('Vad vill du göra?')

        button2 = QPushButton('Lista alla aktiva program', self)
        button2.move(25,70)
        button2.clicked.connect(self.on_click2)
        button2.resize(200, 22)
        button3 = QPushButton('Starta ett program', self)
        button3.move(25,100)
        button3.clicked.connect(self.on_click3)
        button3.resize(200, 22)
        button5 = QPushButton('Lista alla installerade program', self)
        button5.move(25,130)
        button5.clicked.connect(self.on_click5)
        button5.resize(200, 22)
        button6 = QPushButton('Starta Program', self)
        button6.move(25,270)
        button6.clicked.connect(self.approve)
        button6.resize(200, 27)
        button7 = QPushButton('Stäng av ett program', self)
        button7.move(25,160)
        button7.clicked.connect(self.closeFile)
        button7.resize(200, 22)
        button8 = QPushButton('Minimera', self)
        button8.move(75,310)
        button8.clicked.connect(self.on_click4)
        button8.resize(100, 22)

        self.line = QLineEdit(self)
        self.line.resize(0,0)
        self.line2 = QLineEdit(self)
        self.line2.resize(0,0)
        self.line3 = QLineEdit(self)
        self.line3.resize(0,0)
        self.line4 = QLineEdit(self)
        self.line4.resize(0,0)
        self.show()

    def on_click2(self):
        import subprocess
        cmd = 'WMIC PROCESS get Caption,Processid'
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
        cleancache()
        for line in proc.stdout:
            print(line, file=open("activeapplications.txt", "a"))
        os.startfile('activeapplications.txt')

    def on_click3(self):
        #Lägg till loading.gif
        self.line2.move(70, 240)
        self.line2.resize(100, 65)
        self.line2.adjustSize()
        self.line4.move(-9999,-9999)
        self.height = 340
        self.updateUI()

    def on_click4(self):
        self.line2.move(70, 250)
        self.height = 250
        self.updateUI()

    def closeFile(self):
        self.height = 340
        self.updateUI()
        self.line4.move(70, 240)
        self.line4.resize(100, 65)
        self.line4.adjustSize()
        self.line2.move(-9999,-9999)
        try:
            os.system('TASKKILL /F /IM ' + self.line4.text())
        except Exception as e:
            print(str(e))

    def on_click5(self):
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
            print(app.InstalledProductName, file=open("InstalledApplications.txt", "a"))

        self.labl7.setText('Lägg till ett program manuellt:')
        self.labl7.adjustSize()
        self.line3.move(70, 240)
        self.line3.resize(100, 65)
        self.line3.adjustSize()
        self.line2.resize(0,0)
        print(self.line3.text(), file=open("InstalledApplications.txt", "a"))
        os.startfile('InstalledApplications.txt')

    def approve(self):
        if self.line2.text() == "Steam":
            os.getcwd()
            os.chdir('D:/Steam')
            #print(os.getcwd())
            os.startfile("Steam.exe")

        if self.line2.text() == "Origin":
            os.getcwd()
            os.chdir('D:/Origin')
            #print(os.getcwd())
            os.startfile("Origin.exe")

        if self.line2.text() == "Spotify":
            os.getcwd()
            os.chdir('C:/Users')
            #print(os.getcwd())
            os.chdir('C:/Users/Edvin')
            os.chdir('C:/Users/Edvin/AppData')
            os.chdir('C:/Users/Edvin/AppData/Roaming')
            os.chdir('C:/Users/Edvin/AppData/Roaming/Spotify')
            os.startfile('Spotify.exe')

        if self.line2.text() == "OneDrive":
            os.getcwd()
            os.chdir('C:/Users')
            #print(os.getcwd())
            os.chdir('C:/Users/Edvin')
            os.chdir('C:/Users/Edvin/AppData')
            os.chdir('C:/Users/Edvin/AppData/Local')
            os.chdir('C:/Users/Edvin/AppData/Local/Microsoft')
            os.chdir('C:/Users/Edvin/AppData/Local/Microsoft/OneDrive')
            os.startfile('OneDrive.exe')

        else:
            try:
                os.startfile(self.line2.text())
            except Exception as e:
                print(str(e))

if __name__ == '__main__':
    cleancache()
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())