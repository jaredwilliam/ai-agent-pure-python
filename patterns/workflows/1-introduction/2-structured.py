import os
from openai import OpenAI
from pydantic import BaseModel

client = OpenAI(api_key=os.getenv("API_KEY"))

# ---------------------------------------------------------
# Step 1: Define the response format in a Pydantic model
# ---------------------------------------------------------


class CalendarEvent(BaseModel):
    name: str
    date: str
    participants: list[str]


my_name = CalendarEvent(name="Jared", date="2025-01-01", participants=["1,2,3"])
