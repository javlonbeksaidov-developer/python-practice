import pytest
from xatolik_ushlash import check_password


def test_check_password():
    # 1. Uzunligi yetarli emas
    with pytest.raises(ValueError, match="kamida 8 ta"):
        check_password("Jav1")

    # 2. Raqam qatnashmagan
    with pytest.raises(ValueError, match="kamida 1 ta raqam"):
        check_password("Javlonbek")


def test_parol_togri():
    assert check_password("Javlonbek123") == True
