def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object
    
    Args:
        obj: The object to check.
        a_class: The class to compare with.
    
    Returns:
        bool: True if obj is an instance of a_class or a subclass, False otherwise.
    """
    return isinstance(obj, a_class)
