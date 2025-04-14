This domain model represents the core structure of the Automated Payroll System based on prior assignments. It includes essential business entities, their relationships, and responsibilities.


| **Entity**      | **Attributes**                                                             | **Methods**                                     | **Relationships**                                                 |
|------------------|---------------------------------------------------------------------------|--------------------------------------------------|------------------------------------------------------------------|
| **Employee**      | employeeId, name, email, role, bankDetails, taxStatus                    | viewPayslip(), updateDetails()                  | Associated with Payslip (1..*), linked to PayrollBatch (0..*)     |
| **HRManager**     | managerId, name, email                                                    | approvePayroll(), manageEmployeeRecords()       | Reviews PayrollBatch (1..*), has access to AuditLog              |
| **PayrollBatch**  | batchId, period, status, createdOn                                        | generatePayslips(), processPayroll()            | Contains Payslip (1..*), linked to HRManager (1)                 |
| **Payslip**       | payslipId, grossSalary, netSalary, taxAmount, deductions, issueDate      | calculateNetPay(), printPayslip()               | Belongs to Employee (1), part of PayrollBatch (1)                |
| **TaxCalculator** | taxRate, taxBrackets                                                      | calculateTax(grossSalary), validateTaxStatus()  | Used by PayrollBatch and Payslip                                 |
| **AuditLog**      | logId, userId, actionType, timestamp                                      | logAction(), getLogsForUser()                   | Accessed by HRManager and System                                 |
| **SystemUser**    | userId, username, passwordHash, role                                      | login(), logout(), resetPassword()              | Generalization → Employee, HRManager                             |


Business Rules:

*An Employee can receive multiple Payslips, one per PayrollBatch.

*A PayrollBatch cannot be processed until approved by the HRManager.

*Payslip must contain accurate tax deduction calculated by the TaxCalculator.

*Only authorized HRManager can view and review AuditLogs.

*SystemUser is a general type for login access — inherited by both Employee and HRManager.
