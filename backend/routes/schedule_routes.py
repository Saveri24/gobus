from flask import Blueprint, jsonify, request
from backend.models.schedule import Schedule
from backend.extensions import db
from backend.schemas.schedule_schema import ScheduleSchema
import datetime

schedule_bp = Blueprint('schedule_bp', __name__, url_prefix='/schedules', strict_slashes=False)
schedule_schema = ScheduleSchema()
schedules_schema = ScheduleSchema(many=True)

@schedule_bp.route("/", methods=['GET', 'POST'])
def get_schedules():
    if request.method == 'GET':
        schedules = Schedule.query.all()
        result = [{
            "id": s.id,
            "bus_id": s.bus_id,
        "source": s.source,
        "destination": s.destination,
        "departure_datetime": s.departure_datetime.isoformat(),
        "price": s.price
        } for s in schedules]
        return jsonify(result)
    elif request.method == 'POST':
        data = request.get_json()
        departure_str = data.get("departure_datetime")
        departure_dt = datetime.datetime.fromisoformat(departure_str)
        errors = schedule_schema.validate(data)
        if errors:
            return jsonify({"errors": errors}), 400
        new_schedule = Schedule(
            bus_id=data.get("bus_id"),
            source=data.get("source"),
            destination=data.get("destination"),
            departure_datetime=departure_dt,
            price=data.get("price")
        )
        db.session.add(new_schedule)
        db.session.commit()
        return jsonify({"message": "Schedule created successfully", "id": new_schedule.id}), 201


@schedule_bp.route("/<int:schedule_id>", methods=['GET', 'PUT', 'DELETE'])
def get_schedule(schedule_id):
    
    schedule = Schedule.query.get_or_404(schedule_id)
    if request.method == 'GET':
        result = {
            "id": schedule.id,
            "bus_id": schedule.bus_id,
            "source": schedule.source,
            "destination": schedule.destination,
            "departure_datetime": schedule.departure_datetime.isoformat(),
            "price": schedule.price
        }
        return jsonify(result)
    elif request.method == 'PUT':
        data = request.get_json()
        schedule.bus_id = data.get("bus_id", schedule.bus_id)
        schedule.source = data.get("source", schedule.source)
        schedule.destination = data.get("destination", schedule.destination)
        schedule.departure_datetime = data.get("departure_datetime", schedule.departure_datetime)
        schedule.price = data.get("price", schedule.price)
        db.session.commit()
        return jsonify({"message": "Schedule updated successfully"})
    elif request.method == 'DELETE':
        db.session.delete(schedule)
        db.session.commit()
        return jsonify({"message": "Schedule deleted successfully"})
