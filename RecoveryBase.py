# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Nombre:       RecoveryBase.py
# Autor:      	Cristian Cala Sierra 
# Creado:       31 de Julio del 2020
# Modificado:   31 de Julio del 2020
# Copyright:    (c) Cristian Cala
# ----------------------------------------------------------------------------
__version__ = "1.0"

import sys, time
import pymysql
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import QRect, Qt, QPropertyAnimation, QAbstractAnimation
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtWidgets import (QApplication, QMainWindow, QDialog, QFrame, QLabel, QPushButton
,QGraphicsDropShadowEffect,QVBoxLayout, QGraphicsBlurEffect,QTableWidgetItem,QWidget, QAbstractItemView,
QTableWidget, QMessageBox, QLineEdit, QAbstractItemView, QTextEdit)


class hoverButton(QPushButton):
    def __init__(self, parent=None):
        QPushButton.__init__(self, parent)
        
        self.setMouseTracking(True)

        self.posicionX = int
        self.posicionY = int

    def enterEvent(self, event):
        self.posicionX = self.pos().x()
        self.posicionY = self.pos().y()
        
        self.animacionCursor = QPropertyAnimation(self, b"geometry")
        self.animacionCursor.setDuration(100)
        self.animacionCursor.setEndValue(QRect(self.posicionX+10, self.posicionY+5, 125, 50))
        self.animacionCursor.start(QAbstractAnimation.DeleteWhenStopped)
        

    def leaveEvent(self, event):
        self.animacionNoCursor = QPropertyAnimation(self, b"geometry")
        self.animacionNoCursor.setDuration(100)
        self.animacionNoCursor.setEndValue(QRect(self.posicionX, self.posicionY, 125, 50))
        self.animacionNoCursor.start(QAbstractAnimation.DeleteWhenStopped)

class Interface(QDialog):
	def __init__(self):
		super(Interface, self).__init__()
		self.setWindowTitle("RecoveryBase")
		self.setWindowIcon(QIcon("Recovery.png"))
		self.setFixedSize(750, 630)
		self.setStyleSheet("QDialog{\n"
							"background-image: url('Circuits.jpg');\n"
							"}\n"
							"")

		self.initUi()

	def initUi(self):


		estiloFrame = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgba(1,117,140,0.8);\n"
				"border-radius: 10px;\n"
				"}")

		estiloCircular = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgba(0,247,255,1);\n"
				"background-image: url('Recovery.png');"
				"border-radius: 75px;\n"
				"}")

		estiloBotonPrincipal = ("QPushButton{\n"
						"color: black;"
						"background-color: rgba(1,167,200,0.8);"
						"border-radius: 20px;"
						"}\n"
						"QPushButton:hover{\n"
						"background-color:#00F7FF;\n"
						"color:rgb(255, 255, 255);\n"
						"}")

		estiloLabel = ("QLabel{\n"
						"color: white;\n"
						"background-color: rgba(1,117,140,0.1);\n"
						"}")

		estiloFonts1 = (QtGui.QFont("Roboto", 13, QtGui.QFont.Bold))

		self.framePrincipal = QFrame(self)
		self.framePrincipal.setStyleSheet(estiloFrame)
		self.framePrincipal.setGeometry(QRect(20,20,300,350))
		self.framePrincipal.move(230,180)

		self.frameCircular = QFrame(self)
		self.frameCircular.setStyleSheet(estiloCircular)
		self.frameCircular.setGeometry(QRect(20,20,150,150))
		self.sombra1 = QGraphicsDropShadowEffect()
		self.sombra1.setBlurRadius(23)
		self.frameCircular.setGraphicsEffect(self.sombra1)
		self.frameCircular.move(305,100)

		self.labelPrincipal = QLabel(self.framePrincipal)
		self.labelPrincipal.setStyleSheet(estiloLabel)
		self.labelPrincipal.setGeometry(QRect(20,20,300,50))
		self.labelPrincipal.setText("Programa para gestión de datos\n de Recoveryloid")
		self.labelPrincipal.setAlignment(Qt.AlignCenter)
		self.labelPrincipal.setFont(estiloFonts1)
		self.labelPrincipal.move(0,150)

		self.labelEncabezado = QLabel(self.framePrincipal)
		self.labelEncabezado.setStyleSheet(estiloLabel)
		self.labelEncabezado.setGeometry(QRect(20,20,120,50))
		self.labelEncabezado.setText("RecoveryBase")
		self.labelEncabezado.setFont(estiloFonts1)
		self.labelEncabezado.move(90,80)

		self.botonPrincipal = QPushButton(self.framePrincipal)
		self.botonPrincipal.setStyleSheet(estiloBotonPrincipal)
		self.botonPrincipal.setGeometry(QRect(80,230,130,50))
		self.botonPrincipal.setIcon(QIcon('Next.svg'))
		self.botonPrincipal.setFont(estiloFonts1)
		self.botonPrincipal.setText("Siguiente")
		self.sombra2 = QGraphicsDropShadowEffect()
		self.sombra2.setBlurRadius(23)
		self.botonPrincipal.setGraphicsEffect(self.sombra2)


		# Eventos de botones###############################################################################

		self.botonPrincipal.clicked.connect(self.open)

		# Eventos de funciones###############################################################################

	def open(self):
		self.ventana = segundaVentana()
		self.ventana.show()
		self.close()

