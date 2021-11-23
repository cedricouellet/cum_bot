"""
Functions related to mathematical calculations.
"""

import numexpr


def calculate_expression(expression: str) -> int:
    """
    Calculate a mathematical expression.

    Parameters:
    - `{str} expression` - The expression to calculate

    Returns:
    - `{str}` - The result of the calculated expression

    Raises:
    - `BaseException` - If there was a problem calculating the expression
    """
    try:
        return numexpr.evaluate(expression)
    except BaseException as e:
        raise e
