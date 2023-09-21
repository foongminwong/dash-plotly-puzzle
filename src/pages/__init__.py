from dotenv import load_dotenv
import os

load_dotenv('env')

HOME_URL = os.getenv('HOME_URL')
TABLE_URL = os.getenv('TABLE_URL')
DROPDOWN_URL = os.getenv('DROPDOWN_URL')