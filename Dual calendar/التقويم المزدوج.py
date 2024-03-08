from PyQt6 import QtWidgets as qt
from PyQt6 import QtGui as qt1
from PyQt6 import QtCore as qt2
import الميلادي
import الهجري
class main (qt.QMainWindow):
    def __init__(self):
        super().__init__()
        self.showFullScreen
        self.setWindowTitle("التقويم المزدوج")
        self.إظهار=qt.QLabel("إختيار نوع التحويل")
        self.التواريخ=qt.QComboBox()
        self.التواريخ.setAccessibleName("إختيار نوع التحويل")
        self.التواريخ.addItems(["من ميلادي الى هجري","من هجري الى ميلادي"])
        self.إختيار=qt.QPushButton("إختيار")
        self.إختيار.setDefault(True)
        self.إختيار.clicked.connect(self.ch)
        l=qt.QVBoxLayout()        
        l.addWidget(self.إظهار)
        l.addWidget(self.التواريخ)
        l.addWidget(self.إختيار)
        w=qt.QWidget()
        w.setLayout(l)
        self.setCentralWidget(w)        
    def ch(self):
        الإختيار=self.التواريخ.currentIndex()
        if الإختيار ==0:
            الهجري.dialog(self).exec()
        if الإختيار ==1:
            الميلادي.dialog(self).exec()
app=qt.QApplication([])
app.setStyle('fusion')
w=main()
w.show()
app.exec()