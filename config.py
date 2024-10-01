import os

# For a production app, you should use a secret key set in the environment
# The recommended way to generate a 64char secret key is to run:
# python -c 'import secrets; print(secrets.token_hex())'
SECRET_KEY = os.getenv('SECRET_KEY', 'not-set')

# When deploying, set in the environment to the PostgreSQL URL
#connection_string = 'postgresql://postgres:ta5tyburg3r@localhost:5432/db1'
connection_string = 'postgresql://paraic:GFXIjfYjzWnikSUQcDARpAD8R6vl2mP2@dpg-cru5d1m8ii6s73air950-a.oregon-postgres.render.com/blog_jclj'
SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', connection_string)

#SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')

