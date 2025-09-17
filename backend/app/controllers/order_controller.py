from fastapi import APIRouter
from google.genai import types
from app.models.schemas import UserRequest
from app.models import order_states
from app.models.order_states import orders
from app.services.order_service import execute_function_by_name
from app.gemini.gemini import client, config

router = APIRouter()

@router.post("/send_chat")
async def send_chat(req: UserRequest):
    user_input = req.input
    contents = [types.Content(role="user", parts=[types.Part(text=user_input)])]

    response = client.models.generate_content(
        model="gemini-1.5-flash",
        config=config,
        contents=contents
    )

    if getattr(response, "function_calls", None):
        fn = response.function_calls[0]
        fn_name = fn.name
        fn_args: dict = fn.args or {}
        print("fn args", fn_args)
        result_text = execute_function_by_name(fn_name, fn_args)

        current_orders = [{"order_number": k, "items": v} for k, v in order_states.orders.items()]
        return {
            "function": fn_name,
            "params": fn_args,
            "result": result_text,
            "orders": current_orders
        }

    return {"response": response.text, "orders": order_states.orders}

@router.get("/orders")
async def get_order_history():
    return [
        {"order_number": order_num, **items}
        for order_num, items in orders.items()
    ]

@router.get("/orders/totals")
async def get_order_summary():
    total_burgers = sum(order["burgers"] for order in orders.values())
    total_fries = sum(order["fries"] for order in orders.values())
    total_drinks = sum(order["drinks"] for order in orders.values())
    return {
        "burgers": total_burgers,
        "fries": total_fries,
        "drinks": total_drinks,
    }