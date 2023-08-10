# Octonion Calculator
A python class for octonions and their basic operations. Currently supported is:
* Addition/subtraction
* Multiplication/division
* Inverse
* Conjugate
* Norm

Also comes with two functions outside the class for generating pseudo-random octonions as a string (for use with initializing the object).

# Usage
Have Python 3.11 (likely compatible with much older versions) with the math, numpy, and decimal packages.
Run the file in a python console. Don't forget to ``print()`` the results of your operation or you will just be returned a hex address for the resulting Octonian object.

---

Initialize an Octonian as follows:

``test = Octonian(NUM)``

where NUM is a tuple of the form (a_0, a_1, a_2, a_3, a_4, a_5, a_6, a_7) and a_i are rational numbers (integers, floats, or Decimals): the coefficients for the basis elements. Zeroes must *not* be omitted. For example:

Acceptable: (1, 2, -97.151516156498794, 0, 0, 0, 0, 0)

Unacceptable: (1, 2, -97.151516156498794)

---

Addition, subtraction, multiplication, and division overload the standard operators and return an Octonian object. Inverse and conjugate functions are accessed by ``test.inverse()`` and ``test.conj()`` respectively, both of which return an Octonian object. Norm can be accessed with ``test.norm`` and returns a Decimal object.

---

Call the pseudo-random octonion generator by ``random_octonian()`` or ``random_octonian_int()``. The prior returns an octonion as a tuple of the appropriate format with pseudo-random float coefficients in the interval [0,1). The latter with integers between -100 and 100. For usage with initialization, one would input ``test = Octonian(random_octonian_int())``, for example.

# Miscellaneous
Yes, I know that I have misspelled "octonion" throughout the file, including in the name of the file. I don't know what to say other than I must have read it like this somewhere and now I kind of like it.
