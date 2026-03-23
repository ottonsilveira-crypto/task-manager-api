from flask import Flask
from routes import task_routes

app = Flask(__name__)

app.register_blueprint(task_routes)

@app.route("/")
def home():
    return {"message": "Task Manager API running"}

if __name__ == "__main__":
    app.run(debug=True)
