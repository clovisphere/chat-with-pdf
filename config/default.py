import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))


class Config:
    # TITLE = """
    # $\\left(\\Large{Chat with PDF 📃}\\right)$
    # """
    TITLE = """
        $\\left(\\Large{Chat with PDF 📃}\\right)$
        """
    ALLOW_MULTIPLE_FILES = False
    ALLOWED_FILE_EXTENSION = 'pdf'
    EXCERPT_LENGTH = 300
    VERTICAL_SPACING = 2
    NUMBER_OF_RELEVANT_CHUNKS = 2
    CHAIN_TYPE = 'stuff'
    WIDTH = "50"
    HEIGHT = "60"


class DevelopmentConfig(Config):
    pass


config = {
    'default': DevelopmentConfig,
}
