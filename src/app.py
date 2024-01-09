from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/todos', methods=['GET'])
def hello_world():
    response_body = todos
    return response_body
# @app.route('/todos', methods=['GET'])
# def hello_world():
#     json_text = jsonify(todos)
#     return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    response_body = todos
    return response_body
# @app.route('/todos', methods=['POST'])
# def add_new_todo():
#     request_body = request.json
#     print("Incoming request with the following body", request_body)
#     todos.append(request_body)
#     return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    response_body = todos
    return response_body
# @app.route('/todos/<int:position>', methods=['DELETE']) 
# def delete_todo(position):
#     print("This is the position to delete: ",position)
#     todos.pop((position-1))
#     return jsonify(todos)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)