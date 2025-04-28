from repositories.inmemory.InMemoryEmployeeRepository import InMemoryEmployeeRepository
from repositories.inmemory.InMemoryHRManagerRepository import InMemoryHRManagerRepository

class RepositoryFactory:
    @staticmethod
    def get_employee_repository():
        return InMemoryEmployeeRepository()

    @staticmethod
    def get_hrmanager_repository():
        return InMemoryHRManagerRepository()