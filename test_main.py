import pytest
from main import processOrder, handlePayment
def test_process_order_index_out_of_range():
    order = {'items': [1, 2, 3]}
    assert processOrder(order['id']) is None
def test_handle_payment_nil_pointer_dereference():
    payment = None
    assert handlePayment(payment['id']) is None