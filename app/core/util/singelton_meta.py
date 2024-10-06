class SingletonMeta(type):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonMeta, cls).__new__(cls, *args, **kwargs)
            cls._instance.__initialized = False
        return cls._instance
