# 1. Use an official Python runtime as a parent image
FROM python:3.12-slim-buster

# 2. Set the working directory in the container to /app
WORKDIR /app

# 3. Copy the current directory contents into the container at /app
COPY . /app

# 4. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Make port 8000 available to the world outside this container
EXPOSE 8000

# 6. Define environment variable
ENV DJANGO_SETTINGS_MODULE=electronic_sales.settings

# 7. Run django migrate and collectstatic when the container starts
CMD ["python", "manage.py", "migrate", "--noinput", "&&", "python", "manage.py", "collectstatic", "--noinput", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]
