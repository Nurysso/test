import pytest
from main import poll, return_order_id

@pytest.mark.parametrize('inc_id', ['12345', '67890'])
def test_poll(inc_id):
    poll(inc_id, 'label')

def test_return_order_id():
    assert return_order_id() == '12345'