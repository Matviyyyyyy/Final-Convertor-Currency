
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from forex_python.converter import CurrencyRates
from  PyQt5.QtGui import QPixmap

c = CurrencyRates()
app = QApplication([])
win_card = QWidget()
win_card.setWindowTitle('pon') 
win_card.resize(400, 400)

app.setStyleSheet("""
        QWidget {
            background: #061c3b;
            border-radius: 11px;    

        }
        
        QPushButton{
            background: #8f7efc;
            color: #ffffff;
            border-radius: 11px;
            min-width: 6em;    
            min-height: 2em;
            font-family: Arial;
            font: bold 18px;      
        }
        
        QLineEdit{
            background-color: ;
            max-width: 20em;
            max-height: 7em;
            font-family: Arial;
            font: bold 18px;
            border-color: beige;
            color:#ff0505;
            
        }

        QLabel{
            color:#ff0505;
            font-family: Arial;
            font: bold 18px;

        }

"""
)

im = QPixmap("D:\\Projects\\unnamed (8).png")
im = im.scaledToWidth(250)
im = im.scaledToHeight(250) 
label = QLabel()
label.setPixmap(im) 

oneline_edit = QLineEdit()
twoline_edit = QLineEdit()
threeline_edit = QLineEdit()
threeline_edit.setReadOnly(True) 
fiveline_edit = QLineEdit()

l1 = QLabel("From which currency:")
l2 = QLabel("In what currency:")
l4 = QLabel("Count of currency:")
l3 = QLabel("Result count:")


button = QPushButton("Convert")

ver_line = QVBoxLayout()
H1 = QHBoxLayout()
H2 = QHBoxLayout()
H3 = QHBoxLayout()
H4 = QHBoxLayout()
H5 = QHBoxLayout()

ver_line.addLayout(H1)
ver_line.addLayout(H2)
ver_line.addLayout(H3)
ver_line.addLayout(H4)
ver_line.addLayout(H5)

H1.addStretch(1)
H1.addWidget(label)
H1.addStretch(1)

H2.addWidget(l1)
H2.addWidget(oneline_edit)

H3.addWidget(l2)
H3.addWidget(twoline_edit)

H4.addWidget(l4)
H4.addWidget(fiveline_edit)

H5.addWidget(l3)
H5.addWidget(threeline_edit)

ver_line.addWidget(button)

def convert():
    withsomething = oneline_edit.text()
    getrate = twoline_edit.text()
    count = int(fiveline_edit.text())
    rate = c.get_rate(withsomething, getrate)
    result = (rate * count)
    threeline_edit.setText(str(result))

button.clicked.connect(convert)
win_card.setLayout(ver_line)
win_card.show()
app.exec_()