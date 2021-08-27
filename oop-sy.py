class User:
    def __init__(self, first, last, age):
        print(f"User- {first} created")
        self.first = first
        self.last = last
        self.age = age


user1 = User(
    "Joe",
    "smith",
    "86",
)
user2 = User(
    "Hoe",
    "smith",
    "86",
)
user3 = User("Moe", "smith", "86",)
user4 = User("Foe", "smith", "86",)

print(f"{user1.first} {user1.last}")
print(f"{user2.first} {user2.last}")
print(f"{user3.first} {user3.last}")
print(f"{user4.first} {user4.last}")
