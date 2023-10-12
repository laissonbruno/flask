from flask import Flask, jsonify, request
import json
app = Flask(__name__)

developers = [
    {'id': 1,
     'nome': 'Laisson',
     'Hard skills': ['Python', 'Flask']
     },
    {'id': 2,
     'nome': 'Lucas',
     'Hard skills': ['Python', 'Pandas']
     },
]


@app.route('/dev/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = developers[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': f'Dev de Id {id} não existe'}
        except Exception:
            response = {'status': 'erro', 'mensagem': 'Erro desconhecido, procure o administrador da aplicação'}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        developers[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        developers.pop(id)
        return jsonify({'status': 'sucess', 'mensagem': 'Registro excluido'})




@app.route('/dev/', method=['POST', 'GET'])
def lista_developers():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(developers)
        dados['id'] = posicao
        developers.append(dados)
        return jsonify(developers[posicao])
    elif request.method == 'GET':
        return jsonify(developers)

if __name__ == '__main__':
    app.run(debug=True)

