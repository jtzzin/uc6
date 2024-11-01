import sys
from PyQt5.QTWidgets import QApplication, QWidget, Qlabel, QPushButton, QVBoxLayout

def greet():
    label.setText("Olá, mundo!")
    
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Hello World App")

layout = QVBoxLayout()

label = Qlabel("")
layout.addWidget(label)

button = QPushButton("Clique aqui")
button.clicked.connect(greet)
layout.addWidget(button)
window.setLayout(layout)

window.show()

sys.exit(app.exec_())
