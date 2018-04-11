import operator
import re

from back.suplementary.custom_comparsion import Comparison


class FilterHandler(object):

    def __init__(self, table, filter_restrictions):
        self.table = table
        # self.filter_regex = r'\s*(w+|\w+\s{0,1}\w+)\s*(>|<|=)\s*(\S+)\s*'
        self.filter_regex = r'\s*(\w+[A-Za-z\.\s]+\w+)\s*(>|<|=)\s*(\S+)\s*'
        self.filter_restrictions = filter_restrictions

    def process_filter(self, text):

        class Filter(object):

            def __init__(self, column, operand, value):
                self.column = column
                self.operand = operand
                self.value = value

        # filter_regex = r'\s*(\S+)\s*(>|<|=)\s*(\S+)\s*'
        # filter_regex = r'\s*(w+|\w+\s{0,1}\w+)\s*(>|<|=)\s*(\S+)\s*'
        match = re.match(self.filter_regex, text, re.I)
        #
        # print('1:', match.group(1))
        # print('2:', match.group(2))
        # print('3:', match.group(3))

        if match:
            attribute = match.group(1)
            # operand = ops[match.group(2)]
            operand = match.group(2)
            value = match.group(3)

            attribute_column = None
            for i, header in enumerate(self.table.headers_list):
                # print(header)
                if attribute.lower() == header.lower():
                    attribute_column = i
                    break

            if attribute_column is not None:
                filter = Filter(
                    column=attribute_column, operand=operand, value=value
                )
                return filter
            else:
                return None
        else:
            return None

    def apply_filter(self, filter):

        operators = {'>': operator.gt, '<': operator.lt, '=': operator.eq}
        operation = operators[filter.operand]

        for i, row in enumerate(self.table.data_list):

            if filter.column in self.filter_restrictions:
                try:
                    # int_val = int(filter.value)
                    if int(filter.value) != len(row[filter.column]):
                        self.table.row_flags[i] = 0
                    continue
                except ValueError:
                    pass



            if operation is operator.eq:

                if isinstance(row[filter.column], list):
                    found = False
                    for cell_row in row[filter.column]:
                        match = re.match(filter.value, cell_row, re.I)
                        if match and match.group() == cell_row:
                            found = True

                    if not found:
                        self.table.row_flags[i] = 0

                else:
                    match = re.match(filter.value, row[filter.column], re.I)
                    if match is None or match.group() != row[filter.column]:
                        self.table.row_flags[i] = 0

            elif operation(
                    Comparison(row[filter.column]), Comparison(filter.value)
            ) is False:
                self.table.row_flags[i] = 0
