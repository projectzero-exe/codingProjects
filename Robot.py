class Robot:
    """
    This implements a Robot.
    """
    def __init__(self, name, year):
        self.name = name
        self.year = year
        print('Creating a new robot. Its name is:', self.name)

    def __del__(self):
        print('Robot died ')

# r1 = Robot("Hansi", 1996)
#
# # print(type(r1))
# #
# # print(r1.__doc__)
#
# print('Robot name:', r1.name)
# print('Built in Year:', r1.year)
#
# print('Dictionary that stores the attributes:', r1.__dict__)

