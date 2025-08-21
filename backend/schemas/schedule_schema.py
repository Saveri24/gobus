# backend/schemas/schedule_schema.py
from marshmallow import Schema, fields, validate
import datetime

class ScheduleSchema(Schema):
    id = fields.Int(dump_only=True)
    bus_id = fields.Int(required=True)
    source = fields.Str(required=True)
    destination = fields.Str(required=True)
    departure_datetime = fields.DateTime(required=True)
    price = fields.Float(required=True, validate=validate.Range(min=0))
