from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/info', methods=['GET'])
def get_info():
    response = jsonify({
        "festival": "Pacific DevOps Music Fest",
        "artistas": ["Banda Docker", "Los Kubernéticos", "Git Merge Orchestra", "DJ Pipeline"]
    })
    # Agregamos el permiso CORS manualmente para no usar librerías externas
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)