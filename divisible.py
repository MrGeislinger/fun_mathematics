# https://www.youtube.com/watch?v=Ki-M1DJIZsk
# Division graph
from typing import Callable
import sys

DivisionGraph = dict[int, int]

def get_div_func(n: int) -> Callable[[int, bool], int]:
    def div(number: int, debug: bool = False) -> int:
        # Define the 'division graph': each digit is a multiple of 10
        graph: DivisionGraph = {i: (i * 10) % n for i in range(n)}
        print(f'Remainder for {n}')
        # Go through each digit keeping track of the remainder
        remainder = 0
        for digit in str(number):
            # Travel graph then add the digit (modular arithmetic) 
            remainder = (graph[remainder] + int(digit)) % n
            if debug: print(f'\tDIGIT: {digit} --> {remainder}')
        return remainder
    return div


if __name__ == '__main__':
    # nums = [70, 98, 16, 700, 699]
    nums = (str(number) for number in sys.argv[1:])

    div7 = get_div_func(7)
    div5 = get_div_func(5)
    for n in nums:
        print(f'For {n}:')
        print(f'\t{div7(n)}')
        print(f'\t{div5(n)}')
    print('DONE')