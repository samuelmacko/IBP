from back.high.bases.base import HighBase
from back.suplementary.filter_restrictions import FilterRestrictions


class Networks(HighBase):

    def __init__(self, connection, build_classes, col_flags=None):
        super(Networks, self).__init__(
            connection=connection, build_classes=build_classes
        )
        if col_flags:
            self.col_flags = col_flags
        else:
            self.col_flags = [1, 1, 1, 1, 1, 1, 1, 1]
        self.filter_restrictions = FilterRestrictions(
            str_col=[],
            float_col=[]
        )
