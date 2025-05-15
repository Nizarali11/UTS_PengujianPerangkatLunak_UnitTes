class UserUseCase:
    def __init__(self, repository):
        self.repo = repository

    def create_user(self, user):
        self.repo.add_user(user)

    def browse_users(self):
        return self.repo.get_all_users()

    def read_user(self, user_id):
        return self.repo.get_user(user_id)

    def edit_user(self, user_id, name, email):
        return self.repo.update_user(user_id, name, email)

    def delete_user(self, user_id):
        return self.repo.delete_user(user_id)
