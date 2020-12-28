import calc


def test_add():
    num1 = 3
    num2 = 5
    assert calc.add_num(num1, num2) == 8


def test_sub():
    num1 = 3
    num2 = 5
    assert calc.sub_num(num1, num2) == -2


def test_multi():
    num1 = 3
    num2 = 5
    assert calc.multi_num(num1, num2) == 15


def test_devide():
    num1 = 3
    num2 = 5
    assert calc.devide_num(num1, num2) == 0.6
