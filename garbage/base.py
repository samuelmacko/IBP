

class TypeBase(object):

    def __init__(self, connection):
        self.service = connection.system_service()
