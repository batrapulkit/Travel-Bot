import os
import yaml
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load YAML configuration
def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

config = load_config()

# Settings Dictionary
SETTINGS = {
    "PROJECT_NAME": config["project"]["name"],
    "VERSION": config["project"]["version"],
    "AUTHOR": config["project"]["author"],
    "LOG_LEVEL": config["logging"]["level"],
    "LOG_FILE": config["logging"]["log_file"],
    "API_SERVICES": config["api_services"],
}
