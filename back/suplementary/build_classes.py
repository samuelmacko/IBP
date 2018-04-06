

class BuildClasses(object):

    def __init__(self, entity_class, list_class):
        self._entity_class = entity_class
        self._list_class = list_class

    @property
    def entity_class(self):
        return self._entity_class

    @property
    def list_class(self):
        return self._list_class
