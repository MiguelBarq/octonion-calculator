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

where NUM is a string of the form "a_1e_1 + a_2e_2 + a_3e_3 + a_4e_4 + a_5e_5 + a_6e_6 + a_7e_7" and a_i are numbers (integers or decimals as a substring, do *not* use scientific notation). Whitespace may be omitted, the order of the terms in not strict, terms with a_i = 0 may be omitted, and if a_i == 1 the coefficient may also be omitted. The pluses *must* be there, even if a_i is negative. For example:

Acceptable: "e_0 + 12e_7 + -97.151516156498794e_2"

Unacceptable "e_0 + 12e_7 - 97.151516156498794e_2"

---

Addition, subtraction, multiplication, and division overload the standard operators and return an Octonian object. Inverse and conjugate functions are accessed by ``test.inverse()`` and ``test.conj()`` respectively, both of which return an Octonian object. Norm can be accessed with ``test.norm`` and returns a Decimal object.

---

Call the pseudo-random octonion generator by ``random_octonian()`` or ``random_octonian_int()``. The prior returns an octonion as a string of the appropriate format with pseudo-random float coefficients in the interval [0,1). The latter with integers between -100 and 100. For usage with initialization, one would input ``test = Octonian(random_octonian_int())``, for example.

# Miscellaneous
Yes, I know that I have misspelled "octonion" throughout the file, including in the name of the file. I don't know what to say other than I must have read it like this somewhere and now I kind of like it.
