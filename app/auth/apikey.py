import secrets

def create_api_key():
    return secrets.token_hex(24)

