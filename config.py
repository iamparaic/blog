import os

# For a production app, you should use a secret key set in the environment
# The recommended way to generate a 64char secret key is to run:
# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

# When deploying, set in the environment to the PostgreSQL URL
SQLALCHEMY_DATABASE_URI = os.getenv('postgresql://paraic:rNYLVX9G830WcU756ixqzlHeoyJCn7N4@dpg-crsk4k68ii6s73ee7lm0-a/blog_e6gg')
if SQLALCHEMY_DATABASE_URI is None:
    raise ValueError("DATABASE_URL is not set")
# When you use Flask's default settings, the application looks for the instance folder to store files
# that should persist across different runs of the application, but are specific to the instance (like your SQLite database).
