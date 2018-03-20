

class Comparison(object):

    def __init__(self, operand):
        self.operand = operand

    def __lt__(self, other):
        if self.operand is None:
            return True
        elif other.operand is None:
            return False
        elif to_number(value=self.operand):
            return to_number(value=self.operand) \
                   < to_number(value=other.operand)
        else:
            return self.operand < other.operand

    def __gt__(self, other):
        if self.operand is None:
            return False
        elif other.operand is None:
            return True
        elif to_number(value=self.operand):
            return to_number(value=self.operand) \
                   > to_number(value=other.operand)
        else:
            return self.operand > other.operand

    def __eq__(self, other):
        if self.operand is None and other.operand is None:
            return True
        elif self.operand is None:
            return False
        elif other.operand is None:
            return False
        elif to_number(value=self.operand):
            return to_number(value=self.operand) \
                   == to_number(value=other.operand)
        else:
            return self.operand == other.operand


def to_number(value):
    # split_value = value.split(' ')
    # if split_value:
    #     try:
    #         float_value = float(split_value[0])
    #         return float_value
    #     except ValueError:
    #         return split_value
    # else:
    #     return False

    try:
        integer = int(value)
        return integer
    except ValueError:
        if (' ' in value):
            split_value = value.split(' ')
            return float(split_value[0])
        else:
            return False