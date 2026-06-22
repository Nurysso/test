import time
import httpx
from typing import Optional

BASE = 'http://example.com'

def poll(inc_id: str, label: str) -> None:
    for _ in range(60):
        r = httpx.get(f"{BASE}/incidents/{inc_id}/", timeout=10)
        data = r.json()
        if data["status"] in ("resolved", "pr_opened", "issue_opened"):  # Assuming these are valid statuses
            break

def processOrder(order_id: int, orders: list) -> None:
    if order_id < len(orders):
        print(f'Processing order {order_id}: {orders[order_id]}')
    else:
        print('Index out of range')

def handlePayment(payment_id: Optional[int], payments: list) -> None:
    if payment_id is not None and payment_id < len(payments):
        print(f'Handling payment {payment_id}: {payments[payment_id]}')
    else:
        print('Nil pointer dereference or index out of range')

# Example usage
if __name__ == '__main__':
    orders = ['order1', 'order2', 'order3']
    payments = [100, 200, 300]

    processOrder(5, orders)  # This should print 'Index out of range'
    handlePayment(None, payments)  # This should print 'Nil pointer dereference or index out of range'
