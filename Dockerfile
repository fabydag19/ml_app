# Set Python Version
FROM python:3.9

EXPOSE 5000

# Set Work Directory
WORKDIR /ml_app

# Copy files in work directory
ADD . /ml_app

# Install dependences from file
RUN pip install -r requirements.txt
RUN python -m spacy download it_core_news_sm

# Run app
CMD [ "python", "app.py"]