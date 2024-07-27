# Set Python Version
FROM python:3.9

# Set Work Directory
WORKDIR /app

# Copy files in work directory
COPY . /app

# Install dependences
RUN pip install --no-cache-dir -r requirements.txt

# Run app
CMD ["python3", "app.py"]