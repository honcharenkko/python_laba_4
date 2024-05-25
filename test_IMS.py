import pytest
from main_prog import *
from contextlib import nullcontext as keinER




# Тести для функції add_arb
@pytest.mark.parametrize(
    "username, password, expected_exception",
    [
        (123, 123, TypeError),
        (-123, 123, TypeError),
        (123, -123, TypeError),
        ('2ededhe', 123, TypeError),
        ('123', 123, TypeError),
        (True, 123, TypeError),
        (['fjrijfurj'], 2323, TypeError),
        ('-123', 123, TypeError),
        ('123', '123', ValueError),
        ([45], bool, TypeError),
        ([-55], 43434, TypeError),
        ([True], bool, TypeError),
        ('[45]', 123, TypeError),
        ('!Roger', '3434', ValueError),
        ('Roger', '!_3434', ValueError),
        ('Nikson', 123, TypeError),
        ('Николай', 3434, TypeError),
    ]
)
def test_add_arb(username, password, expected_exception):
    if expected_exception is keinER:
        with keinER():
            add_arb(username, password)
    else:
        with pytest.raises(expected_exception):
            add_arb(username, password)


# #Тести для функції login_user
# @pytest.mark.parametrize(
#     "username, password, expected_exception",
#     [
#         (123, 123, TypeError),
#         (-123, 123, TypeError),
#         (123, -123, TypeError),
#         ("2ededhe", 123, keinER),
#         ('123', 123, keinER),
#         (True, 123, TypeError),
#         (['fjrijfurj'], 2323, TypeError),
#         ('-123', 123, keinER),
#         ('123', "123", keinER),
#         ([45], bool, TypeError),
#         ([-55], 43434, TypeError),
#         ([True], bool, TypeError),
#         ("[45]", 123, keinER),
#         ("!Roger", "3434", keinER),
#         ("Roger", "!_3434", keinER),
#         ('Nikson', 123, keinER),
#         ("Николай", 3434, keinER),
#     ]
# )
# def test_login_user(username, password, expected_exception):
#     with pytest.raises(expected_exception) if expected_exception is not keinER else keinER():
#         login_user(username, password)









