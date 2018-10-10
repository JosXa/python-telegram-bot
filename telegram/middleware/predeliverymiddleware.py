import functools


class PreDeliveryMiddleware(object):
    def __init__(self, data):
        self.data = data

    def prepare_data(self):
        return self.data

    def postprocess(self, result):
        pass
