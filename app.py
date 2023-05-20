import os
from src import create_app


if __name__ == '__main__':
    # Create the app
    create_app(os.getenv('APP_ENV') or 'default')
