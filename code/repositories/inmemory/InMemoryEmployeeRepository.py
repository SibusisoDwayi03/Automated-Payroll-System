class InMemoryEmployeeRepository:
    def __init__(self):
        self.employees = {}

    def save(self, employee):
        self.employees[employee.employee_id] = employee

    def find_by_id(self, employee_id):
        return self.employees.get(employee_id)

    def find_all(self):
        return list(self.employees.values())

    def delete(self, employee_id):
        if employee_id in self.employees:
            del self.employees[employee_id]