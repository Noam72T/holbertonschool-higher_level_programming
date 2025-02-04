def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.
    
    Args:
        obj: The object to inspect.
    
    Returns:
        list: A list of attributes and methods of the object.
    """
    return dir(obj)
