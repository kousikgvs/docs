from langchain_core.tools import tool
import requests 

# Weather Tool
@tool
def get_weather(location: str) -> str:
    """
    DocString -> Used to get the current weather of a given location.
    Args:       
        location (str): The city name to get the weather for.
    Returns:
        str: A string describing the current weather.
    """

    url = f"https://wttr.in/{location}?format=j1"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    return data

# Math Tool
@tool
def calculate(expression: str) -> str:
    """Calculate a mathematical expression.

    USE THIS TOOL FOR:
    - Any mathematical calculations or arithmetic operations
    - Queries involving numbers and operators (+, -, *, /, **, %)
    - Questions asking to compute, calculate, or solve math problems
    - Evaluating mathematical expressions

    EXAMPLE QUERIES:
    - "What is 2 + 2?"
    - "Calculate 15 times 7"
    - "Solve 100 / 4"
    - "What's 5 to the power of 3?"
    - "Compute 45 * 12 + 30"

    DO NOT USE FOR:
    - Word problems without explicit expressions (extract the math first)
    - Questions about mathematical concepts or theory

    Args:
    expression: Math expression like "2 + 2" or "15 * 7" (use standard Python operators)
    """

    result = eval(expression)
    print(f"Calculated Result: {result}")
    return str(result)
