import sys

# TODO: This is bad! Need to figure out how to set deps reliably...
sys.path.append("C:\\Users\\Ben\\Documents\\Projects\\hberg-directory-api\\deps")
from flask_api import FlaskAPI

app = FlaskAPI(__name__)

@app.route('/example/<int:key>/<string:name>', methods=['GET'])
def example(key, name):
    return {
        'hello': name,
        'age': key
    }

if __name__ == "__main__":
    app.run(debug=True)