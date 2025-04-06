    2.1 View Payslip Workflow
flowchart TD
    A[Start] --> B[Login]
    B --> C[Go to Payslip Module]
    C --> D[System Retrieves Payslip]
    D --> E[Display Payslip]
    E --> F[End]

  Mapped to: FR-001, US-001

    2.2 Process Payroll Workflow
  flowchart TD
    A[Start] --> B[HR Inputs Payroll Info]
    B --> C[System Validates Data]
    C --> D{Is Data Valid?}
    D -- No --> E[Prompt for Corrections]
    D -- Yes --> F[Manager Approves]
    F --> G[Run Payroll]
    G --> H[Generate Payslips]
    H --> I[End]

  Mapped to: FR-002, US-002

    2.3 Generate Financial Report Workflow

   flowchart TD
    A[Start] --> B[Finance Logs In]
    B --> C[Select Report Type]
    C --> D[Fetch Data]
    D --> E[Format Report]
    E --> F[Display or Download]
    F --> G[End]

  Mapped to: FR-003, US-003

    2.4 Update Personal Details Workflow

  flowchart TD
    A[Start] --> B[Login]
    B --> C[Access Profile Settings]
    C --> D[Edit Details]
    D --> E[Submit Changes]
    E --> F{Are Changes Valid?}
    F -- Yes --> G[Update Database]
    G --> H[Show Confirmation]
    H --> I[End]
    F -- No --> J[Show Error]
    J --> I
  Mapped to: FR-006, US-006
  
    2.5 Secure Login Workflow
    
  flowchart TD
    A[Start] --> B[Input Credentials]
    B --> C[System Hashes & Validates]
    C --> D{Credentials Valid?}
    D -- Yes --> E[Grant Access]
    D -- No --> F[Error / Retry]
    E --> G[End]
    F --> G

  Mapped to: FR-004, NFR-009
  
    2.6 Tax Calculation Workflow 
    
  flowchart TD
    A[Start] --> B[Trigger Payroll]
    B --> C[Retrieve Tax Tables]
    C --> D[Apply Rules]
    D --> E[Calculate Deduction]
    E --> F[Link to Payslip]
    F --> G[End]

  Mapped to: FR-005, US-005

    2.7 Audit Trail Entry 
    
  flowchart TD
    A[Start] --> B[Action Detected]
    B --> C[Create Log Entry]
    C --> D[Timestamp Assigned]
    D --> E[Save to DB]
    E --> F[End]

  Mapped to: FR-008, US-008

    2.8 Approve Payroll Workflow

  flowchart TD
    A[Start] --> B[HR Submits Payroll]
    B --> C[Manager Reviews]
    C --> D{Approve?}
    D -- Yes --> E[Approve Payroll]
    D -- No --> F[Return to HR for Edits]
    E --> G[Start Processing]
    F --> G
    G --> H[End]

  Mapped to: FR-007, US-007
