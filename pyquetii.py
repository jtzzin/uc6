import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
# função com a descrição

def greet():
    label.setText("Olá, mundo!") # atualiza o botão ao ser chamado
    

# inicia o PyQt   
app = QApplication(sys.argv)

# Janela principal
window = QWidget()
window.setWindowTitle("Hello World App")

# layout vertifcal e organiza os Widgets de forma sequencial
layout = QVBoxLayout()

# widgets

# rotulo vazio
label = QLabel("")
layout.addWidget(label)

# botão que chama a função greet
button = QPushButton("Clique aqui")
button.clicked.connect(greet)
layout.addWidget(button)

# configura o layout da janela
window.setLayout(layout)

# exibe a janela
window.show()

# executa o loop da aplicação, esperando o user iniciar 
sys.exit(app.exec_())