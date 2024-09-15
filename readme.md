Hamrah Mechanic Clone
Hamrah Mechanic Clone is a Django REST Framework-based web application that allows users to post and browse car advertisements, similar to bama.ir. Users can list their cars for sale, browse available cars, and get notified via email or SMS when a specific car becomes available if it's not currently listed. This notification feature is managed using Celery and RabbitMQ.

Features
Car Listings: Users can post advertisements for cars they want to sell, complete with relevant details.
Browse Cars: Users can browse through available car listings by various filters like make, model, price, etc.
Notifications: If a car a user is interested in is not available, they can opt-in for an alert. When that specific car becomes available, they will receive an email or SMS notification.
Background Tasks: Asynchronous handling of notifications using Celery and RabbitMQ.
Technologies Used
Backend: Django, Django REST Framework (DRF)
Asynchronous Tasks: Celery, RabbitMQ
Database: (Specify which database you are using, e.g., PostgreSQL, SQLite)
Other Tools: (Include any other relevant libraries, APIs, or tools)
Installation
Prerequisites
Before setting up the project, ensure you have the following installed:

Python 3.x
Django
RabbitMQ
Celery
(Optional) PostgreSQL or your preferred database
Setup Instructions
Clone the repository:

bash
Copy code
git clone https://github.com/shayanostovari/Hamrah-mechanic-clone.git
cd Hamrah-mechanic-clone
Set up a virtual environment and activate it:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the database:

Configure the settings.py file with your database credentials.
Run the migrations:
bash
Copy code
python manage.py migrate
Start RabbitMQ (make sure RabbitMQ is installed and running):

bash
Copy code
rabbitmq-server
Start the Celery worker:

bash
Copy code
celery -A your_project_name worker --loglevel=info
Run the Django development server:

bash
Copy code
python manage.py runserver
Access the app at http://127.0.0.1:8000/.

Usage
Posting an Advertisement:

Users can sign up or log in to create and manage their car listings.
When adding a car, the user can fill in details such as make, model, year, price, and additional features.
Browsing Cars:

Users can view a list of available cars, filter by different parameters, and click on individual listings for more details.
Notifications:

If a desired car is not available, the user can subscribe for notifications. When the car is posted by someone else, an SMS or email alert will be sent automatically.
Celery and RabbitMQ Setup
Celery is used to handle the background task of sending email/SMS notifications when the desired car is available. RabbitMQ serves as the message broker between Django and Celery.

Start Celery: Ensure that Celery is running alongside RabbitMQ to handle task queues:

bash
Copy code
celery -A your_project_name worker --loglevel=info
Start RabbitMQ: Start the RabbitMQ server:

bash
Copy code
rabbitmq-server