class segundaVentana(QMainWindow):
	def __init__(self):
		super(segundaVentana, self).__init__()
		self.resize(750, 630)
		self.setMaximumWidth(750)
		self.setMaximumHeight(630)
		self.setWindowIcon(QIcon("Recovery.png"))
		self.setWindowTitle("RecoveryBase")
		self.setStyleSheet("QMainWindow{\n"
							"background-color: #F3F3F3;"
							"}\n"
							"")

		self.initUi()

	def initUi(self):

		estiloFontTable = (QtGui.QFont("Roboto", 11, QtGui.QFont.Light))
		estiloFonts2 = (QtGui.QFont("Roboto", 15, QtGui.QFont.Bold))
		estiloFontBotones = (QtGui.QFont("Roboto", 11, QtGui.QFont.Bold))


		estiloFrameArriba = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgb(3, 169, 244);\n"
				"}")
		estiloFrameIzquierda = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: white;\n"
				"border: 1px solihoverButton;\n"
				"}")

		estiloLabelRecovery = ("QLabel{\n"
				"color:white;\n"
				"background-color: rgb(3, 169, 244);\n"
				"}")

		estiloQtable = ("QTableWidget::item{\n"
									"color: black;\n"
									"border-radius: 5px;"
									"}\n"
									"QTableWidget::item:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#000000;\n"
									"}\n"
									"QTableWidget{\n"
									"background-color:white;\n"
									"border-radius:5px;\n"
									"border:1px solid Gainsboro;"
									"color:white;\n"
									"}\n"
									"QHeaderView::section{\n"
									"font-size: 11pt;"
									"background-color:black;\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000;\n"
									"border-radius: 5px;"
									"}\n"
									"QHeaderView::section:hover{\n"
									"background-color: rgb(0, 170, 255);\n"
									"color:#ffffff;\n"
									"border: 1px solid #000000\n"									
									"}\n"
									"QHeaderView::section:checked{\n"
									"background-color: rgb(0, 170, 255);\n"
									"}")

		estiloBotones = ("QPushButton{\n"
						"color: black;"
						"background-color: rgba(255,255,255,0.8);"
						"border-radius: 1px;"
						"border: 1px solid Gainsboro;"
						"}\n"
						"QPushButton:hover{\n"
						"background-color: #F2F2F2;\n"
						"color:#35B6F2;\n"
						"}")

		estiloBotonConfig = ("QPushButton{\n"
						"color: black;"
						"background-color: rgb(3, 169, 244);"
						"border-radius: 1px;"
						"}\n"
						"QPushButton:hover{\n"
						"background-color: #F2F2F2;\n"
						"border-radius: 2px;"
						"color:#35B6F2;\n"
						"}")

		self.frameArriba = QFrame(self)
		self.frameArriba.setGeometry(QRect(0,0,750,130))
		self.frameArriba.setStyleSheet(estiloFrameArriba)
		self.sombra2 = QGraphicsDropShadowEffect()
		self.sombra2.setBlurRadius(23)
		self.frameArriba.setGraphicsEffect(self.sombra2)

		self.frameIzquierda = QFrame(self)
		self.frameIzquierda.setGeometry(QRect(0,130,130,630))
		self.frameIzquierda.setStyleSheet(estiloFrameIzquierda)

		self.labelRecovery = QLabel(self.frameArriba)
		self.labelRecovery.setGeometry(QRect(30,10,200,100))
		self.labelRecovery.setText("RecoveryBase")
		self.labelRecovery.setFont(estiloFonts2)
		self.labelRecovery.setStyleSheet(estiloLabelRecovery)

		self.labelArriba = QLabel(self.frameArriba)
		self.labelArriba.setGeometry(QRect(350,10,200,100))
		self.labelArriba.setText("Tabla de Usuarios")
		self.labelArriba.setFont(estiloFonts2)
		self.labelArriba.setStyleSheet(estiloLabelRecovery)


		self.botonEditar = hoverButton(self.frameIzquierda)
		self.botonEditar.setStyleSheet(estiloBotones)
		self.botonEditar.setGeometry(QRect(5,0,125,50))
		self.botonEditar.setText("Editar")
		self.botonEditar.setAutoDefault(False)
		self.botonEditar.setFont(estiloFontBotones)

		self.botonRecargar = hoverButton(self.frameIzquierda)
		self.botonRecargar.setStyleSheet(estiloBotones)
		self.botonRecargar.setGeometry(QRect(5,50,125,50))
		self.botonRecargar.setIcon(QIcon('Charger.svg'))
		self.botonRecargar.setText("Recargar")
		self.botonRecargar.setAutoDefault(False)
		self.botonRecargar.setFont(estiloFontBotones)

		self.botonAgregar = hoverButton(self.frameIzquierda)
		self.botonAgregar.setStyleSheet(estiloBotones)
		self.botonAgregar.setGeometry(QRect(5,100,125,50))
		self.botonAgregar.setText("Agregar Usuario")
		self.botonAgregar.setAutoDefault(False)
		self.botonAgregar.setFont(estiloFontBotones)

		self.botonEliminar = hoverButton(self.frameIzquierda)
		self.botonEliminar.setStyleSheet(estiloBotones)
		self.botonEliminar.setGeometry(QRect(5,150,125,50))
		self.botonEliminar.setText("Eliminar")
		self.botonEliminar.setAutoDefault(False)
		self.botonEliminar.setFont(estiloFontBotones)

		self.botonCancelar = hoverButton(self.frameIzquierda)
		self.botonCancelar.setStyleSheet(estiloBotones)
		self.botonCancelar.setGeometry(QRect(5,200,125,50))
		self.botonCancelar.setText("Cancelar")
		self.botonCancelar.setAutoDefault(False)
		self.botonCancelar.setFont(estiloFontBotones)

		# self.botonConfiguracion = QPushButton(self.frameArriba)
		# self.botonConfiguracion.setStyleSheet(estiloBotonConfig)
		# self.botonConfiguracion.setGeometry(690,20,50,30)
		# self.botonConfiguracion.setIcon(QIcon('settings.svg'))


		#QTableWidget ==========================================================================================      		
		nombreColumnas = ("Id", "Usuario", "Cédula", "Fecha",
		 "Equipo")
		self.tablaQWidget = QTableWidget(self)
		self.tablaQWidget.setToolTip("Clickea una tabla UwU")
		self.tablaQWidget.setFont(estiloFontTable)
		self.tablaQWidget.setGeometry(QRect(160,150,560,450))
		self.tablaQWidget.setStyleSheet(estiloQtable)
		self.tablaQWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tablaQWidget.setDragDropOverwriteMode(False)
		self.tablaQWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
		self.tablaQWidget.setSelectionMode(QAbstractItemView.SingleSelection)
		self.tablaQWidget.setTextElideMode(Qt.ElideRight)
		self.tablaQWidget.setWordWrap(False)
		self.tablaQWidget.setSortingEnabled(False)
		self.tablaQWidget.setColumnCount(5)
		self.tablaQWidget.setRowCount(0)
		self.tablaQWidget.horizontalHeader().setDefaultAlignment(Qt.AlignHCenter|Qt.AlignVCenter|
														  Qt.AlignCenter)
		self.tablaQWidget.horizontalHeader().setHighlightSections(False)
		self.tablaQWidget.horizontalHeader().setStretchLastSection(True)
		self.tablaQWidget.verticalHeader().setVisible(False)
		self.tablaQWidget.setAlternatingRowColors(False)
		self.tablaQWidget.verticalHeader().setDefaultSectionSize(20)
		self.tablaQWidget.setHorizontalHeaderLabels(nombreColumnas)
		sombra3 = QGraphicsBlurEffect()
		sombra3.setBlurRadius(1)
		self.tablaQWidget.setGraphicsEffect(sombra3)

		for indice, ancho in enumerate((110, 110, 110, 110, 110), start=0):
			self.tablaQWidget.setColumnWidth(indice, ancho)


		# Eventos de botones###############################################################################

		self.botonAgregar.clicked.connect(self.ventanaAbrir)
		self.botonEliminar.clicked.connect(self.eliminarUsuario)
		self.botonRecargar.clicked.connect(self.database)
		self.botonCancelar.clicked.connect(self.salir)
		self.botonEditar.clicked.connect(self.editarUsuario)

	def database(self):
		try:
			conn = pymysql.connect(
				host = 'nombre del host',
				user = 'nombre de usuario',
				password ='contraseña del host',
				db = 'nombre de la base de datos',
				)
			cursor = conn.cursor()

		except Exception as e:
			print("Error al conectar", e)
			QMessageBox.information(self, "Conexión", "Fallo al conectar, revise su conexión a internet", QMessageBox.Ok)

		try:

			cursor.execute("SELECT ID, NOMBRE, CEDULA, FECHA, EQUIPO FROM recoverytable")


			datosDevueltos = cursor.fetchall()
			self.tablaQWidget.clearContents()
			self.tablaQWidget.setRowCount(0)

			row = 0
			for datos in datosDevueltos:
				self.tablaQWidget.setRowCount(row + 1)
						
				idDato = QTableWidgetItem(str(datos[0]))
				cdDato = QTableWidgetItem(str(datos[2]))
				idDato.setTextAlignment(Qt.AlignCenter)

				self.tablaQWidget.setItem(row, 0, idDato)
				self.tablaQWidget.setItem(row, 1, QTableWidgetItem(datos[1]))
				self.tablaQWidget.setItem(row, 2, cdDato)
				self.tablaQWidget.setItem(row, 3, QTableWidgetItem(datos[3]))
				self.tablaQWidget.setItem(row, 4, QTableWidgetItem(datos[4]))
					
				row +=1
		except Exception as e:
			print("Error al leer en tabla", e)
			QMessageBox.information(self, "Conexión", "Falla al leer la base de datos", QMessageBox.Ok)



	def editarUsuario(self, celda):
		celda = self.tablaQWidget.selectedItems()

		if celda:
			indice = celda[0].row()
			dato = [self.tablaQWidget.item(indice,i).text()for i in range(4)]
			dato_buscar = dato[2]
			print("DATO A BUSCAR EL DATO ES:", dato_buscar)

			if dato_buscar:
				sql = "SELECT * FROM recoverytable WHERE CEDULA LIKE %s", (dato_buscar,)
			else:
				print("NO")

			try:
				conexion = pymysql.connect(
				host = 'nombre del host',
				user = 'nombre de usuario',
				password ='contraseña del host',
				db = 'nombre de la base de datos',
				)

				cursor = conexion.cursor()
			except Exception as e:
				print("Error al conectar", e)
				QMessageBox.information(self, "Conexión", "Error al conectar, revise su conexión a internet", QMessageBox.Ok)


			try:
				cursor.execute(sql[0],sql[1])
				datosdevueltos = cursor.fetchall()
				for dato in datosdevueltos:
					indice = dato[0]

				ventanaEditar(dato,self).exec_()
				conexion.close()
			except Exception as e:
				print("A1:",e)

		else:
			print("Error de selección")
			QMessageBox.information(self, "Selección", "Enserio??, no has seleccionado nada sabias?", QMessageBox.Ok)



	def eliminarUsuario(self):

		msg = QMessageBox()
		msg.setText("¿Está seguro de querer eliminar este usuario?")
		msg.setIcon(QMessageBox.Question)
		msg.setWindowTitle("Eliminar Usuario")
		msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		button_si = msg.button(QMessageBox.Yes)
		button_si.setText("Si")
		button_si.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;\n"
		"}")

		button_no = msg.button(QMessageBox.No)
		button_no.setStyleSheet("QPushButton:hover{background:rgb(0, 170, 255);}\n"
		"QPushButton{background:#343a40;}")

		msg.setStyleSheet("\n"
			"color:#ffffff;\n"
			"font-size:12px;\n"
			"background-color:#12191D;")

		if (msg.exec_() == QMessageBox.Yes):

			try:
				conn = pymysql.connect(
				host = 'nombre del host',
				user = 'nombre de usuario',
				password ='contraseña del host',
				db = 'nombre de la base de datos',
				)
				cursor = conn.cursor()

			except Exception as e:
				print("Error al conectar", e)
				QMessageBox.information(self, "Conexión", "No se pudo conectar, revise su conexión a internet", QMessageBox.Ok)			

			try:

				self.tablaQWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
				ID = self.tablaQWidget.selectedIndexes()[0].data()
					
				query = 'DELETE  FROM recoverytable WHERE ID =%s'
				cursor.execute(query, (ID,))
				conn.commit()

				self.database()

				QMessageBox.information(self, "Eliminar", "¡Borrado exitoso!")

			except Exception as e:
				print("Error al eliminar", e)


	def ventanaAbrir(self):
		self.ventana = terceraVentana()
		self.ventana.show()
		self.close()


	def salir(self):
		cerrar = QMessageBox(self)
		cerrar.setWindowTitle("¿Salir de RecoveryBase?")
		cerrar.setIcon(QMessageBox.Question)
		cerrar.setText("¿Estás seguro que desea cerrar esta ventana?")
		botonSalir = cerrar.addButton("Salir", QMessageBox.YesRole)
		botonCancelar = cerrar.addButton("Cancelar", QMessageBox.NoRole)
            
		cerrar.exec_()
            
		if cerrar.clickedButton() == botonSalir:
			self.close()
		else:
			pass

