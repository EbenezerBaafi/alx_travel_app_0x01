# ALX Travel App 0x01

A Django REST Framework API for managing travel listings and bookings.

## Features

- RESTful API endpoints for Listings and Bookings
- Full CRUD operations (Create, Read, Update, Delete)
- Django REST Framework ViewSets
- API documentation with Swagger
- Token-based authentication support

## Prerequisites

- Python 3.8+
- pip
- virtualenv (recommended)

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/EbenezerBaafi/alx_travel_app_0x01.git
cd alx_travel_app_0x01
```

### 2. Create and Activate Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the root directory (use `.env.examples` as a template):

```bash
cp .env.examples .env
```

Edit `.env` and add your configuration:
```
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=your-database-url
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at `http://127.0.0.1:8000/`

## API Endpoints

### Listings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/listings/` | List all listings |
| POST | `/api/listings/` | Create a new listing |
| GET | `/api/listings/{id}/` | Retrieve a specific listing |
| PUT | `/api/listings/{id}/` | Update a listing (full) |
| PATCH | `/api/listings/{id}/` | Update a listing (partial) |
| DELETE | `/api/listings/{id}/` | Delete a listing |

### Bookings

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/bookings/` | List all bookings |
| POST | `/api/bookings/` | Create a new booking |
| GET | `/api/bookings/{id}/` | Retrieve a specific booking |
| PUT | `/api/bookings/{id}/` | Update a booking (full) |
| PATCH | `/api/bookings/{id}/` | Update a booking (partial) |
| DELETE | `/api/bookings/{id}/` | Delete a booking |

## API Documentation

Access the interactive API documentation:

- **Swagger UI:** `http://127.0.0.1:8000/swagger/`
- **ReDoc:** `http://127.0.0.1:8000/redoc/`

## Testing the API

### Using cURL

**List all listings:**
```bash
curl http://127.0.0.1:8000/api/listings/
```

**Create a listing:**
```bash
curl -X POST http://127.0.0.1:8000/api/listings/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Beach House", "description": "Beautiful property", "location": "Miami", "price_per_night": 200}'
```

**Update a listing:**
```bash
curl -X PATCH http://127.0.0.1:8000/api/listings/1/ \
  -H "Content-Type: application/json" \
  -d '{"price_per_night": 250}'
```

**Delete a listing:**
```bash
curl -X DELETE http://127.0.0.1:8000/api/listings/1/
```

### Using Postman

1. Import the API collection or manually create requests
2. Set the base URL to `http://127.0.0.1:8000`
3. Test each endpoint with appropriate HTTP methods

### Using Browser (Django REST Framework Browsable API)

Simply navigate to `http://127.0.0.1:8000/api/listings/` in your browser for an interactive interface.

## Project Structure

```
alx_travel_app_0x01/
├── alx_travel_app/          # Main project settings
│   ├── __init__.py
│   ├── settings.py          # Django settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py
│   └── asgi.py
├── listings/                # Listings app
│   ├── models.py            # Listing and Booking models
│   ├── serializers.py       # DRF serializers
│   ├── views.py             # ViewSets
│   └── urls.py              # App URL configuration
├── venv/                    # Virtual environment
├── .env                     # Environment variables
├── .gitignore
├── manage.py                # Django management script
└── requirement.txt          # Project dependencies
```

## Technologies Used

- **Django** - Web framework
- **Django REST Framework** - API framework
- **drf-yasg** - Swagger/OpenAPI documentation
- **python-decouple** - Environment variable management

## Development

### Running Tests

```bash
python manage.py test
```

### Creating Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Collecting Static Files

```bash
python manage.py collectstatic
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is part of the ALX Software Engineering program.

## Author

**Ebenezer Baafi**
- GitHub: [@EbenezerBaafi](https://github.com/EbenezerBaafi)

## Acknowledgments

- ALX Africa
- Django Documentation
- Django REST Framework Documentation