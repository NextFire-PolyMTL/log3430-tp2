import pytest

from ipinfo.bogon import is_bogon


@pytest.mark.parametrize(
    'value, expected',
    [
        # some valid bogons
        ('192.168.0.1', True),
        ('10.0.0.10', True),
        # some non-valid bogons
        ('174.134.92.1', False),
        ('1.1.1.1', False),
    ]
)
def test_is_bogon(value, expected):
    assert is_bogon(value) == expected