class terceraVentana(QDialog):
	def __init__(self):
		super(terceraVentana, self).__init__()
		self.resize(750, 630)
		self.setMaximumWidth(750)
		self.setMaximumHeight(630)
		self.setWindowIcon(QIcon("Recovery.png"))
		self.setWindowTitle("RecoveryBase")
		self.setStyleSheet("QDialog{\n"
							"background-color: #F3F3F3;"
							"}\n"
							"")

		self.initUi()

	def initUi(self):

		estiloFontBotones2 = (QtGui.QFont("Roboto", 11, QtGui.QFont.Bold))
		estiloFonts2 = (QtGui.QFont("Roboto", 15, QtGui.QFont.Bold))
		estiloFontLines = (QtGui.QFont("Roboto", 11, QtGui.QFont.Bold))
		estiloFontLinesEdit = (QtGui.QFont("Roboto", 11, QtGui.QFont.Light))

		estiloFrameArriba = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgb(3, 169, 244);\n"
				"}")
		estiloFrameIzquierda = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: white;\n"
				"border: 2px solid Gainsboro;\n"
				"}")

		estiloFrameRayita = ("QFrame{\n"
				"background-color: black;\n"
				"border-radius: 2px;"
				"}")

		estiloLabelRecovery = ("QLabel{\n"
				"color:white;\n"
				"background-color: rgb(3, 169, 244);\n"
				"}")

		estiloQLine = ("QLineEdit{\n"
				"color:black;\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid Gainsboro;\n"
				"border-radius: 4px;\n"
				"}\n"
				"QLineEdit:hover{\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid ;\n"
				"}")

		estiloQText = ("QTextEdit{\n"
				"color:black;\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid Gainsboro;\n"
				"border-radius: 4px;\n"
				"}\n"
				"QTextEdit:hover{\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid ;\n"
				"}")

		estiloLabels = ("QLabel{\n"
				"color:black;\n"
				"background-color: rgb(255, 255, 255);\n"
				"border: none;"
				"}")

		estiloBotones2 = ("QPushButton{\n"
						"color: black;"
						"background-color: rgba(255,255,255,0.8);"
						"border-radius: 1px;"
						"border: 1px solid Gainsboro;"
						"}\n"
						"QPushButton:hover{\n"
						"background-color: #F2F2F2;\n"
						"color:#35B6F2;\n"
						"}")

		self.frameArriba = QFrame(self)
		self.frameArriba.setGeometry(QRect(0,0,750,130))
		self.frameArriba.setStyleSheet(estiloFrameArriba)
		self.sombra2 = QGraphicsDropShadowEffect()
		self.sombra2.setBlurRadius(23)
		self.frameArriba.setGraphicsEffect(self.sombra2)

		self.frameIzquierda = QFrame(self)
		self.frameIzquierda.setGeometry(QRect(0,130,130,630))
		self.frameIzquierda.setStyleSheet(estiloFrameIzquierda)
		
		self.labelRecovery = QLabel(self)
		self.labelRecovery.setGeometry(QRect(30,10,250,100))
		self.labelRecovery.setText("RecoveryBase")
		self.labelRecovery.setFont(estiloFonts2)
		self.labelRecovery.setStyleSheet(estiloLabelRecovery)

		self.labelRecovery = QLabel(self.frameArriba)
		self.labelRecovery.setGeometry(QRect(350,20,300,100))
		self.labelRecovery.setText("Registro de Usuario")
		self.labelRecovery.setFont(estiloFonts2)
		self.labelRecovery.setStyleSheet(estiloLabelRecovery)

		self.botonAceptar = hoverButton(self.frameIzquierda)
		self.botonAceptar.setStyleSheet(estiloBotones2)
		self.botonAceptar.setGeometry(QRect(5,0,125,50))
		self.botonAceptar.setText("Aceptar")
		self.botonAceptar.setAutoDefault(False)
		self.botonAceptar.setFont(estiloFontBotones2)

		self.botonLimpiar = hoverButton(self.frameIzquierda)
		self.botonLimpiar.setStyleSheet(estiloBotones2)
		self.botonLimpiar.setGeometry(QRect(5,50,125,50))
		self.botonLimpiar.setIcon(QIcon('clean.svg'))
		self.botonLimpiar.setText("Limpiar")
		self.botonLimpiar.setAutoDefault(False)
		self.botonLimpiar.setFont(estiloFontBotones2)

		self.botonCancelar = hoverButton(self.frameIzquierda)
		self.botonCancelar.setStyleSheet(estiloBotones2)
		self.botonCancelar.setGeometry(QRect(5,100,125,50))
		self.botonCancelar.setText("Atrás")
		self.botonCancelar.setAutoDefault(False)
		self.botonCancelar.setFont(estiloFontBotones2)


		self.frameCentrado = QLabel(self)
		self.frameCentrado.setGeometry(QRect(200,180,490,430))
		self.frameCentrado.setStyleSheet(estiloFrameIzquierda)
		self.sombra4 = QGraphicsBlurEffect()
		self.sombra4.setBlurRadius(1)
		self.frameCentrado.setGraphicsEffect(self.sombra4)


		self.frameRayita = QLabel(self.frameCentrado)
		self.frameRayita.setGeometry(QRect(45,180,400,2))
		self.frameRayita.setStyleSheet(estiloFrameRayita)

		self.labelNombre = QLabel(self.frameCentrado)
		self.labelNombre.setGeometry(QRect(20,20,100,20))
		self.labelNombre.setText("Nombre")
		self.labelNombre.setFont(estiloFontLines)
		self.labelNombre.setStyleSheet(estiloLabels)

		self.lineNombre = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineNombre.setGeometry(20,60,100,30)
		self.lineNombre.setFont(estiloFontLinesEdit)
		self.lineNombre.setStyleSheet(estiloQLine)
		

		self.labelSegundoNomb = QLabel(self.frameCentrado)
		self.labelSegundoNomb.setGeometry(QRect(130,20,100,20))
		self.labelSegundoNomb.setText("S.Nombre")
		self.labelSegundoNomb.setFont(estiloFontLines)
		self.labelSegundoNomb.setStyleSheet(estiloLabels)

		self.lineSegundoNomb = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineSegundoNomb.setGeometry(130,60,100,30)
		self.lineSegundoNomb.setFont(estiloFontLinesEdit)
		self.lineSegundoNomb.setStyleSheet(estiloQLine)


		self.labelApellido = QLabel(self.frameCentrado)
		self.labelApellido.setGeometry(QRect(240,20,100,20))
		self.labelApellido.setText("Apellido")
		self.labelApellido.setFont(estiloFontLines)
		self.labelApellido.setStyleSheet(estiloLabels)

		self.lineApellido = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineApellido.setGeometry(240,60,100,30)
		self.lineApellido.setFont(estiloFontLinesEdit)
		self.lineApellido.setStyleSheet(estiloQLine)


		self.labelSegundoApellido = QLabel(self.frameCentrado)
		self.labelSegundoApellido.setGeometry(QRect(350,20,100,20))
		self.labelSegundoApellido.setText("S. Apellido")
		self.labelSegundoApellido.setFont(estiloFontLines)
		self.labelSegundoApellido.setStyleSheet(estiloLabels)

		self.lineSegundoApellido = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineSegundoApellido.setGeometry(350,60,100,30)
		self.lineSegundoApellido.setStyleSheet(estiloQLine)
		self.lineSegundoApellido.setFont(estiloFontLinesEdit)

		self.labelCedula = QLabel(self.frameCentrado)
		self.labelCedula.setGeometry(QRect(180,100,100,20))
		self.labelCedula.setText("Cédula")
		self.labelCedula.setFont(estiloFontLines)
		self.labelCedula.setStyleSheet(estiloLabels)

		self.lineCedula = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineCedula.setGeometry(180,130,100,30)
		self.lineCedula.setStyleSheet(estiloQLine)
		self.lineCedula.setMaxLength(8)
		self.lineCedula.setInputMask('99999999')
		self.lineCedula.setFont(estiloFontLinesEdit)


		self.labelEquipo = QLabel(self.frameCentrado)
		self.labelEquipo.setGeometry(QRect(30,220,100,20))
		self.labelEquipo.setText("Equipo")
		self.labelEquipo.setAlignment(Qt.AlignCenter)
		self.labelEquipo.setFont(estiloFontLines)
		self.labelEquipo.setStyleSheet(estiloLabels)

		self.lineEquipo = QTextEdit(self.frameCentrado)
		self.lineEquipo.setGeometry(20,250,130,150)
		self.lineEquipo.setStyleSheet(estiloQText)
		self.lineEquipo.setFont(estiloFontLinesEdit)


		self.labelDescripcion = QLabel(self.frameCentrado)
		self.labelDescripcion.setGeometry(QRect(200,220,100,20))
		self.labelDescripcion.setText("Descripción")
		self.labelDescripcion.setAlignment(Qt.AlignCenter)
		self.labelDescripcion.setFont(estiloFontLines)
		self.labelDescripcion.setStyleSheet(estiloLabels)

		self.lineDescripcion = QTextEdit(self.frameCentrado)
		self.lineDescripcion.setGeometry(190,250,130,150)
		self.lineDescripcion.setStyleSheet(estiloQText)
		self.lineDescripcion.setFont(estiloFontLinesEdit)

		self.labelProblema = QLabel(self.frameCentrado)
		self.labelProblema.setGeometry(QRect(350,220,100,20))
		self.labelProblema.setText("Problema")
		self.labelProblema.setAlignment(Qt.AlignCenter)
		self.labelProblema.setFont(estiloFontLines)
		self.labelProblema.setStyleSheet(estiloLabels)

		self.lineProblema = QTextEdit(self.frameCentrado)
		self.lineProblema.setGeometry(350,250,100,150)
		self.lineProblema.setStyleSheet(estiloQText)
		self.lineProblema.setFont(estiloFontLinesEdit)

		# Eventos de botones###############################################################################

		self.botonCancelar.clicked.connect(self.cerrar)
		self.botonLimpiar.clicked.connect(self.limpiar)
		self.botonAceptar.clicked.connect(self.insertarUsuario)


		# Función para registrar usuarios

	def insertarUsuario(self):
		nombre = self.lineNombre.text()
		nombre2 = self.lineSegundoNomb.text()
		apellido = self.lineApellido.text()
		apellido2 = self.lineSegundoApellido.text()
		cedula = self.lineCedula.text()
		equipo = self.lineEquipo.toPlainText()
		descripcion = self.lineDescripcion.toPlainText()
		problema = self.lineProblema.toPlainText()
		solucion = "null" #todavía no puse nada  aqui así que no hay pedo :V 

		try:
			conn = pymysql.connect(
				host = 'nombre del host',
				user = 'nombre de usuario',
				password ='contraseña del host',
				db = 'nombre de la base de datos',
				)

			cursor = conn.cursor()
		except Exception as e:
			print("No sé pudo conectar a la base de datos", e)
			QMessageBox.information(self, "Conexión", "No se pudo conectar a la base de datos, revise su conexión", QMessageBox.Ok)


		try:
			fechaActual = time.strftime("%d/%m/%y")

			datosInsertar = (nombre, nombre2, apellido, apellido2, cedula, fechaActual ,equipo, descripcion, problema, solucion)

			sql = "INSERT INTO recoverytable(NOMBRE, NOMBRE2, APELLIDO, APELLIDO2, CEDULA, FECHA, EQUIPO, DESCRIPCION, PROBLEMA, SOLUCION) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

			cursor.execute(sql, datosInsertar)

			conn.commit()
			cursor.close()
			conn.close()


			QMessageBox.information(self, "Registro", "Registro exitoso",QMessageBox.Ok)


			self.lineNombre.clear()
			self.lineSegundoNomb.clear()
			self.lineApellido.clear()
			self.lineSegundoApellido.clear()
			self.lineCedula.clear()
			self.lineEquipo.clear()
			self.lineDescripcion.clear()
			self.lineProblema.clear()

		except Exception as e:
			print("Error al insertar datos", e)
			QMessageBox.information(self, "Registro", "Registro fallido", QMessageBox.Ok)


	# Función para limpiar QlineEdits

	def limpiar(self):
		mensaje = QMessageBox()
		mensaje.setText("Está seguro de limpiar lo que escribió?")
		mensaje.setIcon(QMessageBox.Question)
		mensaje.setWindowTitle("Limpiar")
		mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		botonSalir = mensaje.button(QMessageBox.Yes)
		botonSalir.setText("Si")
		botonSalir.setStyleSheet("QPushButton{\n"
						"color: black;"
						"}\n"
						"QPushButton:hover{\n"
						"color:#35B6F2;\n"
						"}")


		botonNo = mensaje.button(QMessageBox.No)
		botonNo.setStyleSheet("QPushButton{\n"
						"color: black;"
						"}\n"
						"QPushButton:hover{\n"
						"color:rgb(255,0,0);\n"
						"}")

		mensaje.setStyleSheet("\n"
			"color: black;\n"
			"background-color: rgb(255,255,255);")
            
		mensaje.exec_()
            
		if mensaje.clickedButton() == botonSalir:
			self.lineNombre.clear()
			self.lineSegundoNomb.clear()
			self.lineApellido.clear()
			self.lineSegundoApellido.clear()
			self.lineCedula.clear()
			self.lineEquipo.clear()
			self.lineDescripcion.clear()
			self.lineProblema.clear()
		else:
			pass


	def cerrar(self):
		self.abrirVentana = segundaVentana()
		self.abrirVentana.show()
		self.close()


