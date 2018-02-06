import re
import operator


class FilterHandle(object):

    def __init__(self, table):
        self.table = table

    def table_from_flags(self):
        headers = []
        data = []

        for i, flag in enumerate(self.table.col_flags):
            if flag == 1:
                headers.append(self.table.headers_list[i])

        for j, row in enumerate(self.table.data_list):
            data_row = []
            for i, flag in enumerate(self.table.col_flags):
                if flag == 1:
                    data_row.append(row[i])
            if self.table.row_flags[j]:
                data.append(data_row)

        return headers, data

    def process_filter(self, text):

        class Filter(object):

            def __init__(self, column, operand, value):
                self.column = column
                self.operand = operand
                self.value = value

        ops = {
            '>': operator.gt, '<': operator.lt, '=': operator.eq}

        filter_regex = r'\s*(\S+)\s*(>|<|=)\s*(\S+)\s*'
        match = re.match(filter_regex, text, re.I)

        if match:
            attribute = match.group(1)
            operand = ops[match.group(2)]
            value = match.group(3)

            attribute_column = None
            for i, header in enumerate(self.table.headers_list):
                # print(header)
                if attribute == header:
                    attribute_column = i
                    break

            if attribute_column is not None:
                filter = Filter(
                    column=attribute_column, operand=operand, value=value)
                return filter
            else:
                return None
        else:
            return None

    def apply_filter(self, filter):
        for i, row in enumerate(self.table.data_list):
            # if filter.operand(row[filter.column], filter.value) is False:
            # if (filter.operand is not operator.eq and
            #         isinstance(filter.value, str)) or \
            #     filter.operand(row[filter.column], filter.value) is False:
            if filter.operand(row[filter.column], filter.value) is False:
                # print('naslo', row[0])
                # del self.current_data_list[i]
                self.table.row_flags[i] = 0