import psycopg2
from flask import render_template, Blueprint, Flask, request
from flask import current_app as app

views = Blueprint("views", __name__)


def dbconnection():
    conn = psycopg2.connect(host=app.config['db_host'], database=app.config['db_name'], user=app.config['db_username'], password=app.config['db_password'])
    return conn

def dbquery(query):
    conn=dbconnection()
    cur=conn.cursor()
    cur.execute(query)
    results=cur.fetchall()
    print(results)
    cur.close()
    conn.close()
    return results

def getsingleimage(results):
    final = []
    for res in results:
        res=list(res)
        image = dbquery('SELECT image_path, image_name FROM product_images WHERE product_id = ' + str(res[0]) + ' LIMIT 1')
        image = image[0][0] + image[0][1]
        res.append(image)
        print(res)
        final.append(res)
    return final

def getproductadditions(id):
    results = dbquery('SELECT addition, addition_answer FROM product_additions WHERE product_id = ' + str(id))
    results = list(results)
    print(results)
    return results



def getproductimages(id):
    results = dbquery('SELECT image_path, image_name FROM product_images WHERE product_id = ' + str(id))
    results = list(results)
    return results
    
@views.route("/")
def home():
    return render_template("index.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/store")
def store():
    results=dbquery("SELECT * from products WHERE is_product = true")
    final = getsingleimage(results)
    return render_template("store.html", products=final, type="products")

@views.route("/gallery")
def gallery():
    return render_template("gallery.html")

@views.route("/store/accessories")
def storeaccess():
    results=dbquery("SELECT * from products WHERE is_accessory = true")
    final = getsingleimage(results)
    return render_template("store.html", accessories=final, type="accessories")

@views.route("/store/<id>/<title>")
def storeItem(id, title):
    print(id)
    product = dbquery('SELECT id, title, description, price, discount, quantity from products WHERE id = '+ str(id))
    images = getproductimages(product[0][0])
    additions = getproductadditions(product[0][0])
    print(images)
    return render_template("store-item.html", product=product, images=images, additions=additions)
