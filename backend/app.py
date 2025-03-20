from flask import Flask, jsonify, request
from flask_cors import CORS
import produto_service as ProdutoService

app = Flask(__name__)
CORS(app)


@app.route('/produtos', methods=['GET'])
def listarProduto():
  return jsonify(ProdutoService.listar())


@app.route('/produtos/<id>', methods=['GET'])
def buscarProduto(id):
  return jsonify(ProdutoService.buscar(id))


@app.route('/produtos', methods=['POST'])
def adicionarProduto():
  data = request.get_json()

  return jsonify(ProdutoService.adicionar(data))


@app.route('/produtos', methods=['PATCH'])
def editarProduto():
  data = request.get_json()

  return jsonify(ProdutoService.editar(data))


@app.route('/produtos/<id>', methods=['DELETE'])
def excluirProduto(id):
  return jsonify(ProdutoService.excluir(id))


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