class ventanaEditar(QDialog):
	def __init__(self, dato, parent = None ):
		super(ventanaEditar, self).__init__()
		
		self.parent = parent
		self.datos = dato 
		self.resize(750, 630)
		self.setMaximumWidth(750)
		self.setMaximumHeight(630)
		self.setWindowIcon(QIcon("Recovery.png"))
		self.setWindowTitle("RecoveryBase Edición")
		self.setStyleSheet("QDialog{\n"
							"background-color: #F3F3F3;"
							"}\n"
							"")

		self.initUi()

	def initUi(self):

		estiloFontBotones2 = (QtGui.QFont("Roboto", 11, QtGui.QFont.Bold))
		estiloFonts2 = (QtGui.QFont("Roboto", 15, QtGui.QFont.Bold))
		estiloFontLines = (QtGui.QFont("Roboto", 11, QtGui.QFont.Bold))
		estiloFontLinesEdit = (QtGui.QFont("Roboto", 11, QtGui.QFont.Light))

		estiloFrameArriba = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: rgb(3, 169, 244);\n"
				"}")
		estiloFrameIzquierda = ("QFrame{\n"
				"color:#1b231f;\n"
				"background-color: white;\n"
				"border: 2px solid Gainsboro;\n"
				"}")

		estiloFrameRayita = ("QFrame{\n"
				"background-color: black;\n"
				"border-radius: 2px;"
				"}")

		estiloLabelRecovery = ("QLabel{\n"
				"color:white;\n"
				"background-color: rgb(3, 169, 244);\n"
				"}")

		estiloQLine = ("QLineEdit{\n"
				"color:black;\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid Gainsboro;\n"
				"border-radius: 4px;\n"
				"}\n"
				"QLineEdit:hover{\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid ;\n"
				"}")

		estiloQText = ("QTextEdit{\n"
				"color:black;\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid Gainsboro;\n"
				"border-radius: 4px;\n"
				"}\n"
				"QTextEdit:hover{\n"
				"background-color: #FAFAFA;\n"
				"border: 1px solid ;\n"
				"}")

		estiloLabels = ("QLabel{\n"
				"color:black;\n"
				"background-color: rgb(255, 255, 255);\n"
				"border: none;"
				"}")

		estiloBotones2 = ("QPushButton{\n"
						"color: black;"
						"background-color: rgba(255,255,255,0.8);"
						"border-radius: 1px;"
						"border: 1px solid Gainsboro;"
						"}\n"
						"QPushButton:hover{\n"
						"background-color: #F2F2F2;\n"
						"color:#35B6F2;\n"
						"}")

		self.frameArriba = QFrame(self)
		self.frameArriba.setGeometry(QRect(0,0,750,130))
		self.frameArriba.setStyleSheet(estiloFrameArriba)
		self.sombra2 = QGraphicsDropShadowEffect()
		self.sombra2.setBlurRadius(23)
		self.frameArriba.setGraphicsEffect(self.sombra2)

		self.frameIzquierda = QFrame(self)
		self.frameIzquierda.setGeometry(QRect(0,130,130,630))
		self.frameIzquierda.setStyleSheet(estiloFrameIzquierda)
		
		self.labelRecovery = QLabel(self)
		self.labelRecovery.setGeometry(QRect(30,10,250,100))
		self.labelRecovery.setText("RecoveryBase")
		self.labelRecovery.setFont(estiloFonts2)
		self.labelRecovery.setStyleSheet(estiloLabelRecovery)

		self.labelRecovery = QLabel(self.frameArriba)
		self.labelRecovery.setGeometry(QRect(350,20,300,100))
		self.labelRecovery.setText("Edición de Usuario")
		self.labelRecovery.setFont(estiloFonts2)
		self.labelRecovery.setStyleSheet(estiloLabelRecovery)

		self.botonActualizar = hoverButton(self.frameIzquierda)
		self.botonActualizar.setStyleSheet(estiloBotones2)
		self.botonActualizar.setGeometry(QRect(5,0,125,50))
		self.botonActualizar.setText("Actualizar")
		self.botonActualizar.setAutoDefault(False)
		self.botonActualizar.setFont(estiloFontBotones2)

		self.botonLimpiar = hoverButton(self.frameIzquierda)
		self.botonLimpiar.setStyleSheet(estiloBotones2)
		self.botonLimpiar.setGeometry(QRect(5,50,125,50))
		self.botonLimpiar.setIcon(QIcon('clean.svg'))
		self.botonLimpiar.setText("Limpiar")
		self.botonLimpiar.setAutoDefault(False)
		self.botonLimpiar.setFont(estiloFontBotones2)

		self.botonCancelar = hoverButton(self.frameIzquierda)
		self.botonCancelar.setStyleSheet(estiloBotones2)
		self.botonCancelar.setGeometry(QRect(5,100,125,50))
		self.botonCancelar.setText("Atrás")
		self.botonCancelar.setAutoDefault(False)
		self.botonCancelar.setFont(estiloFontBotones2)


		self.frameCentrado = QLabel(self)
		self.frameCentrado.setGeometry(QRect(200,180,490,430))
		self.frameCentrado.setStyleSheet(estiloFrameIzquierda)
		self.sombra4 = QGraphicsBlurEffect()
		self.sombra4.setBlurRadius(1)
		self.frameCentrado.setGraphicsEffect(self.sombra4)


		self.frameRayita = QLabel(self.frameCentrado)
		self.frameRayita.setGeometry(QRect(45,180,400,2))
		self.frameRayita.setStyleSheet(estiloFrameRayita)

		self.labelNombre = QLabel(self.frameCentrado)
		self.labelNombre.setGeometry(QRect(20,20,100,20))
		self.labelNombre.setText("Nombre")
		self.labelNombre.setFont(estiloFontLines)
		self.labelNombre.setStyleSheet(estiloLabels)


		self.lineNombre = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineNombre.setGeometry(20,60,100,30)
		self.lineNombre.setFont(estiloFontLinesEdit)
		self.lineNombre.setStyleSheet(estiloQLine)
		self.lineNombre.setText(self.datos[1])
		

		self.labelSegundoNomb = QLabel(self.frameCentrado)
		self.labelSegundoNomb.setGeometry(QRect(130,20,100,20))
		self.labelSegundoNomb.setText("S.Nombre")
		self.labelSegundoNomb.setFont(estiloFontLines)
		self.labelSegundoNomb.setStyleSheet(estiloLabels)

		self.lineSegundoNomb = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineSegundoNomb.setGeometry(130,60,100,30)
		self.lineSegundoNomb.setFont(estiloFontLinesEdit)
		self.lineSegundoNomb.setStyleSheet(estiloQLine)
		self.lineSegundoNomb.setText(self.datos[2])


		self.labelApellido = QLabel(self.frameCentrado)
		self.labelApellido.setGeometry(QRect(240,20,100,20))
		self.labelApellido.setText("Apellido")
		self.labelApellido.setFont(estiloFontLines)
		self.labelApellido.setStyleSheet(estiloLabels)

		self.lineApellido = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineApellido.setGeometry(240,60,100,30)
		self.lineApellido.setFont(estiloFontLinesEdit)
		self.lineApellido.setStyleSheet(estiloQLine)
		self.lineApellido.setText(self.datos[3])


		self.labelSegundoApellido = QLabel(self.frameCentrado)
		self.labelSegundoApellido.setGeometry(QRect(350,20,100,20))
		self.labelSegundoApellido.setText("S. Apellido")
		self.labelSegundoApellido.setFont(estiloFontLines)
		self.labelSegundoApellido.setStyleSheet(estiloLabels)

		self.lineSegundoApellido = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineSegundoApellido.setGeometry(350,60,100,30)
		self.lineSegundoApellido.setStyleSheet(estiloQLine)
		self.lineSegundoApellido.setFont(estiloFontLinesEdit)
		self.lineSegundoApellido.setText(self.datos[4])

		self.labelCedula = QLabel(self.frameCentrado)
		self.labelCedula.setGeometry(QRect(180,100,100,20))
		self.labelCedula.setText("Cédula")
		self.labelCedula.setFont(estiloFontLines)
		self.labelCedula.setStyleSheet(estiloLabels)

		self.lineCedula = QtWidgets.QLineEdit(self.frameCentrado)
		self.lineCedula.setGeometry(180,130,100,30)
		self.lineCedula.setStyleSheet(estiloQLine)
		self.lineCedula.setMaxLength(8)
		self.lineCedula.setInputMask('99999999')
		self.lineCedula.setFont(estiloFontLinesEdit)
		datoCedula = self.datos[5]
		datoCedula = str(datoCedula)
		self.lineCedula.setText(datoCedula)


		self.labelEquipo = QLabel(self.frameCentrado)
		self.labelEquipo.setGeometry(QRect(30,220,100,20))
		self.labelEquipo.setText("Equipo")
		self.labelEquipo.setAlignment(Qt.AlignCenter)
		self.labelEquipo.setFont(estiloFontLines)
		self.labelEquipo.setStyleSheet(estiloLabels)

		self.lineEquipo = QTextEdit(self.frameCentrado)
		self.lineEquipo.setGeometry(20,250,130,150)
		self.lineEquipo.setStyleSheet(estiloQText)
		self.lineEquipo.setFont(estiloFontLinesEdit)
		self.lineEquipo.setText(self.datos[7])

		self.labelDescripcion = QLabel(self.frameCentrado)
		self.labelDescripcion.setGeometry(QRect(200,220,100,20))
		self.labelDescripcion.setText("Descripción")
		self.labelDescripcion.setAlignment(Qt.AlignCenter)
		self.labelDescripcion.setFont(estiloFontLines)
		self.labelDescripcion.setStyleSheet(estiloLabels)

		self.lineDescripcion = QTextEdit(self.frameCentrado)
		self.lineDescripcion.setGeometry(190,250,130,150)
		self.lineDescripcion.setStyleSheet(estiloQText)
		self.lineDescripcion.setFont(estiloFontLinesEdit)
		self.lineDescripcion.setText(self.datos[8])

		self.labelProblema = QLabel(self.frameCentrado)
		self.labelProblema.setGeometry(QRect(350,220,100,20))
		self.labelProblema.setText("Problema")
		self.labelProblema.setAlignment(Qt.AlignCenter)
		self.labelProblema.setFont(estiloFontLines)
		self.labelProblema.setStyleSheet(estiloLabels)

		self.lineProblema = QTextEdit(self.frameCentrado)
		self.lineProblema.setGeometry(350,250,100,150)
		self.lineProblema.setStyleSheet(estiloQText)
		self.lineProblema.setFont(estiloFontLinesEdit)
		self.lineProblema.setText(self.datos[9])

		# Eventos de botones###############################################################################
		self.botonLimpiar.clicked.connect(self.limpiar)
		self.botonCancelar.clicked.connect(self.irAtras)
		self.botonActualizar.clicked.connect(self.actualizarUsuario)


	def actualizarUsuario(self):
		nombre = self.lineNombre.text()
		nombre2 = self.lineSegundoNomb.text()
		apellido = self.lineApellido.text()
		apellido2 = self.lineSegundoApellido.text()
		cedula = self.lineCedula.text()
		equipo = self.lineEquipo.toPlainText()
		descripcion = self.lineDescripcion.toPlainText()
		problema = self.lineProblema.toPlainText()
		idUsuario = self.datos[0]
		idUsuario = str(idUsuario)
		print(idUsuario)

		datosActualizar = (nombre, nombre2, apellido, apellido2, cedula, equipo, descripcion, problema, idUsuario)

		try:
			conn = pymysql.connect(
				host = 'nombre del host',
				user = 'nombre de usuario',
				password ='contraseña del host',
				db = 'nombre de la base de datos',
				)

			cursor = conn.cursor()
		except Exception as e:
			print("No sé pudo conectar a la base de datos", e)
			QMessageBox.information(self, "Conexión", "No se pudo conectar a la base de datos, revise su conexión", QMessageBox.Ok)

		try:
			sql = 'UPDATE recoverytable SET NOMBRE = %s,  NOMBRE2 = %s,  APELLIDO = %s, APELLIDO2 = %s, CEDULA = %s, EQUIPO = %s, DESCRIPCION = %s, PROBLEMA = %s WHERE ID = %s'

			cursor.execute(sql, datosActualizar)
			conn.commit()
			cursor.close()
			conn.close()

			QMessageBox.information(self, "Actualizar", "Actualización exitosa", QMessageBox.Ok)

		except Exception as e:
			print("Error al actualizar", e)
			QMessageBox.information(self, "Actualizar", "Error al actualizar", QMessageBox.Ok)

	# Función para limpiar QlineEdits

	def limpiar(self):
		mensaje = QMessageBox()
		mensaje.setText("Está seguro de limpiar lo que escribió?")
		mensaje.setIcon(QMessageBox.Question)
		mensaje.setWindowTitle("Limpiar")
		mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		botonSalir = mensaje.button(QMessageBox.Yes)
		botonSalir.setText("Si")
		botonSalir.setStyleSheet("QPushButton{\n"
						"color: black;"
						"}\n"
						"QPushButton:hover{\n"
						"color:#35B6F2;\n"
						"}")


		botonNo = mensaje.button(QMessageBox.No)
		botonNo.setStyleSheet("QPushButton{\n"
						"color: black;"
						"}\n"
						"QPushButton:hover{\n"
						"color:rgb(255,0,0);\n"
						"}")

		mensaje.setStyleSheet("\n"
			"color: black;\n"
			"background-color: rgb(255,255,255);")
            
		mensaje.exec_()
            
		if mensaje.clickedButton() == botonSalir:
			self.lineNombre.clear()
			self.lineSegundoNomb.clear()
			self.lineApellido.clear()
			self.lineSegundoApellido.clear()
			self.lineCedula.clear()
			self.lineEquipo.clear()
			self.lineDescripcion.clear()
			self.lineProblema.clear()
		else:
			pass

	def irAtras(self):
		mensaje = QMessageBox()
		mensaje.setText("¿Está seguro de regresar?")
		mensaje.setIcon(QMessageBox.Question)
		mensaje.setWindowTitle("Regresar")
		mensaje.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

		botonSalir = mensaje.button(QMessageBox.Yes)
		botonSalir.setText("Si")
		botonSalir.setStyleSheet("QPushButton{\n"
						"color: black;"
						"}\n"
						"QPushButton:hover{\n"
						"color:#35B6F2;\n"
						"}")


		botonNo = mensaje.button(QMessageBox.No)
		botonNo.setStyleSheet("QPushButton{\n"
						"color: black;"
						"}\n"
						"QPushButton:hover{\n"
						"color:rgb(255,0,0);\n"
						"}")

		mensaje.setStyleSheet("\n"
			"color: black;\n"
			"background-color: rgb(255,255,255);")
            
		mensaje.exec_()
            
		if mensaje.clickedButton() == botonSalir:
			self.close()
		else:
			pass

if __name__ == "__main__":
	app = QApplication(sys.argv)
	interface = Interface()
	interface.show()
	app.exec_()