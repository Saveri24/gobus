from backend.app import create_app
from backend.extensions import db
from backend.models.bus import Bus
from backend.models.schedule import Schedule
import datetime

app = create_app()

with app.app_context():
    # Add a bus
    bus = Bus(bus_name="GoBus Express", total_seats=40)
    db.session.add(bus)
    db.session.commit()

    # Add a schedule
    schedule = Schedule(
        bus_id=bus.id,
        source="HYD",
        destination="BLR",
        departure_datetime=datetime.datetime(2025,8,22,9,30),
        price=899
    )
    db.session.add(schedule)
    db.session.commit()

    print("Seed data inserted successfully!")
