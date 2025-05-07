from fastapi import FastAPI
from api.employee_routes import router as employee_router
from api.payslip_routes import router as payslip_router
from api.payroll_batch_routes import router as batch_router

app = FastAPI()

app.include_router(employee_router)
app.include_router(payslip_router)
app.include_router(batch_router)
