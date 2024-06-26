from fastapi import APIRouter, Depends, HTTPException, Path
from sqlalchemy.orm import Session
from ..database import get_db
from typing import Optional
from ..schemas import Message, MessageStatus
from typing import List
from datetime import datetime
from fastapi.security.api_key import APIKey
from ..auth import check_secret_key


from .. import crud

router = APIRouter(prefix="/messages", tags=["Messages"])

@router.get("/", summary="Get all messages", response_model=list[Message],)
def get_messages(start_date: datetime, end_date: datetime, path: str | None = "" , db: Session = Depends(get_db), secret_key: APIKey = Depends(check_secret_key)):
    
    if not start_date:
        raise HTTPException(status_code=400, detail="Start date is required")
    
    if not end_date:
        raise HTTPException(status_code=400, detail="End date is required")
    
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Start date is greater than end date")
    
    response = crud.get_messages(db, f"/{path}", end_date=end_date, start_date=start_date)
    
    if not response:
        raise HTTPException(status_code=404, detail="No messages found")
    return response

@router.get("/count", summary="Get message count", response_model=MessageStatus)
def get_message_status(start_date: datetime, end_date: datetime, path: str | None = "" , db: Session = Depends(get_db), secret_key: APIKey = Depends(check_secret_key)):
    
    if not start_date:
        raise HTTPException(status_code=400, detail="Start date is required")
    
    if not end_date:
        raise HTTPException(status_code=400, detail="End date is required")
    
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Start date is greater than end date")
    
    response = crud.get_message_status(db, f"/{path}", end_date=end_date, start_date=start_date)
    
    if not response:
        raise HTTPException(status_code=404, detail="No messages found")
    return response

@router.get("/sorted/size", summary="Get sorted message by size")
def get_sorted_messages_size(start_date: datetime, end_date: datetime, db: Session = Depends(get_db), secret_key: APIKey = Depends(check_secret_key)):
    
    if not start_date:
        raise HTTPException(status_code=400, detail="Start date is required")
    
    if not end_date:
        raise HTTPException(status_code=400, detail="End date is required")
    
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Start date is greater than end date")
    
    response = crud.get_sorted_message_size(db, end_date=end_date, start_date=start_date)
    
    if not response:
        raise HTTPException(status_code=404, detail="No messages found")
    return response

@router.get("/sorted/count", summary="Get sorted message by count")
def get_sorted_messages_count(start_date: datetime, end_date: datetime, db: Session = Depends(get_db), secret_key: APIKey = Depends(check_secret_key)):
    
    if not start_date:
        raise HTTPException(status_code=400, detail="Start date is required")
    
    if not end_date:
        raise HTTPException(status_code=400, detail="End date is required")
    
    if start_date > end_date:
        raise HTTPException(status_code=400, detail="Start date is greater than end date")
    
    response = crud.get_sorted_message_count(db, end_date=end_date, start_date=start_date)
    
    if not response:
        raise HTTPException(status_code=404, detail="No messages found")
    return response

@router.get("/simulate", summary="simulate messages")
def simulate_messages(count: int,secret_key: APIKey = Depends):
    return crud.simulate_messages( count=count)