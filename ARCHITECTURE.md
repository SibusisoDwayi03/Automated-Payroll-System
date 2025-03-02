# System Architecture - Automated Payroll System

## 1️⃣ Overview
This document outlines the system architecture of the **Automated Payroll System**, which automates employee salary processing.

## 2️⃣ System Components
- **Frontend:** React.js (User interface for HR, Finance, and Employees)
- **Backend:** Node.js + Express.js (Payroll logic, authentication)
- **Database:** PostgreSQL (Stores employee records, salary details)
- **Authentication:** JWT-based authentication (Secure user access)
- **Bank API Integration:** Stripe/PayFast (Automated salary disbursements)

## 3️⃣ C4 Diagrams
- **Context Diagram:** Shows interactions between users and the system.
- **Container Diagram:** Illustrates major system components.
- **Component Diagram:** Displays internal structure of key components.

## 4️⃣ Data Flow
1. HR/Finance logs into the system.
2. Employees' salaries are calculated based on predefined rules.
3. Tax deductions and bonuses are applied.
4. Payslips are generated and stored in the database.
5. The system integrates with a banking API to process payments.
6. Employees receive salary notifications.

## 5️⃣ Security Measures
- **Data encryption** for salary records.
- **Role-based access control** for different users.
- **Audit logs** for tracking changes in payroll records.

📌 **Diagrams are available in the `/diagrams` folder.**

