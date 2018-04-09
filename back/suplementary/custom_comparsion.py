

class Comparison(object):

    def __init__(self, operand):
        if operand:
            if isinstance(operand, list):
                self.operand = operand[0].lower()
            else:
                self.operand = operand.lower()
        else:
            self.operand = operand

    def __lt__(self, other):
        if self.operand is None:
            return True
        elif other.operand is None:
            return False
        elif to_number(value=self.operand):
            print(
                float(to_number(value=self.operand)), '<',
                float(to_number(value=other.operand)), '=',
                float(to_number(value=self.operand)) \
                < float(to_number(value=other.operand))
                  )
            return \
                float(to_number(value=self.operand))\
                < float(to_number(value=other.operand))
            # print(
            #     int(to_number(value=self.operand)), '<',
            #     int(to_number(value=other.operand)), '=',
            #     int(to_number(value=self.operand)) \
            #     < int(to_number(value=other.operand))
            # )
            # return \
            #     int(to_number(value=self.operand)) \
            #     < int(to_number(value=other.operand))
        else:
            print('eeeellssseee: lt', self.operand, other.operand)
            return self.operand < other.operand

    def __gt__(self, other):
        if self.operand is None:
            return False
        elif other.operand is None:
            return True
        elif to_number(value=self.operand):
            print('gggttt')
            print(
                float(to_number(value=self.operand)), '>',
                float(to_number(value=other.operand)), '=',
                float(to_number(value=self.operand)) \
                > float(to_number(value=other.operand))
            )
            # return \
                # to_number(value=self.operand) > to_number(value=other.operand)
            return \
                float(to_number(value=self.operand)) \
                > float(to_number(value=other.operand))
        else:
            print('eeeellssseee: gt', self.operand, other.operand)
            return self.operand > other.operand

    def __eq__(self, other):
        if self.operand is None and other.operand is None:
            return True
        elif self.operand is None:
            return False
        elif other.operand is None:
            return False

        elif isinstance(self.operand, list):
            return any(row.id == other.operand for row in self.operand)
        elif isinstance(other.operand, list):
            return any(row.id == self.operand for row in other.operand)

        elif to_number(value=self.operand):
            return \
                to_number(value=self.operand) == to_number(value=other.operand)
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
        # integer = int(value)
        # # print('int:', integer)
        # return integer
        return int(value)
    except ValueError:
        try:
            if ' ' in value:
                split_value = value.split(' ')
                return float(split_value[0])
            else:
                return float(value)
        except ValueError:
            return False
        # if (' ' in value):
        #     split_value = value.split(' ')
        #     return float(split_value[0])
        # else:
        #     return False