from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
  return "Welcome to APIs"

@app.route("/predict")
def predict():
  return "predict"

@app.route("/sayhi")
def sayhi():
  nama = request.args.get('nama', default = "tayo", type = str)

  return f"Hi! {nama}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
