from flask import Flask, request, jsonify

app = Flask(__name__)

todos = []


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200


@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.json.get('todo')
    todos.append(todo)
    return jsonify({'message': 'Todo added!'}), 201


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

