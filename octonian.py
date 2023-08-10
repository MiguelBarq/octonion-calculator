from math import sqrt
from numpy import array, random
from decimal import Decimal
""""
NOTE: CURRENTLY REQUIRES NEGATIVE COEFFICIENTS TO BE ADDDED
Do: e_1 + -3e_2 + 2e_3
Do not: e_1 - 3e_2 + 2e_3
"""


class Octonian:
    # Expects number written in summation form, sanitized. For example: 3e_1 + 5e_2
    def __init__(self, num='0'):
        """
        Parameters
        ----------
        num : STR, optional
            DESCRIPTION. Flags if the Octonian is left blank, intializes object
            as the number 0 if left blank. Otherwise, expected input is an
            octonian of form "ae_0 + be_1 + ... + ge_7" where a through g are
            numbers (floats or integers).

        Returns
        -------
        None.

        """
        # Extracting the data from input string
        self.number = {
            'e_0': 0,
            'e_1': 0,
            'e_2': 0,
            'e_3': 0,
            'e_4': 0,
            'e_5': 0,
            'e_6': 0,
            'e_7': 0
        }
        self.norm = 0
        # Checking if number is 0
        if num == '0':
            return
        # Turning expected input into dictionary
        num_split = [term.strip() for term in num.split('+')]

        # Turning into tuple pairs (coefficient, basis element)
        num_tuple = []
        for term in num_split:
            # Dealing with missing leading coefficient (e_i = 1e_i)
            if term[0] == 'e':
                num_tuple.append((1, term))
            else:
                num_tuple.append(
                    (float(term[:term.index('e')]), term[term.index('e'):]))

        # Inserting to self.number
        for pair in num_tuple:
            curr = self.number.get(pair[1])
            self.number.update({pair[1]: curr + float(pair[0])})

        # Creating norm
        self.norm = Decimal(sqrt(self.__mul__(self.conj()).number.get('e_0')))
        return

    def __str__(self):
        """
        Returns octonian as a string of form "ae_0 + be_1 + ..."
        """
        output = ""
        hits = 0
        for basis, coef in self.number.items():
            # Skipping printing 0s
            if coef == 0:
                continue

            hits += 1
            # If not the first non-zero term, insert +
            if hits != 1:
                output += " + "

            # Removing '.0' from coefficients, if applicable
            if coef.is_integer():
                output += str(int(coef))
            else:
                output += str(coef)

            output += basis
        # endfor
        # Checking if octonian is 0
        if output == "":
            return "0"
        else:
            return output

    def __add__(self, other):
        """
        Adds two octonian instances.
        Returns resulting octonian object.
        """
        output = Octonian()
        for basis in output.number.keys():
            output.number.update(
                {basis: self.number.get(basis) + other.number.get(basis)})
        return output

    def __sub__(self, other):
        """
        Subtracts two octonian instances, other from self.
        Returns resulting octonian object.
        """
        output = Octonian()
        for basis in output.number.keys():
            output.number.update(
                {basis: self.number.get(basis) - other.number.get(basis)})
        return output

    def __mul__(self, other):
        """
        Multiplies two octonian instances, self and other.
        Returns resulting octonian object.
        """
        # Helper function, multipication of basis elements. String input.
        def basis_mult(e_i, e_j):
            basis_mult_lookup = array([
                ["e_0", "e_1", "e_2", "e_3", "e_4", "e_5", "e_6", "e_7"],
                ["e_1", "-e_0", "e_3", "-e_2", "e_5", "-e_4", "-e_7", "e_6"],
                ["e_2", "-e_3", "-e_0", "e_1", "e_6", "e_7", "-e_4", "-e_5"],
                ["e_3", "e_2", "-e_1", "-e_0", "e_7", "-e_6", "e_5", "e_4"],
                ["e_4", "-e_5", "-e_6", "-e_7", "-e_0", "e_1", "e_2", "e_3"],
                ["e_5", "e_4", "-e_7", "e_6", "-e_1", "-e_0", "-e_3", "e_2"],
                ["e_6", "e_7", "e_4", "-e_5", "-e_2", "e_3", "-e_0", "-e_1"],
                ["e_7", "-e_6", "e_5", "e_4", "-e_3", "-e_2", "e_1", "-e_0"]])
            return basis_mult_lookup[int(e_i[-1])][int(e_j[-1])]

        # Computing the product
        output = Octonian()
        for e_i, a in self.number.items():
            for e_j, b in other.number.items():
                # Finding product of basis elements
                if basis_mult(e_i, e_j)[0] == '-':
                    curr_basis = (basis_mult(e_i, e_j)[1::], -1)
                else:
                    curr_basis = (basis_mult(e_i, e_j), 1)
                # Fetching the current value for output octonian basis elem
                curr_value = output.number.get(curr_basis[0])
                # Adding product of a and b to current value
                output.number.update(
                    {curr_basis[0]: curr_value + curr_basis[1] * a * b})
        return output

    def __truediv__(self, other):
        """
        Divides self by other, defined as self times other's inverse.
        Returns resulting octonian object.
        """
        if other.number.values() == [0, 0, 0, 0, 0, 0, 0]:
            print("ERROR: DIV BY 0")
            return
        else:
            return self.__mul__(other.invert())

    def conj(self):
        """
        Returns involution of self as octonian object.
        """
        output = Octonian()
        for basis, coef in self.number.items():
            # Skipping initial term
            if basis == 'e_0':
                output.number.update({basis: coef})
            else:
                output.number.update({basis: coef * -1})
        return output

    def invert(self):
        """
        Returns inverse of self as octonian object.
        """
        return self.conj().__mul__(
            Octonian(str(Decimal(1 / Decimal((self.norm)**2))) + 'e_0'))


# Function for generating random octonians with floats, useful for testing.
def random_octonian():
    values = random.rand(1, 8)
    # Making the string
    output = str(values[0][0]) + "e_0"
    for i in range(1, 8):
        output += ' + ' + str(values[0][i]) + 'e_' + str(i)
    return output


# Function for generating random octonians with integers, useful for testing.
def random_octonian_int():
    values = random.randint(-100, 100, 8)
    # Making the string
    output = str(values[0]) + "e_0"
    for i in range(1, 8):
        output += ' + ' + str(values[i]) + 'e_' + str(i)
    return output
