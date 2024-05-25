import pytest
from main_prog import *
from contextlib import nullcontext as keinER



@pytest.mark.parametrize("Name, Count, Category, Country, Weight, expected", [

    ("BOOK", 5, "tech", "USA", 5, None),
    ("BOOK", 5, "tech", "USA", 6.9, None),
    ("BOOK", 5.7, "tech", "USA", 5, ValueError),
    ("BOOK", 5, 22232, "USA", 5, ValueError),
    ("BOOK", 5, -343434, "USA", 5, ValueError),
    ("-32323", 5, 22232, "USA", 5, ValueError),
    ("Pop", -5, "tech", "UA", -5, ValueError),
    ("BOOK", -5, "tech", "USA", 5, ValueError),
    ("BOOK", -5, "tech", 1223, -5, ValueError),
    (232323, 5, "tech", "USA", 5, None),
    (232323, 5, "tech", True, 5, TypeError),
    (232323, 5, "tech", False, 5, TypeError),
    ("232323", 5, "tech", True, 5, TypeError),
    ("BOOK", -5, "tech", "USA", -5, ValueError),
    ("Test", 1, "food", 2344, 2, TypeError),  
    ("Test1", "one", "cloth", "USA", 2, ValueError), 
    ("Test2", 1, "Category1", "InvalidCountry", 2, TypeError),



])
def test_send_data(Name, Count, Category, Country, Weight, expected):
    if expected is None:
        # Якщо очікується успішне виконання, просто викликайте функцію і перевірте, чи не виникає винятків
        try:
            send_data(Name, Count, Category, Country, Weight)
        except Exception as e:
            pytest.fail(f"Test failed: {e}")
    else:
        # Якщо очікується виняток, перевірте, чи виникає він
        with pytest.raises(expected):
            send_data(Name, Count, Category, Country, Weight)


