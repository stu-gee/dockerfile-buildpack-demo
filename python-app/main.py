import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    theme_color = "#2D5A27"
    deploy_type = os.environ.get("DEPLOY_TYPE", "local")
    message = "Happy Holidays! ☃️"
    
    return render_template("index.html", color=theme_color, msg=message, deploy_type=deploy_type)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))