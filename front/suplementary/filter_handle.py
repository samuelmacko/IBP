

import operator
import re
from back.suplementary.custom_comparsion import Comparison


class FilterHandler(object):

    def __init__(self, table, filter_restrictions):
        self.table = table
        self.filter_regex = r'\s*(\w+[A-Za-z\.\s]+\w+)\s*(>|<|=)\s*(\S+)\s*'
        self.filter_restrictions = filter_restrictions

    def process_filter(self, text):

        class Filter(object):

            def __init__(self, column, operand, value):
                self.column = column
                self.operand = operand
                self.value = value

        match = re.match(self.filter_regex, text, re.I)

        if match:
            attribute = match.group(1)
            operand = match.group(2)
            value = match.group(3)

            attribute_column = None
            for i, header in enumerate(self.table.headers_list):
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
                    if int(filter.value) != len(row[filter.column]):
                        self.table.row_flags[i] = 0
                    continue
                except ValueError:
                    pass

            if operation is operator.eq:

                if isinstance(row[filter.column], list):
                    found = False
                    for n, cell_row in enumerate(row[filter.column]):
                        match = re.match(filter.value, cell_row, re.I)
                        if match and match.group() == cell_row:
                            found = True

                            tmp = row[filter.column][0]
                            row[filter.column][0] = row[filter.column][n]
                            row[filter.column][n] = tmp

                            break

                    if not found:
                        self.table.row_flags[i] = 0

                else:
                    if filter.value and row[filter.column]:
                        match = re.match(
                            filter.value, row[filter.column], re.I
                        )
                        if match is None \
                                or match.group() != row[filter.column]:
                            self.table.row_flags[i] = 0
                    else:
                        self.table.row_flags[i] = 0

            elif operation(
                    Comparison(row[filter.column]), Comparison(filter.value)
            ) is False:
                self.table.row_flags[i] = 0
