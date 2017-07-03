class AppState(object):
    def __init__(self):
        self.app_tog = False

    @property
    def app_tog(self):
        return self.app_tog

    @app_tog.setter
    def app_tog(self, value):
        self.app_tog = value

    @app_tog.getter
    def app_tog(self): self.app_tog

    @app_tog.deleter
    def app_tog(self):
        self.app_tog = False
