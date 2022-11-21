Please run the following commands to make sure that you have all the required packages

pip install paytmchecksum
pip install Pillow
pip install python-decouple
pip install mysqlclient

Also make sure that you've configured the Database in settings.py and then please run the following commands

python manage.py makemigrations
python manage.py migrate

You can create a superuser and from the admin page you can add packages and news and they will appear on the homepage after being added.

In case you face any problem then please reach out to Avinash Ranjan at +91 9142177535 or Ravi at +91 7597663347