def processOrder(orders, order_index):
    if order_index < len(orders):
        # Process the order
        pass
    else:
        raise IndexError(f'Index out of range [{order_index}] with length {len(orders)}')


def handlePayment(payment_processor, payment_id):
    if payment_processor is not None and payment_id is not None:
        # Handle the payment
        pass
    else:
        raise ValueError('Nil pointer dereference')