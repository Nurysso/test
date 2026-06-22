import unittest
from main import processOrder, handlePayment
class TestMain(unittest.TestCase):
    def test_process_order_index_error(self):
        with self.assertRaises(IndexError):
            processOrder([], 5)

    def test_handle_payment_nil_pointer(self):
        with self.assertRaises(ValueError):
            handlePayment(None, None)
if __name__ == '__main__':
    unittest.main()