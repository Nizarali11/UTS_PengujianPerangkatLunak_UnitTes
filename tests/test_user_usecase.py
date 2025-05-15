import unittest
from domain.entities import User
from repository.user_repository import UserRepository
from usecases.user_usecase import UserUseCase

class TestUserUseCase(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository()
        self.usecase = UserUseCase(self.repo)
        self.user = User(1, "Ari", "ari@mail.com")

    def test_create_user(self):
        self.usecase.create_user(self.user)
        self.assertEqual(len(self.usecase.browse_users()), 1)

    def test_read_user(self):
        self.usecase.create_user(self.user)
        user = self.usecase.read_user(1)
        self.assertEqual(user.name, "Ari")

    def test_edit_user(self):
        self.usecase.create_user(self.user)
        result = self.usecase.edit_user(1, "Rina", "rina@mail.com")
        self.assertTrue(result)
        self.assertEqual(self.usecase.read_user(1).name, "Rina")

    def test_edit_user_fail(self):
        result = self.usecase.edit_user(99, "X", "x@mail.com")
        self.assertFalse(result)

    def test_delete_user(self):
        self.usecase.create_user(self.user)
        self.assertTrue(self.usecase.delete_user(1))
        self.assertIsNone(self.usecase.read_user(1))

    def test_browse_users(self):
        self.usecase.create_user(self.user)
        self.usecase.create_user(User(2, "Budi", "budi@mail.com"))
        self.assertEqual(len(self.usecase.browse_users()), 2)
