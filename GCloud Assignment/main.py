from flask import Flask, jsonify
import random
import socket
gce_name = socket.gethostname()
app = Flask(__name__)


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
    return jsonify({'largest': largest, 'smallest': smallest, 'instance': gce_name, 'numbers generated': len(random_numbers)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
