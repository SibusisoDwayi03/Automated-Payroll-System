class InMemoryHRManagerRepository:
    def __init__(self):
        self.hr_managers = {}

    def save(self, hr_manager):
        self.hr_managers[hr_manager.manager_id] = hr_manager

    def find_by_id(self, manager_id):
        return self.hr_managers.get(manager_id)

    def find_all(self):
        return list(self.hr_managers.values())

    def delete(self, manager_id):
        if manager_id in self.hr_managers:
            del self.hr_managers[manager_id]