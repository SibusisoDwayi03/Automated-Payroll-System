from repositories.inmemory.InMemoryHRManagerRepository import InMemoryHRManagerRepository

class DummyHRManager:
    def __init__(self, manager_id):
        self.manager_id = manager_id

def test_save_and_find_hrmanager():
    repo = InMemoryHRManagerRepository()
    hr = DummyHRManager("h1")
    repo.save(hr)
    assert repo.find_by_id("h1") == hr

def test_delete_hrmanager():
    repo = InMemoryHRManagerRepository()
    hr = DummyHRManager("h2")
    repo.save(hr)
    repo.delete("h2")
    assert repo.find_by_id("h2") is None