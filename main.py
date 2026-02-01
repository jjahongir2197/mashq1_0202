class Room:
    def __init__(self, number, price):
        self.number = number
        self.price = price
        self.free = True

    def info(self):
        status = "Bo‘sh" if self.free else "Band"
        return f"Xona {self.number} | {self.price} so‘m | {status}"


class Hotel:
    def __init__(self):
        self.rooms = []
        self.cash = 0

    def add_room(self, room):
        self.rooms.append(room)

    def show_rooms(self):
        for i, r in enumerate(self.rooms):
            print(i, r.info())

    def book(self, index, days):
        room = self.rooms[index]
        if room.free:
            room.free = False
            cost = room.price * days
            self.cash += cost
            print("Bron qilindi. Narx:", cost)
        else:
            print("Xona band")

    def free_room(self, index):
        self.rooms[index].free = True
        print("Xona bo‘shatildi")

    def report(self):
        print("Daromad:", self.cash)


hotel = Hotel()
hotel.add_room(Room(101, 200000))
hotel.add_room(Room(102, 300000))

while True:
    print("\n1.Xonalar 2.Bron 3.Bo‘shatish 4.Hisobot 0.Exit")
    c = input(">>> ")

    if c == "1":
        hotel.show_rooms()
    elif c == "2":
        hotel.book(int(input("Index: ")), int(input("Kun: ")))
    elif c == "3":
        hotel.free_room(int(input("Index: ")))
    elif c == "4":
        hotel.report()
    elif c == "0":
        break
