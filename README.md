# Vendor Management System with Performance Metrics

This Vendor Management System (VMS) is developed using Django and Django REST Framework. It allows users to manage vendor profiles, track purchase orders, and calculate vendor performance metrics.

## Features

1. **Vendor Profile Management:**
   - Create, retrieve, update, and delete vendor profiles.
   
2. **Purchase Order Tracking:**
   - Create, retrieve, update, and delete purchase orders.
   - Filter purchase orders by vendor.
   
3. **Vendor Performance Evaluation:**
   - Calculate performance metrics such as on-time delivery rate, quality rating average, response time, and fulfillment rate.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/vendor-management-system.git
   cd vendor-management-system
   
##Create a virtual environment:
-python3 -m venv venv
**source venv/bin/activate  # For Linux/Mac
**venv\Scripts\activate      # For Windows

##Install dependencies:
-pip install -r requirements.txt

##Apply migrations:
-python manage.py migrate

##Create a superuser (for admin access):
-python manage.py createsuperuser

##Run the development server:
-python manage.py runserver


# Vendor Management System with Performance Metrics

Access the admin panel at http://localhost:8000/admin/ to add vendors and purchase orders.

## API Endpoints

### Vendor Endpoints:
- POST /api/vendors/
- GET /api/vendors/
- GET /api/vendors/{vendor_id}/
- PUT /api/vendors/{vendor_id}/
- DELETE /api/vendors/{vendor_id}/

### Purchase Order Endpoints:
- POST /api/purchase_orders/
- GET /api/purchase_orders/
- GET /api/purchase_orders/{po_id}/
- PUT /api/purchase_orders/{po_id}/
- DELETE /api/purchase_orders/{po_id}/

### Vendor Performance Endpoint:
- GET /api/vendors/{vendor_id}/performance

## Authentication

API endpoints are secured with token-based authentication. To obtain a token:

1. Send a POST request to /api/token/ with username and password.
2. Include the token in the Authorization header for subsequent requests: `Authorization: Bearer <token>`.





