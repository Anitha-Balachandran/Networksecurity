# Step 1: Use the official Python image from the Docker Hub - baseimage
FROM python:3.10-slim-buster

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the local application code to the container
COPY . /app

# Step 4: Install the required dependencies from the requirements.txt file
RUN apt update -y && apt install awscli -y
RUN apt-get update && pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port on which the Flask app will run
#EXPOSE 5000

# Step 6: Set the environment variable to run Flask in production mode
#ENV FLASK_APP=app.py

# Step 7: Command to run the Flask app
CMD ["python3", "app.py"]