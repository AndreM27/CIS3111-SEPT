from flask import Flask, jsonify, render_template
import random
import socket
from google.cloud.sql.connector import Connector
import sqlalchemy
gce_name = socket.gethostname()
app = Flask(__name__)

#code for connecting to SQL however due to bugs this was not implemented
'''
# initialize parameters
INSTANCE_CONNECTION_NAME = "cis3111-2023-september:europe-west1:db-instance" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "user"
DB_PASS = "pass1234"
DB_NAME = "user"

# initialize Connector object
connector = Connector()

# function to return the database connection object
def getconn():
    conn = connector.connect(
        INSTANCE_CONNECTION_NAME,
        "pg8000",
        user=DB_USER,
        #password=DB_PASS,
        db=DB_NAME
    )
    return conn

#print(getconn())

# create connection pool with 'creator' argument to our connection object function
pool = sqlalchemy.create_engine(
    "postgresql+pg8000://user:pass@34.140.202.145/pass", pool_pre_ping=True
    #creator={INSTANCE_CONNECTION_NAME},
    #creator=getconn,
)
print(pool)

# connect to connection pool
with pool.connect() as db_conn:
  # create storage table in our database
  db_conn.execute(
    sqlalchemy.text(
      "CREATE TABLE IF NOT EXISTS storage "
      "( id SERIAL NOT NULL, instance VARCHAR(255) NOT NULL, "
      "smallest integer NOT NULL, largest integer NOT NULL, "
      "numbers_gen VARCHAR(10485760) NOT NULL, numbers_amt integer NOT NULL, "
      "PRIMARY KEY (id));"
    )
  )
  
  # insert data into our storage table
  insert_stmt = sqlalchemy.text(
      "INSERT INTO storage (instance, smallest, largest, numbers_gen, numbers_amt) VALUES (:instance :smallest :largest :numbers_gen :numbers_amt)",
  )
  
  # query and fetch storage table
  results = db_conn.execute(sqlalchemy.text("SELECT * FROM storage")).fetchall()

  # show results
  for row in results:
    print(row)
    
'''
    
#generates random numbers between 0 and 100,000    
def generate_random_numbers(count):
    return [random.randint(0, 100000) for _ in range(count)]
    
#find the largest number    
def find_largest(numbers):
    largest = max(numbers)
    finMAX = "instance "+gce_name+" generated the largest number :"+str(largest)
    return finMAX

#find the smallest number     
def find_smallest(numbers):
    smallest = min(numbers)
    finMIN = "instance "+gce_name+" generated the smallest number :"+str(smallest)
    return finMIN

#returns largest, smallest and total numbers generated
@app.route('/get_largest_smallest', methods=['GET'])  
def get_largest_smallest():
    random_numbers = generate_random_numbers(15000)
    largest = find_largest(random_numbers)
    smallest = find_smallest(random_numbers)
    numberslen = "numbers generated: "+str(len(random_numbers))
    return value(largest,smallest,numberslen,random_numbers)

@app.route('/')
def home():
    return render_template("/index.html")
  
@app.route('/<large>/<small>/<leng>/<allnum>')   
def value(large, small, leng,allnum):
    return render_template("/index.html", large=large, small=small, leng=leng, allnum=allnum)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
