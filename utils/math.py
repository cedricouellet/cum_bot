"""
Math functions
"""

import numexpr


def calculate_expression(expression: str) -> int:
    """
    Calculate a mathematical expression.

    :param expression: The expression to calculate
    :return: The result of the calculated expression
    :raise BaseException: If there was a problem calculating the expression
    """
    try:
        return numexpr.evaluate(expression)
    except BaseException as e:
        raise e
