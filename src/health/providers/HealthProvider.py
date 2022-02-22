"""A HealthProvider Service Provider."""

from masonite.packages import PackageProvider


class HealthProvider(PackageProvider):

    def configure(self):
        """Register objects into the Service Container."""
        (
            self.root("health")
            .name("health")
            .config("config/health.py", publish=True)
        )

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
