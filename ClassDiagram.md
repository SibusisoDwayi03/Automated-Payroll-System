# Class Diagram 

```mermaid
classDiagram
    %% Base User
    class SystemUser {
        - userId: String
        - username: String
        - passwordHash: String
        - role: String
        + login()
        + logout()
        + resetPassword()
    }

    %% Employee
    class Employee {
        - employeeId: String
        - name: String
        - email: String
        - bankDetails: String
        - taxStatus: String
        + viewPayslip()
        + updateDetails()
    }

    %% HR Manager
    class HRManager {
        - managerId: String
        - name: String
        - email: String
        + approvePayroll()
        + manageEmployeeRecords()
    }

    %% Payroll Batch
    class PayrollBatch {
        - batchId: String
        - period: Date
        - status: String
        - createdOn: Date
        + generatePayslips()
        + processPayroll()
    }

    %% Payslip
    class Payslip {
        - payslipId: String
        - grossSalary: Float
        - netSalary: Float
        - taxAmount: Float
        - deductions: Float
        - issueDate: Date
        + calculateNetPay()
        + printPayslip()
    }

    %% Tax Calculator
    class TaxCalculator {
        - taxRate: Float
        - taxBrackets: Map
        + calculateTax(grossSalary: Float)
        + validateTaxStatus()
    }

    %% Audit Log
    class AuditLog {
        - logId: String
        - userId: String
        - actionType: String
        - timestamp: DateTime
        + logAction()
        + getLogsForUser(userId: String)
    }

    %% Inheritance
    SystemUser <|-- Employee
    SystemUser <|-- HRManager

    %% Associations
    Employee "1" --> "0..*" Payslip : receives
    Payslip "1" --> "1" PayrollBatch : belongs to
    PayrollBatch "1" --> "1..*" Payslip : generates
    PayrollBatch "1" --> "1" HRManager : approved by
    Payslip --> TaxCalculator : uses
    HRManager --> AuditLog : accesses
