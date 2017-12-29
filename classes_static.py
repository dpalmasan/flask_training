class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / float(len(self.marks))

    def friend(self, friend_name):
        return Student(friend_name, self.school)


anna = Student("Anna", "Oxford")
friend = anna.friend("Greg")

print friend.name
print friend.school


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super(self).__init__(name, school)
        self.salary = salary


anna = WorkingStudent("Anna", "Oxford", 20.00)
print anna.salary

friend = anna.friend("Greg")
