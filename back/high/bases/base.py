


class HighBase(object):

    def __init__(self, connection):
        self._connection = connection
        self.col_flags = []
        self.row_flags = []
        self.data_list = None
        self.headers_list = None
        self.current_data_list = []
        self.current_headers_list = []
        self.construct_table()

    def construct_table(self):
        raise NotImplementedError

    def validate_filter(self, filter):
        raise NotImplementedError

    def table_from_flags(self):
        # headers = []
        # data = []
        self.current_headers_list = []
        self.current_data_list = []

        for i, flag in enumerate(self.col_flags):
            if flag == 1:
                self.current_headers_list.append(self.headers_list[i])

        for j, row in enumerate(self.data_list):
            if self.row_flags[j]:
                data_row = []
                for i, flag in enumerate(self.col_flags):
                    if flag == 1:
                        data_row.append(row[i])
                self.current_data_list.append(data_row)

        # return headers, data