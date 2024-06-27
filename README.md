SpotMech
SpotMech is a web application built using Python and Django that helps drivers and vehicle users easily find nearby mechanics. The solution integrates Mapbox for handling location-related features, ensuring users can quickly locate the nearest mechanic to their current location.

Table of Contents
Introduction
Features
Installation
Usage
Configuration
API Reference
Contributing

Introduction
SpotMech addresses the common problem faced by drivers and vehicle users in finding reliable and nearby mechanics. With the integration of Mapbox, users can view a map of their surroundings and quickly identify the closest mechanic to their location. This project aims to provide a seamless and efficient solution for vehicle repair needs.

Features
User Authentication: Secure login and registration for users.
Location Services: Integration with Mapbox for real-time location tracking.
Mechanic Listings: Display a list of nearby mechanics based on the user's current location.
Mechanic Details: View detailed information about each mechanic, including contact information and services offered.
Reviews and Ratings: Users can rate and review mechanics to help others make informed decisions.
Search Functionality: Search for mechanics by name, location, or services provided.
Installation
To get started with SpotMech, follow these steps:

Clone the Repository:

bash
    
git clone https://github.com/yourusername/spotmech.git
cd spotmech
Create and Activate a Virtual Environment:

bash
    
python3 -m venv venv
source venv/bin/activate
Install Dependencies:

bash
    
pip install -r requirements.txt
Set Up the Database:

bash
    
python manage.py migrate
Create a Superuser:

bash
    
python manage.py createsuperuser
Run the Development Server:

bash
    
python manage.py runserver
Access the Application:

Open your browser and go to http://127.0.0.1:8000/.

Usage
User Registration and Login
Navigate to the registration page to create a new account.
After registering, log in with your credentials.
Finding Mechanics
Upon logging in, users will be directed to a map displaying their current location.
Nearby mechanics will be marked on the map.
Click on a mechanic's marker to view detailed information.
Reviewing Mechanics
Users can rate and review mechanics they have visited.
Reviews and ratings help others make informed choices.
Configuration
Mapbox Integration
To integrate Mapbox, you need an API key. Follow these steps:

Get a Mapbox API Key:

Sign up for a Mapbox account at Mapbox.
Create a new access token.
Configure the API Key:

In your Django settings file (settings.py), add your Mapbox API key:

python
    
MAPBOX_API_KEY = 'your_mapbox_api_key'
Environment Variables
For security and convenience, use environment variables to manage sensitive information. Create a .env file in your project root and add the following:

bash
    
SECRET_KEY=your_secret_key
DEBUG=True
MAPBOX_API_KEY=your_mapbox_api_key
Load these variables in your settings.py:

python
    
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = os.getenv('DEBUG')
MAPBOX_API_KEY = os.getenv('MAPBOX_API_KEY')
API Reference
Endpoints
GET /api/mechanics: Retrieve a list of mechanics.
GET /api/mechanics/{id}: Retrieve details of a specific mechanic.
POST /api/mechanics: Add a new mechanic (admin only).
PUT /api/mechanics/{id}: Update a mechanic's details (admin only).
DELETE /api/mechanics/{id}: Delete a mechanic (admin only).
Example Request
bash
    
curl -X GET http://127.0.0.1:8000/api/mechanics/
Contributing
We welcome contributions to SpotMech! To contribute, follow these steps:

Fork the Repository:

Click the "Fork" button on the top right of the repository page.

Clone Your Fork:

bash
    
git clone https://github.com/yourusername/spotmech.git
Create a Branch:

bash
    
git checkout -b feature/your-feature-name
Make Your Changes:

Implement your feature or fix the bug.

Commit Your Changes:

bash
    
git commit -m "Description of your changes"
Push to Your Fork:

bash
    
git push origin feature/your-feature-name
Create a Pull Request:

Go to the original repository and create a pull request.
