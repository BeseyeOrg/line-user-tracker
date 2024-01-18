from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/test')
def test():
    return jsonify({"Savelyn": "flask test"})

@app.route('/test2')
def test2():
    return jsonify({"Savelyn": "flask test2"})



if __name__ == '__main__':
    app.run(debug=True, port=5001)