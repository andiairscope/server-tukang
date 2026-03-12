from flask import Flask, request

app = Flask(__name__)

# Ini rute buat ngecek server lu idup atau nggak
@app.route('/', methods=['GET'])
def home():
    return "Server Marketplace Tukang is LIVE! 🚀"

# Ini rute webhook yang nanti dihubungin ke WhatsApp
@app.route('/wa-webhook', methods=['POST'])
def whatsapp_bot():
    data = request.json
    print("Ada pesan masuk dari user:", data)
    # Nanti logic matching tukang dan balesan chat ditaruh di sini
    return "OK", 200

if __name__ == '__main__':
    app.run(port=5000)