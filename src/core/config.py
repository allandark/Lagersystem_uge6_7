from dataclasses import dataclass
import json

@dataclass
class Config:
    """Class containing config data
    """
    db_name: str
    db_host: str
    db_user: str
    db_password: str
    jwt_token: str
    debug: bool
    swagger_ui: bool
    api_host: str
    api_port: int
    version: str



def ReadConfigFile(filename):
    print(f"Loading config file: {filename}")
    with open(filename) as f:
        try:
            data = json.load(f)
            conf =Config(
                db_name=data['db_name'],
                db_host=data['db_host'],
                db_password=data['db_password'],
                db_user=data['db_user'],
                jwt_token=data['jwt_token'],
                debug=data['debug'],
                swagger_ui=data['swagger_ui'],
                api_host=data['api_host'],
                api_port=data['api_port'],
                version=data['version']
            )

        except Exception as e:
            print(f"Cannot read file \"{filename}\". Exception {e}")            
            conf = None

    return conf