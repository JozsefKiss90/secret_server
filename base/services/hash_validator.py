import uuid

def is_valid_uuid(hash_str):
    try:
        hash_str = str(hash_str)
        uuid.UUID(hash_str)
        return True
    except ValueError:
        return False

