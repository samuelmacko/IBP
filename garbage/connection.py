import ovirtsdk4 as sdk


class Connection(object):

    def __init__(
            self, username=None, password=None, insecure=False,
            url='https://10-37-137-222.rhev.lab.eng.brq.redhat.com/ovirt-engine/api',
            ca_file=None
    ):
        self.connection = sdk.Connection(
            username=username, password=password, url=url,
            # ca_file=ca_file,
            insecure=insecure,
        )

    def close_connection(self):
        self.connection.close()
