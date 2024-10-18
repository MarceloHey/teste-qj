from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():

        return jsonify({'message': 'Usuário autenticado com sucesso!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)