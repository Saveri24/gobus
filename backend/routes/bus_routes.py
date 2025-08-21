from flask import Blueprint, jsonify, request
from backend.models.bus import Bus
from backend.extensions import db
from backend.schemas.bus_schema import BusSchema

bus_bp = Blueprint('bus_bp', __name__, url_prefix='/buses')
bus_schema = BusSchema()
buses_schema = BusSchema(many=True)

@bus_bp.route("/", methods=['GET', 'POST'])
def get_buses():
    if request.method == 'GET':
        buses = Bus.query.all()
        result = [{"id": b.id, "bus_name": b.bus_name, "total_seats": b.total_seats} for b in buses]
        return jsonify(result)
    elif request.method == 'POST':
        data = request.get_json()
        errors = bus_schema.validate(data)
        if errors:
            return jsonify({"errors": errors}), 400
        new_bus = Bus(
            bus_name=data.get("bus_name"),
            total_seats=data.get("total_seats")
        )
        db.session.add(new_bus)
        db.session.commit()
        return jsonify({"message": "Bus created successfully", "id": new_bus.id}), 201



@bus_bp.route("/<int:bus_id>", methods=['GET', 'PUT', 'DELETE'])
def bus_detail(bus_id):
    bus = Bus.query.get_or_404(bus_id)
    if request.method == 'GET':
        result = {"id": bus.id, "bus_name": bus.bus_name, "total_seats": bus.total_seats}
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.get_json()
        bus.bus_name = data.get("bus_name", bus.bus_name)
        bus.total_seats = data.get("total_seats", bus.total_seats)
        db.session.commit()
        return jsonify({"message": "Bus updated successfully"})
    elif request.method == 'DELETE':
        db.session.delete(bus)
        db.session.commit()
        return jsonify({"message": "Bus deleted successfully"})