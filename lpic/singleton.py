# -*- coding: utf-8 -*-


class Singleton:
    """Singleton Class
    This is a class to make some class being a Singleton class.
    Such as database class or config class.
    usage:
        class xxx(Singleton):
            def __init__(self):
                if hasattr(self, '_init'):
                    return
                self._init = True
                other init method
    """

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            orig = super(Singleton, cls)
            # noinspection PyArgumentList
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance
