

class Comparison(object):

    def __init__(self, operand):
        self.operand = operand

    def __lt__(self, other):
        if self.operand is None:
            return True
        elif other.operand is None:
            return False
        else:
            if self.is_float(value=self.operand):
                return self.is_float(value=self.operand)\
                       < self.is_float(value=other.operand)
            elif self.is_int(value=self.operand):
                return self.is_int(value=self.operand)\
                       < self.is_int(value=other.operand)
            else:
                return self.operand < other.operand

    def is_float(self, value):
        split_value = value.split(' ')
        if split_value:
            try:
                float_value = float(split_value[0])
                return float_value
            except ValueError:
                return False
        else:
            return False

    def is_int(self, value):
        split_value = value.split(' ')
        if split_value:
            try:
                int_value = int(split_value[0])
                return int_value
            except ValueError:
                return False
        else:
            return False
