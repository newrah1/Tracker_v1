import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget, QLabel, \
	QPushButton, QMessageBox, QComboBox

from PyQt5 import QtCore, QtGui, QtWidgets


class Firearms_Window:
	def dialog(self):
		mbox = QMessageBox()

		mbox.setText("Firearms Pop-up window")
		mbox.setDetailedText(
			"Random Text")
		mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

		#mbox = QComboBox()
		#mbox.addItems(['test1', 'test2'])


		mbox.exec_()

class Start_Window:
	switch_window = QtCore.pyqtSignal()

	app = QApplication(sys.argv)
	w = QWidget()
	w.resize(800, 800)
	w.setWindowTitle("Firearms Data Tracker")

	btn = QPushButton(w)
	btn.setText('Firearms')
	btn.move(50, 3)
	btn.show()
	btn.clicked.connect(Firearms_Window.dialog)

	w.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	Start_Window