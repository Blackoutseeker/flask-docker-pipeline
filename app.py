from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({"mensagem: ": "Bem-vindo ao API FastOrder!"})


@app.route('/api/status')
def status():
    return jsonify({"status: ": "operacional", "servico": "FastOrder-Web"})


@app.route('/api/soma')
def soma():
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        resultado = a + b

        # Formata para inteiro se não houver casas decimais
        if resultado.is_integer():
            resultado = int(resultado)

        return jsonify({"Resultado: ": resultado})
    except ValueError:
        return jsonify({"Erro: ": "Parâmetros inválidos."}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
