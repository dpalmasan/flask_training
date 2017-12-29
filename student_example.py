lottery_player_dict = {
    'name'      : 'Rolf',
    'numbers'   : (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name       = name
        self.numbers    = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer("Rolf")
player_one.numbers = (1, 2, 3, 6, 7, 8)
player_two = LotteryPlayer("John")

print player_one.numbers == player_two.numbers

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/float(len(self.marks))

    @staticmethod
    def go_to_school():
        """
        Lets suppose that the method is generic (we do not use self)
        If we remove self, python will throw an error, this is why we 
        put static method
        """
        print "I am going to school."

anna = Student("Anna", "MIT")
anna.marks.append(56)
print anna.marks
anna.marks.append(20)
print anna.average()

# We can also do
Student.go_to_school()
