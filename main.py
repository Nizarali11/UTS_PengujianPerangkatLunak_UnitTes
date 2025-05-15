from repository.user_repository import UserRepository
from usecases.user_usecase import UserUseCase
from interface.user_interface import run_interface

repo = UserRepository()
usecase = UserUseCase(repo)
run_interface(usecase)
