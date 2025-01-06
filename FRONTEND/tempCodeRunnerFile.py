def set_users_added(self, users):
        self.users_added_list.clear()
        image_path = os.path.join(os.path.dirname(__file__), '..', 'resources', 'images', 'DefaultProfile.png')
        for user in users:
            item = QListWidgetItem(self.users_added_list)
            widget = ListItemWidget(user, image_path)
            item.setSizeHint(widget.sizeHint())
            self.users_added_list.setItemWidget(item, widget)
            item_text = f"You add {user}!"