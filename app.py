from flask import Flask
from views import views
import psycopg2

app = Flask(__name__)
app.config['db_name'] = 'df7ukr03n4uvr'
app.config['db_username'] = 'yckaqakixspkxi'
app.config['db_password'] = '2f5a7d3740c77bacd30ff267e57d65a65bd3d68b9af6f807601d19c5243736c5'
app.config['db_host'] = 'ec2-54-77-40-202.eu-west-1.compute.amazonaws.com'

app.register_blueprint(views)

if __name__ == "__main__":
    app.run(debug=True, port=8000)