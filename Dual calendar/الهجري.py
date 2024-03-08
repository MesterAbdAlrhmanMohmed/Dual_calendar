from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from hijridate import Hijri, Gregorian
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("التحويل الى هجري")
        self.إظهار=qt.QLabel("أكتب التاريخ الميلادي")
        self.الكتابة=qt.QLineEdit()
        self.الكتابة.setAccessibleName("أكتب التاريخ الميلادي")
        self.التحويل=qt.QPushButton("التحويل")
        self.التحويل.setDefault(True)
        self.التحويل.clicked.connect(self.co)
        self.إظهار1=qt.QLabel("التاريخ الهجري هو")
        self.النتيجة=qt.QLineEdit()
        self.النتيجة.setReadOnly(True)
        self.النتيجة.setAccessibleName("التاريخ الهجري هو")
        self.حول=qt.QPushButton("حول التحويل")
        self.حول.setDefault(True)
        self.حول.clicked.connect(self.ab)
        l=qt.QVBoxLayout(self)                            
        l.addWidget(self.إظهار)
        l.addWidget(self.الكتابة)
        l.addWidget(self.التحويل)
        l.addWidget(self.إظهار1)
        l.addWidget(self.النتيجة)
        l.addWidget(self.حول)
    def co(self):
        try:
            الكتابة=self.الكتابة.text()
            العام, الشهر, اليوم=الكتابة.split(",")
            h=Gregorian(int(العام), int(الشهر), int(اليوم)).to_hijri()
            self.النتيجة.setText(str(h))
            self.النتيجة.setFocus()        
        except:
            qt.QMessageBox.warning(self,"تنبيه","خطأ في الحصول على التاريخ, يرجى كتابة التاريخ بشكلً صحيح, أو التأكد من الإتصال بالإنترنت, ثم إعادة المحاولة")
    def ab(self):
        qt.QMessageBox.information(self,"تنبيه","لكتابة التاريخ بشكلً صحيح, قم بكتابة العام, ثم الشهر, ثم اليوم, وقم بالفصل بينهم بالفاصلة الإنجليزية")