
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Telegram bot loyihasi ishlayapti!</h1>
    <p>Keyingi bosqichda rozilik bilan surat olish sahifasini sozlaymiz.</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
