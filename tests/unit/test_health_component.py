from masonite.tests import TestCase
from src.health.health_result import HealthResult
from src.health.components.database_component import DatabaseComponent
from src.health.status.health_ok import StatusOk


class TestMasoniteHealth(TestCase):
    def test_database_component(self):

        health = DatabaseComponent()
        health.meta("name", "production")
        health.meta("group", "infrastructure")

        result = health.check()

        self.assertIsInstance(result, HealthResult)
        self.assertIsInstance(result.status, StatusOk)
