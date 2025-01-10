from flask import Blueprint, request, jsonify

# Define a Blueprint for routes
routes = Blueprint('routes', __name__)

# In-memory storage for cell data
grid_data = {}

@routes.route('/cells', methods=['GET'])
def get_cells():
    return jsonify(grid_data), 200

@routes.route('/cells', methods=['POST'])
def update_cell():
    data = request.json
    cell_id = data.get('cell_id')  # e.g., "A1"
    value = data.get('value')
    if not cell_id:
        return jsonify({"error": "Cell ID is required"}), 400
    grid_data[cell_id] = value
    return jsonify({"message": "Cell updated", "cell_id": cell_id, "value": value}), 200

@routes.route('/functions', methods=['POST'])
def execute_function():
    data = request.json
    func_name = data.get('function')  # e.g., "SUM"
    range_cells = data.get('range')  # e.g., ["A1", "A2", "A3"]
    if func_name == "SUM":
        result = sum(grid_data.get(cell, 0) for cell in range_cells)
        return jsonify({"function": func_name, "result": result}), 200
    return jsonify({"error": "Function not implemented"}), 400
