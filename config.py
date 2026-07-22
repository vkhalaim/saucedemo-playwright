import os
from dotenv import load_dotenv

load_dotenv()

USERNAME = os.environ["SAUCE_USERNAME"]
PASSWORD = os.environ["SAUCE_PASSWORD"]
USERNAME_LOCKED_OUT = os.environ["SAUCE_USERNAME_LOCKED_OUT"]
