# Django Ecommerce Website
## Installation
Clone the repository:

shell
Copy code
git clone https://github.com/your-username/django-ecommerce.git
Navigate to the project directory:

shell
Copy code
cd django-ecommerce
Create a virtual environment:

shell
Copy code
python -m venv venv
Activate the virtual environment:

For Windows:

shell
Copy code
venv\Scripts\activate
For macOS/Linux:

shell
Copy code
source venv/bin/activate
Install the required dependencies:

shell
Copy code
pip install -r requirements.txt
Set up the database:

shell
Copy code
python manage.py migrate
Create a superuser (admin):

shell
Copy code
python manage.py createsuperuser
Start the development server:

shell
Copy code
python manage.py runserver
Access the website at http://localhost:8000 in your browser.
