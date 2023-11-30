from urllib.request import urlopen
from PyQt5.QtWidgets import QDialog, QMainWindow
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
from pyzbar.pyzbar import decode
import sys
from hello import Ui_ISBN
from PyQt5.QtGui import  QPixmap, QImage

class Ui_main(QMainWindow):

    # function that will be called on pressing submit button
    def message(self):
        # function called to run the main program
        self.isbn = self.lineEdit.text()
        self.cal()

    # function that will be called on pressing scan button
    def scanner(self):
        # function called to run scanner
        self.call()

    # function that will be called on pressing clear button
    def clear(self):
        # clearing the dialog box
        self.isbn = ""
        self.lineEdit.clear()

    def open_window(self):

        # creating second window
        self.window = QtWidgets.QMainWindow()

        # calling the call of second window
        self.jug = Ui_ISBN()

        # running the main code of second window
        self.jug.setupUi(self.window)

        # displaying secound window
        self.window.show()

    # setting up main window
    def setupUi(self, MainWindow):
        # setting up the main window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # label 1
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 50, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        # label 2
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(420, 110, 55, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        # label 3
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(210, 60, 501, 31))
        self.lineEdit.setObjectName("lineEdit")

        # push button 1 for submit button
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(740, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.clicked.connect(self.message)
        self.pushButton.setObjectName("pushButton")

        # push button 2 for scan button
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(410, 170, 93, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.scanner)

        # push button for clear button
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(850, 60, 93, 31))
        self.pushButton_3.clicked.connect(self.clear)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        # naming window
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        #setting texts in labels and push-buttons
        self.label.setText(_translate("MainWindow", "ISBN NUMBER :"))
        self.label_2.setText(_translate("MainWindow", "OR"))
        self.label_3.setText(_translate("MainWindow", "SCAN BAR-CODE OF THE BOOK :"))
        self.pushButton.setText(_translate("MainWindow", "SUBMIT"))
        self.pushButton_2.setText(_translate("MainWindow", "SCAN"))
        self.pushButton_3.setText(_translate("MainWindow", "CLEAR"))

    def BarcodeReader(self, image):
        isbn = []
        self.isbn = isbn
        gray_img = cv2.cvtColor(image, 0)
        detectedBarcodes = decode(gray_img)
        if not detectedBarcodes:
            print("Barcode Not Detected or your barcode is blank/corrupted!")
        else:
            for barcode in detectedBarcodes:
                (x, y, w, h) = barcode.rect
                cv2.rectangle(image, (x - 10, y - 10),
                              (x + w + 10, y + h + 10),
                              (255, 0, 0), 2)
                if barcode.data != "":
                    # converting isbn number from string to list
                    self.isbn = barcode.data.decode('UTF-8')
                    isbn_convert = map(int, self.isbn)
                    self.isbn_list = list(isbn_convert)
                    x = 'q'
                    return x

        cv2.imshow("Image", image)
        cv2.waitKey(10)
        cv2.destroyAllWindows()

    def call(self):
        if __name__ == "__main__":
            cap = cv2.VideoCapture(0)
            while True:
                ret, frame = cap.read()
                self.BarcodeReader(frame)
                x = self.BarcodeReader(frame)
                cv2.imshow("Image", frame)
                if x == 'q':
                    cv2.destroyAllWindows()
                    self.cal()
                    break

    def cal(self):
        n = []
        n = self.isbn
        length = len(n)

        if length == 10:
            sum = int(0)
            a = int(10)
            b = int(0)
            i = 1
            while i <= 10:
                c = n[b]
                c = int(c)
                sum = sum + (c * a)
                a = a - 1
                b = b + 1
                i = i + 1
            if sum % 11 == 0:
                self.valid = "Valid 10-digit ISBN."
                self.source()
            else:
                self.valid = "Invalid 10-digit ISBN."
                self.source()

        elif length == 13:
            sum = 0
            sum = int(sum)
            a = 0
            a = int(a)
            x = n[12]
            x = int(x)
            i = int(1)
            while i <= 12:
                b = n[a]
                b = int(b)
                if a % 2 == 0:
                    sum = sum + (b * 1)
                else:
                    sum = sum + (b * 3)
                a = a + 1
                i = i + 1
            c = sum % 10
            if c == 0:
                if x == c:
                    self.valid = "Valid 13-digit ISBN."
                    self.source()
                else:
                    self.valid = "Invalid 13-digit ISBN."
                    self.source()
            else:
                if x == (10 - c):
                    self.valid = "Valid 13-digit ISBN."
                    self.source()
                else:
                    self.valid = "Invalid 13-digit ISBN."
                    self.source()

        else:
            self.valid = "Invalid 13-digit ISBN."
            self.source()

    def source(self):
        n = []
        n = self.isbn
        self.open_window()
        website1 = "https://www.bookfinder.com/search/?author=&title=&lang=en&new_used=*&destination=in&currency=INR&binding=*&isbn="
        website2 = "&keywords=&minprice=&maxprice=&publisher=&min_year=&max_year=&mode=advanced&st=sr&ac=qr"
        a = ''.join(str(e) for e in n)
        web = website1 + a + website2
        html = urlopen(web)
        bs = BeautifulSoup(html.read(), 'lxml')

        self.jug.label.setText(self.valid)

        nameList = bs.findAll('span', {'itemprop': 'name'})
        for name in nameList:
            self.name = name.get_text()
            self.jug.label_13.setText(self.name)

        nameList1 = bs.findAll('span', {'itemprop': 'author'})
        for name in nameList1:
            self.author = name.get_text()
            self.jug.label_10.setText(self.author)

        nameList2 = bs.findAll('span', {'itemprop': 'publisher'})
        for name in nameList2:
            self.publisher = name.get_text()
            self.jug.label_11.setText(self.publisher)

        nameList3 = bs.findAll('span', {'itemprop': 'inLanguage'})
        for name in nameList3:
            self.language = name.get_text()
            self.jug.label_12.setText(self.language)

        nameList4 = bs.findAll('div', {'itemprop': 'description'})
        for name in nameList4:
            self.description = name.get_text()
            self.jug.label_7.setText(self.description)

        nameList5 = bs.findAll('tr', {'valign': 'top', 'class': 'results-table-first-LogoRow has-data'})
        for name in nameList5:
            self.seller = name.get_text()
            self.jug.label_9.setText(self.seller)

        images = bs.findAll('img', {'id': 'coverImage'})
        for image in images:
            self.path = image['src']
            try:
                with urlopen(self.path) as response:
                    image_data = response.read()
                    image = QImage()
                    image.loadFromData(image_data)
                    self.jug.label_14.setPixmap(QPixmap(image))
            except Exception as e:
                print(f"Error loading image from {self.path}: {e}")

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

#initialize app
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    eb = MyForm()
    eb.show()
    sys.exit(app.exec_())

