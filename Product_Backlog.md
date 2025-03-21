# Product Backlog

| **Story ID** | **User Story** | **Priority (MoSCoW)** | **Effort Estimate (Story Points)** | **Dependencies** |
|------------|------------------------------------------------|----------------|-------------------------|----------------|
| US-001 | Employee views payslip | Must-have | 3 | None |
| US-002 | HR processes payroll | Must-have | 5 | US-007 |
| US-003 | Finance generates reports | Must-have | 4 | US-002 |
| US-004 | IT secures payroll data | Must-have | 5 | None |
| US-005 | System calculates tax deductions | Should-have | 3 | US-002 |
| US-006 | Employee updates personal details | Should-have | 2 | None |
| US-007 | HR approves payroll | Must-have | 3 | US-002 |
| US-008 | IT maintains audit log | Could-have | 2 | US-002 |
| US-009 | User data encryption with AES-256 | Must-have | 5 | None |

### Justification for Prioritization
- **Must-have:** Core payroll functionalities (view payslip, process payroll, generate reports) align with key stakeholder success metrics.
- **Should-have:** Features that enhance accuracy (tax calculations, employee profile updates).
- **Could-have:** Features improving auditability but not critical for MVP (audit logs).
- **Won’t-have:** Features requiring additional phases are deferred for future sprints.

