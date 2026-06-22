import unittest
from main import processOrder, handlePayment

class TestMain(unittest.TestCase):
    def test_process_order(self):
        order_items = [1, 2, 3]
        try:
            processOrder(order_items)
        except IndexError as e:
            self.fail(f'Unexpected error: {e}')

    def test_handle_payment(self):
        payment_info = {}
        handlePayment(payment_info)

if __name__ == '__main__':
    unittest.main()