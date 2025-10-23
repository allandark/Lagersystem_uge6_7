

def parse_int(id_str):
    """Parses string to integer

    Returns:
        int | None: return the parsed integer or None if exception
    """
    try:
        return int(id_str)
    except Exception:
        return None 

def parse_dict_key(dict, key):
    """Checks if dictionary contains key and returns the value

    Returns:
        str | None: return value of key or None if key does not exist
    """
    try:
        return dict[key]
    except KeyError:
        return None