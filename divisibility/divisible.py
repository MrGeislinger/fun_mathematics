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
    # base_number = 7
    # nums = [70, 98, 16, 700, 699]
    base_number = int(sys.argv[1])
    nums = (int(number) for number in sys.argv[2:])

    my_div = get_div_func(base_number)
    for n in nums:
        print(f'For {n}:')
        print(f'\t{my_div(n)}')
    print('DONE')