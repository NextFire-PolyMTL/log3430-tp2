import pytest

from ipinfo.handler_utils import read_coords


@pytest.mark.parametrize(
    'value, expected',
    [
        (None, (None, None)),
        ('', (None, None)),
        ('1.1', (None, None)),
        ('1.1,2.2', ('1.1', '2.2')),
        ('1.1,2.2,3.3', (None, None)),
        ('abcde', (None, None)),
    ]
)
def test_read_coords(value, expected):
    assert read_coords(value) == expected
