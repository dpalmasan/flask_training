class Student(object):
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / float(len(self.marks))

    @classmethod
    def friend(cls, origin, friend_name, salary):
        return cls(friend_name, origin.school, salary)


anna = Student("Anna", "Oxford")


class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super(WorkingStudent, self).__init__(name, school)
        self.salary = salary


anna = WorkingStudent("Anna", "Oxford", 20.00)
print anna.salary

friend = WorkingStudent.friend(anna, "Greg", 20)
print friend.name
print friend.school
print friend.salary
