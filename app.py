from flask import Flask
from views import views
import psycopg2

app = Flask(__name__)
app.config['db_name'] = 'flask'
app.config['db_username'] = 'postgres'
app.config['db_password'] = 'password'
app.config['db_host'] = 'localhost'

app.register_blueprint(views)

if __name__ == "__main__":
    app.run(debug=True, port=8000)