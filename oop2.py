class Robot:
    """
    This implements a Robot.
    """
    population = 0
    def __init__(self, name, year):
        self.name = name
        self.year = year
        Robot.population += 1
    def setEnergy(self, energy):
        self.energy = energy


r1 = Robot("DK", 6006 )
print('Robot name: ',r1.name, 'BUilt in:', r1.year)

r1.setEnergy(1000)
print((r1.__dict__))

#print('Energy consumed:', r1.energy)
print('Energy status:', getattr(r1, 'energy'))

r2 = Robot('Amadeus', 5555)
print((r2.__dict__))
r3 = Robot('Willy', 1111)

print('Robot population:', Robot.population)
