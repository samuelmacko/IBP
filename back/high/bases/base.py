

class HighBase(object):

    def __init__(self, connection, build_classes):
        self._connection = connection
        self.col_flags = []
        self.row_flags = []
        self.data_list = None
        self.headers_list = None
        # self.data_list = []
        # self.headers_list = []
        self.current_data_list = []
        self.current_headers_list = []

        self.build_classes = build_classes
        self.statistics = False

        self.filter_restrictions = None

    def construct_table(self):
        table = []
        header = []
        # print('ent:', len(entity.statistics())) nie tuna
        entity_list = self.build_classes.list_class(
            connection=self._connection).list()

        for n, entity_row in enumerate(entity_list):
            self.row_flags.append(1)
            table_row = []

            entity = self.build_classes.entity_class(
                connection=self._connection, id=entity_row.id
            )

            for method in entity.methods_list():
                cell = method()
                if n == 0:
                    print(cell.name, cell.value)
                    header.append(cell.name)
                table_row.append(cell.value)

            # if self.build_classes.entity_class is Host:
            #     print('aaaaaaa')
            #     continue

            # aaa = entity.statistics()
            # for statistic in aaa:
            if self.statistics:
                for statistic in entity.statistics():
                    if n == 0:
                        header.append(statistic.name)
                    table_row.append(statistic.value)

            table.append(table_row)

        self.data_list = table
        self.headers_list = header

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

    def validate_filter(self, filter):
        if (filter.column in self.filter_restrictions
                and filter.operand == '='):
            # filter.operand is operator.eq and isinstance(filter.value, str):
            return True

        else:
            try:
                float(filter.value)
                return True
            except ValueError:
                return False
