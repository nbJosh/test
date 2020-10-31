

class main:
    def __init__(self, config = None):
        self._config = config
        print("main init")

    def run(self, config = None):
        print("Running!")
        print(config)
        print(self._config)