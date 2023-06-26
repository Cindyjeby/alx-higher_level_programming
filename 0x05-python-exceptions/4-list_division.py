#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    total = []
    for k in range(list_length):
        try:
            dividend = my_list_1[k]
            divisor = my_list_2[k]
            division_total = dividend / divisor
        except ZeroDivisonError:
            print("division by 0")
            division_total = 0
        except TypeError:
            print("wrong type")
            division_total = 0
        except IndexError:
            print("out of range")
            division_total = 0
        finally:
            total.append(division_total)
            return (total)
