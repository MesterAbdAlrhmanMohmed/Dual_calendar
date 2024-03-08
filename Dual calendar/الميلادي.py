from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
from hijridate import Hijri, Gregorian
class dialog(qt.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("التحويل الى ميلادي")
        self.إظهار=qt.QLabel("أكتب التاريخ الهجري")
        self.الكتابة=qt.QLineEdit()
        self.الكتابة.setAccessibleName("أكتب التاريخ الهجري")
        self.التحويل=qt.QPushButton("التحويل")
        self.التحويل.setDefault(True)
        self.التحويل.clicked.connect(self.co)
        self.إظهار1=qt.QLabel("التاريخ الميلادي هو")
        self.النتيجة=qt.QLineEdit()
        self.النتيجة.setReadOnly(True)
        self.النتيجة.setAccessibleName("التاريخ الميلادي هو")
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
            g=Hijri(int(العام), int(الشهر), int(اليوم)).to_gregorian()
            self.النتيجة.setText(str(g))
            self.النتيجة.setFocus()
        except:
            qt.QMessageBox.warning(self,"تنبيه","خطأ في الحصول على التاريخ, يرجى كتابة التاريخ بشكلً صحيح, أو التأكد من الإتصال بالإنترنت, ثم إعادة المحاولة")
    def ab(self):
        qt.QMessageBox.information(self,"تنبيه","لكتابة التاريخ بشكلً صحيح, قم بكتابة العام, ثم الشهر, ثم اليوم, وقم بالفصل بينهم بالفاصلة الإنجليزية")