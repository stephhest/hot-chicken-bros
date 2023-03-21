from pydantic import BaseModel
from datetime import date, time
from typing import Optional

class Error(BaseModel):
    message: str

class MenuItemIn(BaseModel):
    name: str
    description: str
    price: float
    category: Optional(str)
    available: bool

class MenuItemOut(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: Optional(str)
    available: bool

class HeatLevelIn(BaseModel):
    name: str
    description: Optional(str)
    score: int

class HeatLevelOut(BaseModel):
    id: int
    name: str
    description: Optional(str)
    score: int

class EventIn(BaseModel):
    title: str
    location: str
    date: date
    start_time: time
    end_time: time

class EventOut(BaseModel):
    id: int
    title: str
    location: str
    date: date
    start_time: time
    end_time: time

class PickupSlotIn(BaseModel):
    event_id: int
    time: time
    max_mains: int

class PickupSlotOut(BaseModel):
    id: int
    event_id: int
    time: time
    max_mains: int
    ordered_mains: int

class CartOut(BaseModel):
    id: int
    status: str
    total: float

class CartItemIn(BaseModel):
    cart_id: int
    menu_item_id: int
    heat_level_id: int
    quantity: int

class CartItemOut(BaseModel):
    id: int
    cart_id: int
    menu_item_id: int
    heat_level_id: int
    quantity: int

class OrderIn(BaseModel):
    cart_id: int
    existing_user_id: Optional(int)
    pickup_name: str
    customer_email: str
    customer_phone: str
    customer_venmo: Optional(str)
    event_id: Optional(int)
    pickup_slot_id: Optional(int)
    order_status: str
    payment_status: str

class OrderOut(BaseModel):
    id: int
    cart_id: int
    existing_user_id: Optional(int)
    pickup_name: str
    customer_email: str
    customer_phone: str
    customer_venmo: Optional(str)
    event_id: Optional(int)
    pickup_slot_id: Optional(int)
    order_status: str
    payment_status: str
