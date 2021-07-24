from HotelRooms04.room import Room

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number][0]
        if not room.take_room(people):
            self.guests += room.guests

    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number][0]
        room.free_room()
        self.guests = 0

    def status(self):
        taken_rooms = [room.number for room in self.rooms if room.is_taken]
        free_rooms = [room.number for room in self.rooms if not room.is_taken]

        return f"Hotel {self.name} has {self.guests} total guests\n" \
                f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
                f"Taken rooms: {', '.join(map(str, taken_rooms))}"

