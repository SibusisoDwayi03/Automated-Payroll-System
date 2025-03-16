# Test Cases

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|-----------------|----------------|---------------|---------|------------------|------------------|-----------------|
| TC-001 | FR-001 | Employee views payslip | 1. Log in as employee  2. Click "View Payslip"  3. Select month | Payslip is displayed correctly | | |
| TC-002 | FR-002 | HR Manager processes payroll | 1. Log in as HR  2. Click "Process Payroll"  3. Confirm calculations | Payroll is processed and summary displayed | | |
| TC-003 | FR-003 | HR updates employee data | 1. Log in as HR  2. Edit employee info  3. Save changes | Employee data is updated | | |
| TC-004 | FR-004 | Finance generates reports | 1. Log in as Finance  2. Click "Generate Reports"  3. Select report type | Report is generated and available for download | | |
| TC-005 | FR-005 | System calculates tax | 1. Log in as Finance  2. Click "Calculate Tax"  3. Confirm calculation | Tax is calculated and stored | | |
| TC-006 | FR-006 | HR approves payroll | 1. Log in as HR  2. Click "Approve Payroll"  3. Confirm approval | Payroll is marked as approved | | |
| TC-007 | FR-007 | IT secures system | 1. Log in as IT  2. Update security settings  3. Save changes | Security settings are applied | | |
| TC-008 | FR-008 | IT accesses audit log | 1. Log in as IT  2. Click "View Audit Log"  3. Review log | System logs are displayed | | |

## Non-Functional Test Cases

| **Test Case ID** | **Requirement ID** | **Description** | **Steps** | **Expected Result** | **Actual Result** | **Status (Pass/Fail)** |
|-----------------|----------------|---------------|---------|------------------|------------------|-----------------|
| TC-NF-001 | NFR-001 | Performance Test - Load Handling | Simulate 1,000 users logging in at once | System remains responsive, loads within 2 seconds | | |
| TC-NF-002 | NFR-002 | Security Test - Unauthorized Access | Attempt to access payroll without login | Access is denied, user is logged out | | |

