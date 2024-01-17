from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulatie van een kleine database als een Python dictionary
users = {
    '1': {'name': 'John Doe', 'age': 30},
    '2': {'name': 'Jane Doe', 'age': 25}
}

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    """
    Een eenvoudige API endpoint om gebruikersdata op te halen op basis van user_id.
    """
    user = users.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user)

@app.route('/users', methods=['POST'])
def create_user():
    """
    Een API endpoint om een nieuwe gebruiker te creëren.
    De gebruikersdata wordt verwacht als JSON in de body van het verzoek.
    """
    user_data = request.json
    if not user_data or 'name' not in user_data or 'age' not in user_data:
        return jsonify({'error': 'Bad Request, name and age are required'}), 400

    new_id = str(max([int(k) for k in users.keys()]) + 1)
    users[new_id] = user_data
    return jsonify({new_id: user_data}), 201

# Dit is nodig om de Flask applicatie te starten als je dit script direct uitvoert.
if __name__ == '__main__':
    app.run(debug=True)
