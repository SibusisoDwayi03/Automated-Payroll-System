from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.employee_service import EmployeeService

router = APIRouter(prefix="/api/employees", tags=["Employees"])
service = EmployeeService()

class Employee(BaseModel):
    employee_id: str
    name: str
    role: str
    salary: float

@router.post("/", response_model=Employee)
def create_employee(emp: Employee):
    return service.create_employee(emp)

@router.get("/{employee_id}", response_model=Employee)
def get_employee(employee_id: str):
    result = service.get_employee(employee_id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@router.get("/", response_model=list[Employee])
def get_all():
    return service.get_all_employees()
