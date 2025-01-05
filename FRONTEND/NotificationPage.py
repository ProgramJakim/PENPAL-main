from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QListWidget

class NotificationWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Notifications")
        self.setFixedSize(400, 300)
        self.setStyleSheet("background-color: #FFF9F0;")

        layout = QVBoxLayout(self)

        # Divider for users added in the system
        self.users_added_label = QLabel("Users Added in the System")
        self.users_added_label.setStyleSheet("font: 16px 'Rockwell'; color: #7A0C0C;")
        layout.addWidget(self.users_added_label)

        self.users_added_list = QListWidget()
        layout.addWidget(self.users_added_list)

        # Divider for notifications of accepted friend requests
        self.accepted_requests_label = QLabel("Accepted Friend Requests")
        self.accepted_requests_label.setStyleSheet("font: 16px 'Rockwell'; color: #7A0C0C;")
        layout.addWidget(self.accepted_requests_label)

        self.accepted_requests_list = QListWidget()
        layout.addWidget(self.accepted_requests_list)

    def set_users_added(self, users):
        self.users_added_list.clear()
        self.users_added_list.addItems(users)

    def set_accepted_requests(self, requests):
        self.accepted_requests_list.clear()
        self.accepted_requests_list.addItems(requests)