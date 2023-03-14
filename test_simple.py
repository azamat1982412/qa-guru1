import random

import pytest


@pytest.fixture(scope="session")
def browser ():
    print(random.randint(0, 100))
    print("Открываем браузер")
    yield "Chrome"
    print("Закрывыем браузер")




@pytest.fixture()
def get_admin(browser,teardown):
    return random.randint(0, 100)


def test_simple(get_admin,browser):
    assert get_admin == 5,"Айтишник администратора ожидался 5"
    assert browser == "Chrome"
    assert 1 == 1,"единица не должна быть равно двойке"



def test_another():
        assert 1 == 1,"единица не должна быть ровной двойке"