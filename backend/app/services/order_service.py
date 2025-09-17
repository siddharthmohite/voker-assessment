from app.models import order_states

def add_order_backend(args: dict) -> str:
    burgers = int(args.get("burgers", 0))
    fries = int(args.get("fries", 0))
    drinks = int(args.get("drinks", 0))

    if burgers == 0 and fries == 0 and drinks == 0:
        return "Error: no items specified."

    order_num = order_states.generate_order_number()
    order_states.orders[order_num] = {"burgers": burgers, "fries": fries, "drinks": drinks}
    return f"Order {order_num} placed: {burgers} burgers, {fries} fries, {drinks} drinks."


def cancel_order_backend(args: dict) -> str:
    order_num = int(args.get("order_number"))
    if order_num not in order_states.orders:
        return f"Error: order {order_num} not found."
    del order_states.orders[order_num]
    return f"Order {order_num} cancelled successfully."


def execute_function_by_name(name: str, args: dict) -> str:
    if name == "add_order":
        return add_order_backend(args)
    elif name == "cancel_order":
        return cancel_order_backend(args)
    return "Error: unknown function"
