Unit Conversion API (Backend)
A modular, enterprise-structured REST API built with Flask to handle precise calculations and conversions across diverse measurement categories (Length, Weight, Volume, Temperature, Area, and more). It operates entirely through mathematical normalization strategies without relying on static external database records.

Architecture & Project Structure
The engine utilizes a strict separation of concerns separating HTTP routing mechanics from underlying algebraic transformation frameworks:

├── app.py                         # Application execution entrypoint
├── controller/
│   └── unit_converter_controller.py # HTTP Route orchestration & API boundaries
├── service/
│   └── unit_converter_service.py    # Logic & normalization calculation
└── model/
    ├── models.py                  # DTO Contracts (ConversionResponse, Parameters)
    └── units.py                   # System Enums (SIPrefix, Length, Mass, etc.)

Setup & Installation
1, Install required dependencies:
Ensure you have Flask and its Cross-Origin Resource Sharing (CORS) security wrapper installed:
    pip install flask flask-cors
2, Navigate to the project directory:
    /unit_conversion/backend/src
3, Start the localized server:
Execute your core module bundle straight from your shell: python app.py
(The local development loop will initiate and start listening natively at http://127.0.0.1:8080/)

API Interface & Browser Testing
    - Endpoint Contract
        - URL Routing: /convert
        - HTTP Protocol: GET
        - Required Parameters String Matrix:
     Parameter           Name,     Expected Format,            Description,                             Example Target
        value,          String    (Numeric Format),      The physical scale number you want to evaluate,    586 or -12.5
        base_unit,      String    (Case-Insensitive),    The category Enum to reference,                    Length or Volume
        from_unit,      String    (Case-Insensitive),    Current systemic unit,                             kilometer
        to_unit,        String    (Case-Insensitive),    Target unit to scale into,                         mile

Live Browser Testing Examples
http://127.0.0.1:8080/convert?value=100&base_unit=Length&from_unit=KILOMETER&to_unit=MILE

Expected JSON Payload Response:
{
  "original_value": 100.0,
  "from_unit": "km",
  "converted_value": 62.1371,
  "to_unit": "mi"
}

http://127.0.0.1:8080/convert?value=-40&base_unit=Temperature&from_unit=DEGREE_CELSIUS&to_unit=FAHRENHEIT

Expected JSON payload Response:
{
  "converted_value": 32.0,
  "from_unit": "°C",
  "original_value": "0",
  "to_unit": "°F"
}

Guarded Error Handling (Non-Numeric Regex Trigger)
http://127.0.0.1:8080/convert?value=abc&base_unit=Length&from_unit=METER&to_unit=CENTIMETER

Expected JSON Error Feedback:

JSON
{
  "Message": "Provided 'value' is not valid."
}