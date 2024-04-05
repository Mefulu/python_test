from module import GLOBAL_VAR
import module


def one():
    print('Первый пользователь')
    print(GLOBAL_VAR)
    print(module.GLOBAL_VAR)
