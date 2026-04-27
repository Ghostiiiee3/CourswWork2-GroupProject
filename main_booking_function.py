import json
import os
from datetime import datetime

BOOKING_FILE = "bookings.json"


class BookingSystem:

    def __init__(self):

        self.bookings = self.load_bookings()

        # rooms
        self.rooms = ["LAB1", "LAB2", "ROOMA", "ROOMB"]

        # booking times
        self.times = ["09:00", "10:00", "11:00", "12:00", "13:00"]

    # Load bookings
    def load_bookings(self):

        if not os.path.exists(BOOKING_FILE):
            return []

        try:
            with open(BOOKING_FILE, "r") as file:
                return json.load(file)

        except: