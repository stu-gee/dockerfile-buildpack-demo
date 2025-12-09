import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    theme_color = "#2D5A27"  # Forest Green
    message = "Happy Holidays! 🎄"
    
    return render_template("index.html", color=theme_color, msg=message)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))