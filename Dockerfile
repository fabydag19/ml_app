# Set Python Version
FROM python:3.9

EXPOSE 5001

# Set Work Directory
WORKDIR /app

# Copy files in work directory
ADD . /app

# Install dependences from file
RUN pip install -r requirements.txt

# Run app
CMD [ "python", "app.py"]