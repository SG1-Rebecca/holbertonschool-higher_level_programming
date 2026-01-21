#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res_div = a / b
    except ZeroDivisionError:
        res_div = None
    finally:
        print("Inside result: {} ".format(res_div))
    return res_div
