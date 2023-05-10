import sys
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMainWindow, QGridLayout

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejercicio1 Seccion Práctica Prueba Individual')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout_principal = QVBoxLayout()
        self.central_widget.setLayout(self.layout_principal)

        # Layout superior
        self.layout_superior = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_superior)
        self.label_nombre_usuario = QLabel('Nombre de usuario')
        self.layout_superior.addWidget(self.label_nombre_usuario)
        self.boton_ok = QPushButton('OK')
        self.layout_superior.addWidget(self.boton_ok, alignment= QtCore.Qt.AlignmentFlag.AlignRight)

        # Layout central
        self.layout_central = QHBoxLayout()
        self.layout_principal.addLayout(self.layout_central)

        # Layout izquierdo
        self.layout_izquierdo = QVBoxLayout()
        self.layout_central.addLayout(self.layout_izquierdo)
        self.label_imagen = QLabel('Imagen')
        self.layout_izquierdo.addWidget(self.label_imagen)
        self.label_texto = QLabel('Texto')
        self.layout_izquierdo.addWidget(self.label_texto)

        # Layout derecho
        self.layout_derecho = QGridLayout()
        self.layout_central.addLayout(self.layout_derecho)
        self.label_atributo_1 = QLabel('Atributo 1:')
        self.layout_derecho.addWidget(self.label_atributo_1, 0, 0)
        self.label_valor_1 = QLabel('Valor 1')
        self.layout_derecho.addWidget(self.label_valor_1, 0, 1)
        self.label_atributo_2 = QLabel('Atributo 2:')
        self.layout_derecho.addWidget(self.label_atributo_2, 1, 0)
        self.label_valor_2 = QLabel('Valor 2')
        self.layout_derecho.addWidget(self.label_valor_2, 1, 1)
        self.label_atributo_3 = QLabel('Atributo 3:')
        self.layout_derecho.addWidget(self.label_atributo_3, 2, 0)
        self.label_valor_3 = QLabel('Valor 3')
        self.layout_derecho.addWidget(self.label_valor_3, 2, 1)
        self.label_atributo_4 = QLabel('Atributo 4:')
        self.layout_derecho.addWidget(self.label_atributo_4, 3, 0)
        self.label_valor_4 = QLabel('Valor 4')
        self.layout_derecho.addWidget(self.label_valor_4, 3, 1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = VentanaPrincipal()
    main_window.show()
    sys.exit(app.exec())
