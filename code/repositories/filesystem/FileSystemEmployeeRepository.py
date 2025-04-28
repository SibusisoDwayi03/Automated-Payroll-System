# Stub for future filesystem-based persistence (JSON)

class FileSystemEmployeeRepository:
    def __init__(self, filepath):
        self.filepath = filepath

    def save(self, employee):
        pass

    def find_by_id(self, employee_id):
        pass

    def find_all(self):
        pass

    def delete(self, employee_id):
        pass