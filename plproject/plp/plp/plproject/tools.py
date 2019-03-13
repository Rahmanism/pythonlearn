# Maybe some useful methods will be here!


def safe_cast(val, to_type, default=None):
    """
    To cast data to a new type using
    a default value if it failed.
    """
    try:
        return to_type(val)
    except (ValueError, TypeError):
        return default
