from ..health_info import HealthInfo


class BaseComponent:
    def __init__(self):
        from wsgi import application

        self.application = application
        self.meta_health = HealthInfo()

    def meta(self, name, value):
        self.meta_health.add(name, value)
