import pytest


@pytest.fixture()
def set_up():
    print('Вход в систему выполнен')
    yield
    print('Выход из системы')