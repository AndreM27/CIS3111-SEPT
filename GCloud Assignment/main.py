from flask import Flask, jsonify, render_template
import random
import socket
from google.cloud.sql.connector import Connector
import sqlalchemy
gce_name = socket.gethostname()
app = Flask(__name__)

# initialize parameters
INSTANCE_CONNECTION_NAME = "cis3111-2023-september:europe-west1:db-instance" # i.e demo-project:us-central1:demo-instance
print(f"Your instance connection name is: {INSTANCE_CONNECTION_NAME}")
DB_USER = "user"
DB_PASS = "pass"
DB_NAME = "pass"
    
def generate_random_numbers(count):
    return [random.randint(0, 100000) for _ in range(count)]
    
def find_largest(numbers):
    largest = max(numbers)
    finMAX = "instance "+gce_name+" generated the largest number :"+str(largest)
    return finMAX
    
def find_smallest(numbers):
    smallest = min(numbers)
    finMIN = "instance "+gce_name+" generated the smallest number :"+str(smallest)
    return finMIN

@app.route('/get_largest_smallest', methods=['GET'])  
def get_largest_smallest():
    random_numbers = generate_random_numbers(15000)
    #lastRet = find_largest_and_smallest(random_numbers)
    #return jsonify({lastRet})
    largest = find_largest(random_numbers)
    smallest = find_smallest(random_numbers)
    numberslen = "numbers generated: "+str(len(random_numbers))
    return value(largest,smallest,numberslen)

@app.route('/')
def home():
    return render_template("/index.html")
  
@app.route('/<large>/<small>/<leng>')   
def value(large, small, leng):
    return render_template("/index.html", large=large, small=small, leng=leng)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
