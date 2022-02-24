
from masonite.configuration import config

from ..health_status import HealthStatus
from ..health_result import HealthResult
from .base_component import BaseComponent

class DatabaseComponent(BaseComponent):

    """
        - Run logic to retrieve status of component
        - Add specific attributes based in resultant status
        - Add summary information 

    """

    def __init__(self, connection=None):
        super().__init__()
        self.connection = connection

    def check(self) -> HealthResult:

        connection = self.connection or config("database.databases.default")

        try:
            
            resolver = self.application.make("resolver")    
            resolver.statement("select 1", connection=connection)

            return HealthResult(self.meta_health, HealthStatus.ok())

        except Exception as error:
            self.meta("reason", str(error))
            return HealthResult(self.meta_health, HealthStatus.down())







        





    