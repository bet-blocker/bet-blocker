from app.__init__ import AppConfig
from app.__init__ import AppInitializer

if __name__ == "__main__":
    config = AppConfig()
    app = AppInitializer(config)
    app.run()