import unittest
from main import processOrder, handlePayment

class TestMain(unittest.TestCase):
    def test_processOrder(self):
        orders = ['order1', 'order2', 'order3']
        processOrder(0, orders)  # Should not raise an exception
        processOrder(5, orders)  # Should print 'Index out of range'

    def test_handlePayment(self):
        payments = [100, 200, 300]
        handlePayment(0, payments)  # Should not raise an exception
        handlePayment(None, payments)  # Should print 'Nil pointer dereference or index out of range'

if __name__ == '__main__':
    unittest.main()