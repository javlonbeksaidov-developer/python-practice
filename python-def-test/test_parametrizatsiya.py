import pytest
from parametrizatsiya import kabisa


@pytest.mark.parametrize(
    "kirish, natija",
    [
        (0, True),
        (2000, True),
        (2004, True),
        (2005, False),
        (2026, False),
        (-1, False),
    ],
)
def test_kabisa(kirish, natija):
    assert kabisa(kirish) == natija
