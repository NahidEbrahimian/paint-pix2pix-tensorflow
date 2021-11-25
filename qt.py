import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
from inference_qt import inference

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Paint')

        self.setGeometry(600, 150, 256, 256)
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.draw = False
        self.brushSize = 1
        self.brushColor = Qt.black
        self.lastPoint = QPoint()
        self.output_dir = 'input_img'

        # main manu
        menuBar = self.menuBar()

        # file manu
        fileMenu = menuBar.addMenu('File')
        clearAction = QAction('Clear', self)
        fileMenu.addAction(clearAction)
        clearAction.triggered.connect(self.clear)

        # run manu
        inference = menuBar.addMenu('Pix2Pix-Process')
        run = QAction('run', self)
        inference.addAction(run)
        inference.triggered.connect(self.run_inference)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw = True
            self.lastPoint = event.pos()

    def mouseMoveEvent(self, event):
        if Qt.LeftButton & self.draw:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brushColor, self.brushSize,
                                Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            painter.drawLine(self.lastPoint, event.pos())

            self.lastPoint = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw = False

    def paintEvent(self, event):
        canvasPainter = QPainter(self)
        canvasPainter.drawImage(self.rect(), self.image, self.image.rect())

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def run_inference(self):
        import cv2
        self.image_name = QtCore.QDateTime.currentDateTime().toString()+".jpg"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
        self.image.save(os.path.join(self.output_dir, self.image_name))

        img = cv2.imread(os.path.join(self.output_dir, self.image_name))
        self.gen_output = inference(img)
        output_directory = 'qt_output'
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        cv2.imwrite(os.path.join(self.output_directory, self.image_name), self.gen_output)

app = QApplication([])
window = Window()
window.show()
app.exec_()
