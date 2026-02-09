try:
    import crispy_forms  # noqa
    _is_crispy = True
except ImportError:
    _is_crispy = False


def is_crispy():
    return _is_crispy
