
class Employee:
    empCount = 0

  def init (self, name, salary):
    self.name = name
    self.salary = salary
    Employee.empCount += 1
 
  def displayCount(self):
    print("Total Employee %d" % Employee.empCount)

  def displayEmployee(self):
    print("Name : ", self.name, ", Salary: ", self.salary)

    emp1 = Employee ("asif", 2000)
    emp2 = Employee("manni", 5000)
    
print("Total Employee %d" % Employee.empCount)

