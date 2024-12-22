from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QApplication
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os

class Ui_Homepage(QWidget):
    def __init__(self):
        super().__init__()

        # Set the fixed size of the main window
        self.setFixedSize(1440, 900)

        # Create a scroll area
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)  # Disable horizontal scrolling

        # Create a widget to hold the content
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Create a label to hold the background image
        self.background_label = QLabel(content_widget)
        self.background_label.setFixedSize(1440, 4104)
        self.background_label.setContentsMargins(0, 0, 0, 0)  # Remove margins

        # Set the background image
        current_directory = os.path.dirname(os.path.abspath(__file__))
        background_image_path = os.path.join(current_directory, '..', 'resources', 'images', 'HOMEPAGE.png')
        self.background_label.setPixmap(QPixmap(background_image_path).scaled(1440, 4104))

        # Add the background label to the content layout
        content_layout.addWidget(self.background_label)

        # Set the content widget as the scroll area's widget
        scroll_area.setWidget(content_widget)

        # Set the layout of the main window
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(0, 0, 0, 0)  # Remove margins
        main_layout.addWidget(scroll_area)
        self.setLayout(main_layout)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Ui_Homepage()
    window.show()
    sys.exit(app.exec_())