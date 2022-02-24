from src.health.status.health_ok import StatusOk
from src.health.status.health_danger import StatusDanger
from src.health.status.health_warn import StatusWarn
from src.health.status.health_down import StatusDown


class HealthStatus:

    @classmethod
    def ok(cls):  
        return StatusOk()

    @classmethod
    def down(cls):
        return StatusDown()

    @classmethod
    def warn(cls):
        return StatusWarn()
    
    @classmethod
    def danger(cls):
        return StatusDanger()