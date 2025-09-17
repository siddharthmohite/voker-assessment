from google import genai
from google.genai import types

client = genai.Client()

add_order_decl = types.FunctionDeclaration(
    name="add_order",
    description="Place a new order with quantities of burgers, fries, and drinks.",
    parameters_json_schema={
        "type": "object",
        "properties": {
            "burgers": {"type": "integer"},
            "fries": {"type": "integer"},
            "drinks": {"type": "integer"},
        },
        "required": []
    }
)

cancel_order_decl = types.FunctionDeclaration(
    name="cancel_order",
    description="Cancel an existing order given its order_number.",
    parameters_json_schema={
        "type": "object",
        "properties": {"order_number": {"type": "integer"}},
        "required": ["order_number"]
    }
)

tool = types.Tool(function_declarations=[add_order_decl, cancel_order_decl])

tool_config = types.ToolConfig(
    function_calling_config=types.FunctionCallingConfig(
        mode="ANY",
        allowed_function_names=["add_order", "cancel_order"]
    )
)

config = types.GenerateContentConfig(
    tools=[tool],
    tool_config=tool_config,
    temperature=0.0
)
