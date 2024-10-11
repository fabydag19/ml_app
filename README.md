# IT Incident Prediction

A web app that utilizes a machine learning model to predict the `problem_id` of an IT incident by inputting specific data into the platform.

## Description

This web application allows users to enter data related to an IT incident and receive a prediction for the associated `problem_id`. Users need to provide the following input data:

- **Short Description**: A brief summary of the incident.
- **Description**: A detailed description of the incident.
- **Impact Level**: The impact of the incident on business operations.
- **Urgency Level**: The urgency of resolving the incident
- **Priority Level**: The priority assigned to the incident based on its impact and urgency.

## Technologies Used

- **Backend:** Flask
- **Machine Learning:** Scikit-learn, spaCy, Pandas
- **Frontend:** HTML, CSS
- **Database:** MySQL
- **Deployment:** Docker

## Installation

To run the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/fabydag19/ml_app.git
   
2. Navigate to the project directory:
   ```bash
   cd ml_app

4. Build and start the Docker container for the app:
   ```bash
   docker-compose up -d

5. Access MySQL and create the database and table for users:
   ```bash
   docker exec -it ml_app-db-1 mysql -u root -p
   ```
   ```sql
   CREATE DATABASE mlapp;
   ```
   ```sql
   USE mlapp;
   ```
   ```sql
   CREATE TABLE users (
    id int auto_increment primary key not null,
    username varchar(255) unique not null,
    password_hash varchar(255) not null,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    is_active boolean default true,
    activation_date datetime default current_timestamp,
    deactivation_date datetime,
    last_login datetime
    );
   ```
   
6. Open your browser and go to `http://localhost:5001/` to use the app.

