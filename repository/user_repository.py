class UserRepository:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.user_id] = user

    def get_all_users(self):
        return list(self.users.values())

    def get_user(self, user_id):
        return self.users.get(user_id)

    def update_user(self, user_id, name, email):
        if user_id in self.users:
            self.users[user_id].name = name
            self.users[user_id].email = email
            return True
        return False

    def delete_user(self, user_id):
        return self.users.pop(user_id, None) is not None
