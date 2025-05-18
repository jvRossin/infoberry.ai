import os
from dotenv import load_dotenv

load_dotenv()
banco_dados = os.getenv("SQL_API_KEY")