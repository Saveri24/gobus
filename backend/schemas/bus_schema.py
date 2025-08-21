# backend/schemas/bus_schema.py
from marshmallow import Schema, fields, validate

class BusSchema(Schema):
    id = fields.Int(dump_only=True)
    bus_name = fields.Str(required=True, validate=validate.Length(min=1))
    total_seats = fields.Int(required=True, validate=validate.Range(min=1))
