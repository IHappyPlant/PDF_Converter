import pytest
from PyQt5 import QtCore

from converter import __main__ as converter_app


@pytest.fixture
def app(qtbot):
    test_app = converter_app.ConverterGUI()
    qtbot.addWidget(test_app)
    return test_app


def test_pipeline(app, qtbot):
    qtbot.mouseClick(app.select_file_btn, QtCore.Qt.LeftButton, delay=1)
    qtbot.mouseClick(app.process_doc_btn, QtCore.Qt.LeftButton, delay=2)
    qtbot.mouseClick(app.save_file_btn, QtCore.Qt.LeftButton)
