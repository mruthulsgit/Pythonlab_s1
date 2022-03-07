class Employee:
    emp_id_start = 10

    def __init__(self,name, salary, address):
        self.empp_id = self.emp_id_start
        self.emp_id_start += 1
        self.name = name
        self.salary = salary
        self.address = address
    
class Teacher(Employee):
    def __init__(self,name, salary, address, depatment, subjects):
        self.depatment = depatment
        self.subjects = subjects
        super().__init__(name, salary, address)

    def display(self):
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Address: ", self.address)
        print("Depatment: ", self.depatment)
        print("Subjects: ", self.subjects)

emp = Employee("Goutham", 4500, "Trivandrum")
teacher = Teacher("Goutham", 7000, "Trivadnrum", "MCA", ["Python", "S.E"])

teacher.display()
        
