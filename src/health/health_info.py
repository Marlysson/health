class HealthInfo:
    def __init__(self):
        self.data = {}
        self.summary = None
        self.name = None
        self.group = None

    def add(self, attribute, value):
        self.data[attribute] = value
