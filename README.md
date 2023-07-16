# Django Ecommerce Website
## Installation
Clone the repository:

```
git clone https://github.com/your-username/Baigiamasis-darbas-new.git
```

Navigate to the project directory:

```
cd django-ecommerce
```
Create a virtual environment:

```
python -m venv venv
```
Activate the virtual environment:

For Windows:

```
venv\Scripts\activate
```
For macOS/Linux:

```
source venv/bin/activate
```
Install the required dependencies:

```
pip install -r requirements.txt
```
Set up the database (I'm using PostGreSQL change the credentials for it, or use another database):

```
python manage.py migrate
```
Create a superuser (admin):

```
python manage.py createsuperuser
```
Start the development server:

```
python manage.py runserver
```
Access the website at http://localhost:8000 in your browser.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

*  Fork the repository.
*  Create a new branch for your feature or bug fix.
*  Make your changes and commit them with descriptive messages.
*  Push your changes to your fork.
*  Submit a pull request, explaining your changes in detail and referencing any relevant issues.

## Acknowledgements

* Special thanks to the Django community for their excellent documentation and continuous support.
