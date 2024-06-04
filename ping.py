from flask import Flask

app = Flask('ping')

@app.route('/ping', methods=['GET']) # flask decorator: when send a GET request to the address '/ping', execute the python function ("endpoint")
def ping(): # usual python function
    return 'PONG' # just reply with 'PONG'

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=9696)