class Planet:
    def __init__(self, id, name, description, moon):
        self.id = id 
        self.name = name
        self.description = description
        self.moon = moon
    

planets = [
    Planet(1, "Earth", "a beatutify star", "1 Moon"),
    Planet(2, "Pluto", "A totally real planet", "3 Moons"),
    Planet(3, "Mars", "big star", "0 moons")
    ]