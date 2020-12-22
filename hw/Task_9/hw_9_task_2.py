from contextlib import contextmanager


class ContextCls:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        return issubclass(exc_type, self.exception)


@contextmanager
def context_gen(exception):
    try:
        yield
    except exception:
        pass
