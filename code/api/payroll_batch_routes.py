from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from services.payroll_batch_service import PayrollBatchService

router = APIRouter(prefix="/api/payroll-batches", tags=["PayrollBatches"])
service = PayrollBatchService()

class PayrollBatch(BaseModel):
    batch_id: str
    description: str
    status: str = "Pending"

@router.post("/", response_model=PayrollBatch)
def create_batch(batch: PayrollBatch):
    return service.create_batch(batch)

@router.post("/{batch_id}/approve", response_model=PayrollBatch)
def approve(batch_id: str):
    try:
        return service.approve_batch(batch_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[PayrollBatch])
def all_batches():
    return service.get_all_batches()
