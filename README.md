
# Hotel Management System (HMS)

## Overview
Hotel Management System is a Python-based application designed to manage hotel operations including customer registration, room bookings, billing, and various services like dining, gaming, and shopping.

## Features
- **Customer Management**: Register and store customer details
- **Room Booking**: Reserve rooms with different categories (Ultra Royal, Royal, Elite, Budget)
- **Restaurant Billing**: Track dining expenses
- **Gaming Services**: Record gaming activities and charges
- **Fashion Shop**: Manage clothing purchases
- **Bill Management**: Generate and search customer bills

## Requirements
- Python 3.x
- MySQL Server
- `mysql-connector-python` library

## Installation
```bash
pip install mysql-connector-python
```

## Database Setup
The system automatically creates the `HMS` database and required tables on first connection.

## Usage
1. Run the program: `python main.py`
2. Enter MySQL credentials
3. Select operations from the menu:
    - Customer Details
    - Booking Record
    - Room Rent
    - Restaurant
    - Gaming
    - Fashion
    - Search Customer
    - Total Bill
    - Old Bill
    - EXIT

## Tables
- `C_DETAILS`: Customer information
- `BOOKING_RECORD`: Check-in/out dates
- `ROOM_RENT`: Room reservations
- `RESTAURENT`: Dining records
- `GAMING`: Gaming activities
- `FASHION`: Clothing purchases
- `TOTAL`: Final billing

## Notes
Update MySQL credentials in the code before deployment.
