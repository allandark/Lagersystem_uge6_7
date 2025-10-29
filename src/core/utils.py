from werkzeug.security import generate_password_hash, check_password_hash

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


def TupleToAdmin(tuple):
    return {
        "id": tuple[0],
        "name": tuple[1],
        "password_hash": tuple[1]
    }



def create_admin_user(
    db_manager, 
    name = "admin", 
    password="password"):
    """Create an admin user if no users are stored on database

    Args:
        db_manager ([type]): instance of database interface
        name (str, optional): Admin username. Defaults to "admin".
        password (str, optional): Admin passowrd. Defaults to "password".

    Returns:
        bool: True if an admin user is created, false if not
    """

    # Do not create admin:
    # If any users is on db 
    user_list = db_manager.admin.GetAll()    
    if len(user_list) > 0:
        return False

    # Create new user 
    db_manager.admin.Insert(
        name=name,
        password_hash=generate_password_hash(password)
    )    

    return True


