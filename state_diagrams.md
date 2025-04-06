    Employee Paslip State Diiagram:
stateDiagram-v2
    [*] --> Generated : Payroll Processed
    Generated --> Viewed : Employee views payslip
    Generated --> Errors_Found : HR identifies error
    Errors_Found --> Corrected : HR corrects payslip
    Corrected --> Viewed : Employee views corrected payslip
    Viewed --> [*]

  Explanation:

States: Generated, Viewed, Corrected

Requirement: FR-001 (View Payslip)


    Payroll Batch State Diiagram:

stateDiagram-v2
    [*] --> Draft : Created by HR
    Draft --> Approved : Reviewed by HR manager
    Approved --> Processed : Payroll executed
    Processed --> Archived : Month-end completed
    Draft --> Cancelled : Cancelled before approval

  Explanation:

States: Draft, Approved, Processed, Archived, Cancelled

Requirements: FR-002 (Process Payroll), FR-007 (Approve Payroll)


    User Account State Diiagram:

stateDiagram-v2
    [*] --> Registered : User signs up
    Registered --> Active : Email confirmed
    Active --> Suspended : Suspicious activity or admin action
    Suspended --> Active : Issue resolved
    Active --> Deleted : Account removed

   Explanation:

Covers: Account lifecycle and access control

Requirement: FR-004 (Data Security)

    Financial Report State Diiagram:

stateDiagram-v2
    [*] --> Generated : Report compiled
    Generated --> Reviewed : Finance team checks data
    Reviewed --> Finalized : Approved and closed
    Finalized --> Archived : Record stored

   Explanation:

Used in: Monthly reporting, auditing

Requirement: FR-003 (Generate Reports)


    Tax Calculation State Diiagram:

stateDiagram-v2
    [*] --> Initiated : On payroll start
    Initiated --> Calculated : Tax logic run
    Calculated --> Validated : Verified by compliance
    Validated --> Applied : Finalized in payslip

  Explanation:

Automated Tax Deduction Logic

Requirement: FR-005

    Employee Personal Details State Diiagram:
    
stateDiagram-v2
    [*] --> Current : Up-to-date
    Current --> Update_Requested : Employee submits changes
    Update_Requested --> Validated : System checks input
    Validated --> Current

  Explanation:

Tracks changes in profile data

Requirement: FR-006 (Update Personal Info)

    Audit Log State Diiagram:
    
stateDiagram-v2
    [*] --> Entry_Logged : System records action
    Entry_Logged --> Reviewed : Admin audit
    Reviewed --> Archived : Retention period met

    Explanation:

Security compliance logging

Requirement: FR-008 (Maintain Audit Log)


  
