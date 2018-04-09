from back.high.bases.base import HighBase


class NICs(HighBase):

    def __init__(self, connection, build_classes, col_flags=None):
        super(NICs, self).__init__(
            connection=connection, build_classes=build_classes
        )
        if col_flags:
            self.col_flags = col_flags
        else:
            self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1, 1,]
                              # 1, 1, 1, 1, 1, 1, 1, 1]
        self.filter_restrictions = {0, 1, 2, 3, 4, 5, 6, 7, 8}
