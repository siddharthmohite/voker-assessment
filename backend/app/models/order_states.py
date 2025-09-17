orders: dict[int, dict[str, int]] = {}
_counter = 1

def generate_order_number() -> int:
    global _counter
    order_num = _counter
    _counter += 1
    return order_num