import os
from dotenv import load_dotenv
load_dotenv()


print(os.environ.get('ENV_VAR'))
