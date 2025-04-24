from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr
from tasks import send_email_task

app = FastAPI(title="Email Notification Service")

# 📥 Структура тела запроса
class EmailRequest(BaseModel):
    to: EmailStr
    subject: str
    body: str

@app.post("/send-email")
def send_email_endpoint(data: EmailRequest):
    try:
        send_email_task.delay(data.to, data.subject, data.body)
        return {"status": "ok", "message": "Email task added to queue"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))