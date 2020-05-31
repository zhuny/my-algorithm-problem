from typing import List


def is_valid_price(lower_bound, upper_bound, representative, option_price_list):
    for option in option_price_list:
        if option*100 < lower_bound*representative:
            return False
        if upper_bound*representative < option*100:
            return False
    return True


def solution_slow(lower_bound: int, upper_bound: int,
                  option_price_list: List[int]):
    count = 0
    for price in option_price_list:
        if is_valid_price(lower_bound, upper_bound, price, option_price_list):
            count += 1
    return count


if __name__ == '__main__':
    assert solution_slow(80, 150, [85, 100, 140]) == 1
