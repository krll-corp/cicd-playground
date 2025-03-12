from flask import Flask

app = Flask(__name__)

def run():
    return "works"

def run2(a, b):
    return a + b

@app.route("/")
def index():
    return run()

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)