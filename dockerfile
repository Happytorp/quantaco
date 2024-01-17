FROM python:3.9

WORKDIR /customer_management_project

COPY requirements.txt /customer_management_project

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /customer_management_project

RUN python manage.py migrate

# Change CMD to bind to all available network interfaces
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Expose the port on which Django will run
EXPOSE 8000
