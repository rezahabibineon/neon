import json
from unittest import result
from fastapi import APIRouter, Body, Response, Query
from apps.controllers.LoanController import ControllerLoan as loan
from typing import Optional

router = APIRouter()

example_input_cifno = json.dumps({
    "cif": "1",
}, indent=2)

@router.post("/get_loan_by_cif")
async def get_loan_by_cif(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = loan.get_loan_by_cif(input_data=input_data)
    response.status_code = result.status
    return result

@router.post("/get_loan_by_cif_debug")
async def get_loan_by_cif_debug(response: Response, input_data=Body(..., example=example_input_cifno)):
    result = loan.get_loan_by_cif_debug(input_data=input_data)
    response.status_code = result.status
    return result

@router.get("/get_total_by_feature") 
async def get_total_by_feature(response: Response, 
            gender: Optional[str]=Query(None), marital_status: Optional[str]=Query(None)):
    result = loan.get_total_by_feature(gender=gender, marital_status=marital_status)
    response.status_code = result.status
    return result