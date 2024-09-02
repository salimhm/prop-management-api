# prop-management-api
A simple RESTful API for managing properties, tenants and payments written in Python (Django). It allows authenticated users to perform CRUD operations on properties, manage tenants and track rental payments.
## Features
- CRUD operations for properties, tenants, and rental payments
- Filtering and sorting for properties
- JWT authentication for secure access
- Email notifications for due payments
## Installation

### Prerequisites

- Python 3.8+
- Django 5.1
- Django REST Framework
- Docker
### Setup

1. Clone the repository.
2. Create a .env file, go to this site => djecrety . ir (remove space) to generate your Django secret key add it to the .env (a .env.sample is provided).
3. In the root directory (where your 'Dockerfile' is located), execute the following commands:
   - sudo docker build -t propertymanagement .
   - sudo docker run -d -p 8000:8000 --name prop-api propertymanagement
## Usage
### Base URL
The base URL for the API is: http://localhost:8000/api/
1. Create an account by making a POST request to ```/api/auth/register/```
   - Example: ```curl -X POST http://localhost:8000/api/auth/register/ -H "Content-Type: application/json" -d '{"name": "John", "email": "john@lol.com", "password": "YourSillyPassword"}'```
2. Get your JWT token by making a request to ```/api/token/```
	- Example: ```curl -X POST http://localhost:8000/api/token/ -H "Content-Type: application/json" -d '{"name": "John", "email": "john@lol.com", "password": "YourSillyPassword"}'```
3. Now grab your ACCESS token, add the necessary headers and include it with each request to consume the API
	- Example:
 		- For POST requests: ```curl -X POST http://localhost:8000/api/property/add/ -H "Content-Type: application/json" -H "Authorization: Bearer <TOKEN>"```
	 	- For GET requests: ```curl http://localhost:8000/api/property/ -H "Authorization: Bearer <TOKEN>"```

## Available Endpoints
### ```POST /api/property/add/```
- Create a property, the following are the request body of the payload
  - ```name```: Name of the property
  - ```type```: Type of the property (Appartment, Villa, land...)
  - ```address```: The location of the property
  - ```num_units```: The number of units the property contains
  - ```rental_cost```: The cost of the property
### ```GET /api/property/{id}/```
- Retrieve a property. This one simply returns the details of a single property.
### ```PUT /api/property/{id}/```
- Update a property. It takes the same request body as the first endpoint.
### ```GET /api/property/
- Retrieve all the properties the user has created.


### ```POST /api/tenant/add/```
- Create a tenant and associate it with a property. It accepts the following as its request body:
  - ```property```: id of the property the tenant is occupying
  - ```name```: Name of the tenant
  - ```email```: Email
  - ```phone```: Phone number
  - ```occupied_section```: Occupied section
### ```GET /api/tenant/{id}```
- Retrieve a tenant. Returns all the information about a single tenant.
### ```PUT /api/tenant/{id}```
- Update a tenant. It takes the same request body as the first endpoint of the tenant.
### ```GET /api/tenant```
- Retrieve all the tenants create by the user

### ```POST /api/payments/add/```
- Create a payment and associate it with a tenant. It accepts the following as its request body:
  - ```tenant```: tenant id
  - ```status```: either ```paid``` or ```unpaid```
  - ```date```: the date the payment was made
  - ```due_date```: payment due_date (used for sending email reminders)
### ```PUT /api/payments/{id}/```
- Update a payment. It takes the same request body as the first endpoint of the payment endpoint.
### ```GET /api/payments/```
- Retrieve all the payments of all the tenants.

## Filters and ordering (All case insensitive)
### Filters
```GET /api/property/?type=Appartment```
- Returns all the properties that are of type Appartment (works with appartment, aPPartmEnt...)
```GET /api/property/?location=42 St, UK```
- Returns all the properties that have the given address
```GET /api/property/?min_rental_cost=1000```
- Returns all the properties that are less than or equal to the given amount
```GET /api/property/?max_rental_cost=1000```
- Returns all the properties that are greater than or equal to the given amount

### Ordering
```GET /api/property/?ordering=rental_cost```
- Order by rental cost in ascending order
```GET /api/property/?ordering=-rental_cost```
- Order by rental cost in descending order
```GET /api/property/?ordering=type```
- Order by type in ascending order
```GET /api/property/?ordering=-type```
- Order by type in descending order
```GET /api/property/?ordering=address```
- Order by address (location) in ascending order
```GET /api/property/?ordering=-address```
- Order by address (location) in descending order
