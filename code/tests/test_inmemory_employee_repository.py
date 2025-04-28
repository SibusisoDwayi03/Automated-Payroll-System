from repositories.inmemory.InMemoryEmployeeRepository import InMemoryEmployeeRepository

class DummyEmployee:
    def __init__(self, employee_id):
        self.employee_id = employee_id

def test_save_and_find_employee():
    repo = InMemoryEmployeeRepository()
    emp = DummyEmployee("e1")
    repo.save(emp)
    assert repo.find_by_id("e1") == emp

def test_delete_employee():
    repo = InMemoryEmployeeRepository()
    emp = DummyEmployee("e2")
    repo.save(emp)
    repo.delete("e2")
    assert repo.find_by_id("e2") is None