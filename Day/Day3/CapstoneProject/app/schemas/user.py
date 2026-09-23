# Define the Pydantic model that the fastapi uses to validate the incoming request bodies
# shapes the outgoing response bodies, and provides type hints for the IDE

from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from app.models.user import UserRole

class UserCreate(BaseModel):
    name: str = Field(..., min_length = 2, max_length = 100, description = "Full name of the user")
    email: EmailStr = Field(..., description = "Unique email address, used as login identifier")
    password: str = Field(..., min_length = 8, description = "Password")
    role: UserRole = Field(default = UserRole.EMPLOYEE,description = "one of: employee, support_engineer, team_lead, admin")

class UserResponse(BaseModel):
    # Shape the user as returned by the API
    id: str = Field(..., description = "Unique identifier for the user")
    name: str
    email: EmailStr
    role: UserRole
    created_at: datetime