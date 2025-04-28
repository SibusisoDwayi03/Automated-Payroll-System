```mermaid
classDiagram
    Repository <|-- EmployeeRepository
    Repository <|-- HRManagerRepository
    EmployeeRepository <|-- InMemoryEmployeeRepository
    HRManagerRepository <|-- InMemoryHRManagerRepository
    EmployeeRepository <|.. FileSystemEmployeeRepository
    RepositoryFactory --> InMemoryEmployeeRepository
    RepositoryFactory --> InMemoryHRManagerRepository
```