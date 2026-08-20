
from flask import Flask

app = Flask(__name__)

from flask import request, jsonify, Flask

sons = []


sons_id_control = 1

@app.route("/sons", methods=['POST'])
def createSon():
    global sons_id_control
    data = request.get_json()

    new_son = {
        "id": sons_id_control,
        "name": data.get("name"),
        "tasks": [
            {
                "nameTask": task.get("nameTask"),
            }
            for task in data.get("tasks", [])
        ]
    }

    sons.append(new_son)
    sons_id_control += 1

    return jsonify({"message": "Seu filho está registrado", "Filhos": new_son})

@app.route("/sons", methods = ['GET'])
def getSons() :
    return jsonify ({"sons" : sons})


@app.route("/sons/<int:son_id>", methods=["GET"])
def get_son(son_id):
    son = next((s for s in sons if s["id"] == son_id), None)
    if not son:
        return jsonify({"message": "Filho não encontrado"}), 404
    return jsonify(son)






if __name__ == "__main__":
    app.run(debug=True)