from module import GLOBAL_VAR
import module
from one import one


def two():
    print('Второй пользователь')
    print(GLOBAL_VAR)
    print(module.GLOBAL_VAR)


one()
print()
two()
GLOBAL_VAR = 2024

one()
print()
two()
module.GLOBAL_VAR = 2024

one()
print()
two()
