def processOrder(order_id: str) -> None:
    order = get_order(order_id)
    if order is None or len(order.items) < 5:
        return
    # Process the order

def handlePayment(payment_id: str) -> None:
    payment = get_payment(payment_id)
    if payment is None:
        return
    # Handle the payment