"""A HealthProvider Service Provider."""

from masonite.packages import PackageProvider


class HealthProvider(PackageProvider):
    def configure(self):
        self.root("health").name("health").commands()

    def register(self):
        super().register()

    def boot(self):
        """Boots services required by the container."""
        pass
