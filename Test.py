from PopUp_Add_Bullet import Ui_PopUp_Add_Bullet
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Test:

	def __init__(self):
		pass

	def default(self):
		app = QtWidgets.QApplication(sys.argv)
		PopUp_Add_Bullet = QtWidgets.QMainWindow()
		ui = Ui_PopUp_Add_Bullet()
		ui.setupUi(PopUp_Add_Bullet)
		PopUp_Add_Bullet.show()
		sys.exit(app.exec_())

	def run(self):
		self.default()


if __name__ == "__main__":
	DH = Test()
	DH.run()
