


class HighBase(object):

    def __init__(self, connection):
        self._connection = connection
        self.col_flags = []
        self.row_flags = []
        self.data_list = None
        self.headers_list = None
        self.current_data_list = self.data_list
        self.construct_table()

    def construct_table(self):
        raise NotImplementedError

    def validate_filter(self, filter):
        raise NotImplementedError