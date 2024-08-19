# Iterative Method for Modulus

Thought this [Numberphile video](https://youtu.be/Ki-M1DJIZsk) showed an
interesting way of determining if the a number is divisible by a given integer.
Basically uses a graph to iteratively go through a numbers digits to determine
divisibility of a number.

It's not super impressive of an algorithm, but it looked interesting enough to
try quickly implementing it in general for any positive, non-zero integer.

# Code

This likely isn't very efficient compared to other methods. In fact, it's
probably better & easier to just use the modulus operator (`%`). (I did have it
in my Python implementation– could probably change it so didn't have to rely on
this little 'cheat')

## Running the script

Simply pass a number to be the base for divisibility then a list of numbers to
check for the remainder of the base number (separated by spaces).

For example, to check a list of numbers to see if they are divisible by 7:

```bash
python divisible.py 7 21 25 42 3_714_289 867_5309
```