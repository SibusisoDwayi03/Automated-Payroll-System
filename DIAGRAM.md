```mermaid
graph TD;
    Employee -->|Requests Payslip| PayrollSystem;
    HR -->|Manages Employees| PayrollSystem;
    PayrollSystem -->|Sends Salary Data| BankAPI;
    BankAPI -->|Processes Payments| Employee;
    PayrollSystem -->|Generates Reports| HR;

