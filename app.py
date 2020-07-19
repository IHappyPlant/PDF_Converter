from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5.QtGui import QImage, QPixmap
import window
import sys
from utils import convert, get_file_name
import cv2


class MyApp(QMainWindow, window.Ui_MainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.select_file_btn.clicked.connect(self.select_file)
        self.process_doc_btn.clicked.connect(self.process_file)
        self.save_file_btn.clicked.connect(self.save_file)
        self.to_next_btn.clicked.connect(self.to_next_page)
        self.to_prev_btn.clicked.connect(self.to_prev_page)
        self.file_path = None
        self.file_name = None
        self.processed = None
        self.image_format = None
        self.save_path = None
        self.active_page = None
        self.color_mode = None
        self.resized.connect(self.bacground_resize)

    def resizeEvent(self, event):
        self.resized.emit()
        return super(MyApp, self).resizeEvent(event)

    def bacground_resize(self):
        if self.active_page:
            self.display_active_page()

    def select_file(self):
        try:
            table_path = \
                QFileDialog.getOpenFileUrl(caption='Select file')[0].path()
            if table_path.endswith('.pdf'):
                self.select_file_label.setText('File selected')
                self.file_path = table_path
                self.file_name = get_file_name(table_path)
        except FileNotFoundError:
            self.select_file_label.setText('File selected')

    def process_file(self):
        if self.file_path:
            dpi = int(self.dpi_box.currentText())
            self.color_mode = self.color_mode_box.currentText().lower()
            self.image_format = self.image_format_box.currentText().lower()
            self.processed = convert(self.file_path, dpi, self.image_format,
                                     self.color_mode)
            self.active_page = 1
            self.display_active_page()

    def save_file(self):
        if self.processed:
            try:
                self.save_path = QFileDialog.getExistingDirectoryUrl(
                    caption='Save to').path()
                for i, page in enumerate(self.processed):
                    name = '{}_{}.{}'.format(self.file_name, str(i),
                                             self.image_format)
                    cv2.imwrite(name, page)
            except NotADirectoryError:
                pass

    def display_active_page(self):
        if self.color_mode == 'rbga':
            frmt = QImage.Format_RGBA8888
        elif self.color_mode == 'rgb':
            frmt = QImage.Format_RGB888
        elif self.color_mode == 'grayscale' or self.color_mode == 'binary':
            frmt = QImage.Format_Grayscale8
        cur_img = self.processed[self.active_page - 1]
        img = QImage(cur_img, cur_img.shape[1], cur_img.shape[0],
                     cur_img.shape[1] * 3, frmt)
        img = img.smoothScaled(self.display_page_label.width(),
                               self.display_page_label.height())
        img = QPixmap(img)
        self.page_numbers_label.setText('Page {} of {}'.format(
            self.active_page, len(self.processed)))
        self.display_page_label.setPixmap(img)
        self.display_page_label.show()

    def to_next_page(self):
        if self.active_page:
            if self.active_page < len(self.processed):
                self.active_page += 1
                self.display_active_page()

    def to_prev_page(self):
        if self.active_page:
            if self.active_page > 1:
                self.active_page -= 1
                self.display_active_page()


def main():
    app = QApplication(sys.argv)
    window_ = MyApp()
    window_.show()
    app.exec_()


if __name__ == '__main__':
    main()