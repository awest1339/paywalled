#!/usr/bin/env python
import sys
from PySide.QtCore import *
from PySide.QtGui import *

import paywalled as p


class Form(QDialog):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.url = QLineEdit('Enter url here')
        self.proxy = QLineEdit('Enter proxy here (optional)')
        self.button = QPushButton('Get page')
        self.no_check_certificate = QCheckBox('No Check Certificate')
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.url)
        layout.addWidget(self.proxy)
        layout.addWidget(self.no_check_certificate)
        layout.addWidget(self.button)
        # Set dialog layout
        self.setLayout(layout)
        self.setGeometry(300, 300, 600, 300)
        self.setWindowTitle('Paywalled')
        # Add button signal to greetings slot
        self.button.clicked.connect(self.make_request)

    # Get the web page
    def make_request(self):
        web_content = p.get_web_content(self.url.text(), self.proxy.text(), self.no_check_certificate.isChecked())
        full_path = p.write_web_content_to_file(web_content)
        p.open_web_content(full_path)

        
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec_())