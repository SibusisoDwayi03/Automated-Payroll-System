Designing the domain model and class diagram for the Automated Payroll System posed a number of rewarding and educational challenges. Below is a detailed reflection on the design process, its alignment with previous assignments, and key lessons learned.

1. Challenges Faced

One major challenge was selecting the appropriate level of abstraction for each entity. Initially, it was difficult to determine whether "SystemUser" should remain abstract or be treated as a concrete class. To reduce duplication, I chose inheritance, using "SystemUser" as a base for both Employee and HRManager, which proved effective in unifying common login attributes.

Additionally, identifying the right relationships (aggregation vs. association vs. composition) required careful thought. For example, Payslip aggregation within PayrollBatch made sense because Payslips are generated in bulk per batch but could still be independently stored and managed.

Capturing behavior (i.e., methods) was also tricky, especially for utility classes like TaxCalculator and AuditLog. Since these aren’t domain entities with standalone workflows, I treated them as services rather than primary objects.

2. Alignment with Previous Assignments

This class diagram builds directly on prior work:

Assignment 4 (Requirements): Each class corresponds to key functional requirements (e.g., Payslip → View Salary).

Assignment 5 (Use Cases): Methods like generatePayslips(), approvePayroll(), and updateDetails() represent the system’s behavior from Assignment 5.

Assignment 6 (User Stories): Entities like Employee and HRManager trace directly to user stories in the backlog.

Assignment 8 (State Diagrams): Payslip and PayrollBatch lifecycle states informed attribute design (e.g., status, issueDate).

3. Trade-offs and Design Choices

I avoided deep inheritance and complex compositions to keep the diagram maintainable. While more abstraction might be beneficial in real-world systems, in this academic scope, clarity and alignment were prioritized. For example, I used simple associations where dependency injection or service layers might normally be used.

TaxCalculator and AuditLog were intentionally left loosely coupled to preserve modularity — these could easily be replaced or extended without major structural changes.

4. Lessons Learned

This assignment deepened my understanding of:

Object-Oriented Design: The importance of cohesion within classes and the role of abstraction.

UML Semantics: Differentiating relationships like inheritance vs. association improved the accuracy of the diagram.

Design-Driven Development: Good design makes implementation clearer and stakeholder communication easier.

In summary, the domain and class models effectively captured the system’s key components, maintained alignment with all previous design efforts, and laid a solid foundation for implementation and testing.Designing the domain model and class diagram for the Automated Payroll System posed a number of rewarding and educational challenges. Below is a detailed reflection on the design process, its alignment with previous assignments, and key lessons learned.

1. Challenges Faced

One major challenge was selecting the appropriate level of abstraction for each entity. Initially, it was difficult to determine whether "SystemUser" should remain abstract or be treated as a concrete class. To reduce duplication, I chose inheritance, using "SystemUser" as a base for both Employee and HRManager, which proved effective in unifying common login attributes.

Additionally, identifying the right relationships (aggregation vs. association vs. composition) required careful thought. For example, Payslip aggregation within PayrollBatch made sense because Payslips are generated in bulk per batch but could still be independently stored and managed.

Capturing behavior (i.e., methods) was also tricky, especially for utility classes like TaxCalculator and AuditLog. Since these aren’t domain entities with standalone workflows, I treated them as services rather than primary objects.

2. Alignment with Previous Assignments

This class diagram builds directly on prior work:

Assignment 4 (Requirements): Each class corresponds to key functional requirements (e.g., Payslip → View Salary).

Assignment 5 (Use Cases): Methods like generatePayslips(), approvePayroll(), and updateDetails() represent the system’s behavior from Assignment 5.

Assignment 6 (User Stories): Entities like Employee and HRManager trace directly to user stories in the backlog.

Assignment 8 (State Diagrams): Payslip and PayrollBatch lifecycle states informed attribute design (e.g., status, issueDate).

3. Trade-offs and Design Choices

I avoided deep inheritance and complex compositions to keep the diagram maintainable. While more abstraction might be beneficial in real-world systems, in this academic scope, clarity and alignment were prioritized. For example, I used simple associations where dependency injection or service layers might normally be used.

TaxCalculator and AuditLog were intentionally left loosely coupled to preserve modularity — these could easily be replaced or extended without major structural changes.

4. Lessons Learned

This assignment deepened my understanding of:

Object-Oriented Design: The importance of cohesion within classes and the role of abstraction.

UML Semantics: Differentiating relationships like inheritance vs. association improved the accuracy of the diagram.

Design-Driven Development: Good design makes implementation clearer and stakeholder communication easier.

In summary, the domain and class models effectively captured the system’s key components, maintained alignment with all previous design efforts, and laid a solid foundation for implementation and testing.
