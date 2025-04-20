# Automated Payroll System

The Automated Payroll System is designed to simplify salary processing by automating calculations, deductions, and payments while ensuring compliance with financial regulations.

## 📌 Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Architecture](#architecture)
- [Technologies](#technologies)
- [License](#license)

## 🔹 Project Overview
This system allows companies to:
- Automatically calculate employee salaries, deductions, and bonuses.
- Generate and distribute payslips.
- Ensure tax compliance based on financial regulations.
- Enable secure login for HR, finance, and employees.
- Integrate with banking APIs for salary payments.

## 🔹 Features
✅ Employee management (Add, update, remove employees)  
✅ Salary computation (Base salary, overtime, tax deductions)  
✅ Payslip generation (Downloadable PDF format)  
✅ Secure authentication (HR & Finance roles)  
✅ Automated salary payments via banking API  

## 🔹 Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/<SibusisoDwayi03>/automated-payroll-system.git


- [System Specification](SPECIFICATION.md)
- [Context Diagram](DIAGRAM.md)
- [Architecture Design](ARCHITECTURE.md)

# Assignment 8: Object State & Workflow Modeling

This repository contains the deliverables for Assignment 8, which involve modeling system behavior using object state diagrams and activity workflow diagrams. These diagrams trace directly to requirements and user stories from Assignments 4 through 7.

## Deliverables

- [`state_diagrams.md`](./state_diagrams.md): Mermaid-based state diagrams of key system objects.
- [`activity_workflows.md`](./activity_workflows.md): Mermaid-based activity workflows for user and system interactions.
- [`assignment8_reflection.md`](./assignment8_reflection.md): Reflection on challenges and comparison of diagram types.

## Integration with Prior Work

- Requirements from Assignment 4 have been translated into states and workflows.
- User stories from Assignment 6 are represented in both state and activity diagrams.
- Sprint tasks and backlog items helped define the flow of the system in this assignment.

  
# Automated Payroll System – Assignment 10

## Language Choice: Python
For the project I used Python for its readability, strong OOP support, and testability using tools like `pytest`. It aligns with the previously designed class diagram and is ideal for rapid prototyping and pattern implementation.

## Project Structure
```
📁 Automated-Payroll-System/
├── README.md
├── CHANGELOG.md
├── src/                            # Class implementations
│   ├── system_user.py
│   ├── employee.py
│   ├── hr_manager.py
│   ├── payroll_batch.py
│   ├── payslip.py
│   ├── tax_calculator.py
│   └── audit_log.py
├── creational_patterns/           # Creational design pattern implementations
│   ├── simple_factory.py
│   ├── factory_method.py
│   ├── abstract_factory.py
│   ├── builder.py
│   ├── prototype.py
│   └── singleton.py
├── tests/                         # Unit tests
│   ├── test_simple_factory.py
│   ├── test_factory_method.py
│   ├── test_abstract_factory.py
│   ├── test_builder.py
│   ├── test_prototype.py
│   └── test_singleton.py
```

## Creational Patterns Used

| Pattern           | Use Case & Justification                                                                 |
|------------------|------------------------------------------------------------------------------------------|
| Simple Factory    | Centralized creation of objects like vehicles (e.g., Car, Bike)                         |
| Factory Method    | Allows extensible instantiation of different payment processors                         |
| Abstract Factory  | Creates families of GUI elements (e.g., Buttons for Windows and MacOS)                  |
| Builder           | Constructs complex objects like Pizza step by step with optional attributes             |
| Prototype         | Clones existing object instances like Shape for fast memory-safe replication            |
| Singleton         | Restricts instantiation of a class (e.g., Database connection) to a single shared object|

## How to Run Tests
Make sure you have `pytest` installed. Then run:
```bash
pytest tests/
```

## Author
Sibusiso Dwayi – Assignment 10



