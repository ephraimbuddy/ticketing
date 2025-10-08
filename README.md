# Seamless Integration: Building Applications That Leverage Airflow's Database Migration Framework

## Overview

This project accompanies the Airflow Summit presentation **"Seamless Integration: Building Applications That Leverage Airflow's Database Migration Framework."** It showcases a reference application that demonstrates how teams can extend Airflow's powerful migration tools to their plugins/providers ensuring seamless migrations in the apps.

## About the Project

A simple plugin including a listener plugin that mocks creating a ticket for every failed dag and logs these tickets with their URL in a database table (that’s why we need a custom db manager!).


## Features
- **Database Migrations**: Utilizes Alembic for managing database schema changes, ensuring that your application's database evolves alongside Airflow's.
- **Event Listeners**: Implements Airflow listeners to react to DAG run events, such as failures, and trigger actions like ticket creation.
- **Ticketing System Integration**: This is a mock ticketing system that automatically creates tickets when DAG runs fail, demonstrating practical use cases for extending Airflow's capabilities.
- **SQLAlchemy ORM**: Leverages SQLAlchemy for database interactions.

## Getting Started
1. **Clone the Repository**: Start by cloning this repository to your local machine.
   ```bash
   git clone git@github.com:ephraimbuddy/ticketing.git
   ```
2. **Build the package**: Navigate to the project directory and build the package using hatchling.
   ```bash
   cd ticketing
   hatch build --clean
   ```
3. **Install the package**: Install the built package into your Airflow environment.
   ```bash
   pip install dist/ticketing-0.1.0-py3-none-any.wheel
   ```
4. **Configure the Database Manager**: Ensure that the database manager is set up to handle migrations for the ticketing application:
    ```bash
    export AIRFLOW__DATABASE__EXTERNAL_DB_MANAGERS="ticketing.db_manager.DRTDBManager"
    ```
5. **Run Migrations**: Use Airflow's CLI to run the database migrations for the ticketing application.
   ```bash
   airflow db migrate
   ```
6. **Start Airflow**: Launch your Airflow to start using the ticketing system.

7. **DB manager commands**: You can also use the db manager commands to manage migrations specifically for the ticketing app.
   ```bash
   airflow db-manager migrate "ticketing.db_manager:DRTDBManager"
   airflow db-manager downgrade "ticketing.db_manager:DRTDBManager" --to-version 0.1.0
   airflow db-manager reset "ticketing.db_manager:DRTDBManager" --skip-init
   ```
