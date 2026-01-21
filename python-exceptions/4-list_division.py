#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for element in range(list_length):
        try:
            div_list = my_list_1[element] / my_list_2[element]
        except TypeError:
            print("wrong type")
            div_list = 0
        except ZeroDivisionError:
            print("division by 0")
            div_list = 0
        except IndexError:
            print("out of range")
            div_list = 0
        finally:
            new_list.append(div_list)
    return new_list
