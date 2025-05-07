from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.payslip_service import PayslipService

router = APIRouter(prefix="/api/payslips", tags=["Payslips"])
service = PayslipService()

class Payslip(BaseModel):
    payslip_id: str
    employee_id: str
    base_salary: float
    tax_deductions: float
    net_pay: float = 0

@router.post("/", response_model=Payslip)
def generate(payslip: Payslip):
    return service.generate_payslip(payslip)

@router.get("/{payslip_id}", response_model=Payslip)
def get(payslip_id: str):
    result = service.get_payslip(payslip_id)
    if not result:
        raise HTTPException(status_code=404, detail="Payslip not found")
    return result
