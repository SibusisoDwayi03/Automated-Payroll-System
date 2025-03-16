# Use Case Specifications

## 1. View Payslip
- **Actor:** Employee
- **Description:** Allows employees to view and download their payslips.
- **Preconditions:** Employee must be logged into the system.
- **Postconditions:** Employee sees or downloads their payslip.
- **Basic Flow:**
  1. Employee logs in.
  2. Selects "View Payslip" option.
  3. System fetches payslip from the database.
  4. Payslip is displayed.
- **Alternative Flow:**
  - Payslip not found → Display error message.

## 2. Process Payroll
- **Actor:** HR Manager
- **Description:** Calculates and processes payroll for all employees.
- **Preconditions:** Payroll period is active.
- **Postconditions:** Payroll is processed successfully.
- **Basic Flow:**
  1. HR Manager selects "Process Payroll" option.
  2. System calculates salaries, deductions, and taxes.
  3. System generates payroll summary.
  4. HR Manager confirms processing.
  5. System marks payroll as completed.
- **Alternative Flow:**
  - Calculation errors → Display error message.

## 3. Manage Employee Data
- **Actor:** HR Manager
- **Description:** Allows HR to add, edit, or remove employee information.
- **Preconditions:** HR Manager must be logged in.
- **Postconditions:** Employee data is updated.
- **Basic Flow:**
  1. HR Manager selects "Manage Employee Data" option.
  2. System displays employee records.
  3. HR selects an employee record to update.
  4. System saves changes.
- **Alternative Flow:**
  - Invalid input → Show validation error.

## 4. Generate Reports
- **Actor:** Finance Officer
- **Description:** Generates financial reports for payroll analysis.
- **Preconditions:** Financial period is active.
- **Postconditions:** Report is generated and available for download.
- **Basic Flow:**
  1. Finance Officer selects "Generate Reports" option.
  2. System retrieves payroll data.
  3. Report is generated.
  4. System allows download.
- **Alternative Flow:**
  - No data available → Show message.

## 5. Calculate Tax
- **Actor:** Finance Officer, Compliance Officer
- **Description:** Calculates tax deductions for employees.
- **Preconditions:** Employee payroll data is available.
- **Postconditions:** Tax is calculated and stored.
- **Basic Flow:**
  1. System retrieves payroll data.
  2. System applies tax rules.
  3. Tax amount is calculated and stored.
- **Alternative Flow:**
  - Tax rules outdated → Display warning.

## 6. Approve Payroll
- **Actor:** HR Manager
- **Description:** Final approval step before salary payments.
- **Preconditions:** Payroll must be processed.
- **Postconditions:** Payroll is approved for payment.
- **Basic Flow:**
  1. HR Manager selects "Approve Payroll" option.
  2. System displays payroll summary.
  3. HR Manager confirms approval.
- **Alternative Flow:**
  - Payroll incomplete → Display error.

## 7. Secure System
- **Actor:** IT Administrator
- **Description:** Ensures security settings and access controls are in place.
- **Preconditions:** IT Administrator must be logged in.
- **Postconditions:** Security settings are enforced.
- **Basic Flow:**
  1. IT Admin logs in.
  2. System displays security settings.
  3. IT Admin updates access controls.
  4. Changes are saved.
- **Alternative Flow:**
  - Unauthorized access attempt → Log and notify admin.

## 8. Access Audit Log
- **Actor:** IT Administrator
- **Description:** Allows IT to monitor system activity logs.
- **Preconditions:** Logs must be enabled.
- **Postconditions:** IT Admin reviews logs.
- **Basic Flow:**
  1. IT Admin selects "Access Audit Log".
  2. System retrieves logs.
  3. Logs are displayed.
- **Alternative Flow:**
  - No logs available → Show message.

