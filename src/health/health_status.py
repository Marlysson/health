from src.health.status.ok import Ok
from src.health.status.danger import Danger
from src.health.status.warn import Warn
from src.health.status.down import Down


class HealthStatus:
    @classmethod
    def ok(cls):
        return Ok()

    @classmethod
    def down(cls):
        return Down()

    @classmethod
    def warn(cls):
        return Warn()

    @classmethod
    def danger(cls):
        return Danger()
