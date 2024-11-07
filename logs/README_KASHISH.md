# Log Processing API

This Django-based API processes log data and provides statistical insights for each customer. It includes endpoints to
load log data, check the API health, and retrieve customer-specific statistics.

## Table of Contents

1. [Project Setup](#project-setup)
2. [MySQL Configuration](#mysql-configuration)
3. [Running the Application](#running-the-application)
4. [API Endpoints](#api-endpoints)
5. [Loading Data](#loading-data)

---

## Project Setup

To get started, follow these steps to set up your environment and install the necessary dependencies.

### Prerequisites

- **Python 3.8+**: Install Python from [python.org](https://www.python.org/).
- **MySQL**: Ensure you have a MySQL server running locally or remotely.
- **Virtual Environment** (recommended): Use a virtual environment to isolate dependencies.

### Step 1: Clone the Repository

```bash
git clone https://github.com/kashishbest/rated-r-coding-challenge/tree/ksinghal/
cd rated-r-coding-challenge/logs
```

### Step 2: Set Up the Virtual Environment

- **Create a virtual environment**:

    ```bash
    python -m venv venv
    ```

- **Activate the virtual environment**:

    - **macOS/Linux**:

    ```bash
    source venv/bin/activate
    ```

    - **Windows**:

    ```bash
    .\venv\Scripts\activate
    ```
### Step 3: Install Dependencies

Install the required Python packages listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### MySQL Configuration

The application requires a MySQL database to store and retrieve log data. Configure the MySQL settings in `config.ini`.
#### Step 1: Create a MySQL Database

- **Log in to your MySQL server**:

    ```bash
    mysql -u root -p
    ```

- **Create a new database**:

  ```sql
  CREATE DATABASE log_db;
  ```

- **Create a user and grant privileges**:

  ```sql
  CREATE USER 'log_user'@'localhost' IDENTIFIED BY 'your_password';
  GRANT ALL PRIVILEGES ON log_db.* TO 'log_user'@'localhost';
  FLUSH PRIVILEGES;
  ```

#### Step 2: Configure MySQL in `config.ini`

In the project root, locate or create `config.ini` and configure it as follows:

```ini
[mysql]
DATABASE_NAME = log_db
USER = log_user
PASSWORD = your_password
HOST = localhost
PORT = 3306
```

Ensure `config.ini` is not checked into version control, especially if it contains sensitive information.
#### Step 3: Run Migrations

Apply migrations to create the necessary database tables:

```bash
python manage.py migrate
```

### Running the Application

After setting up the database and installing dependencies, you can start the Django development server:

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

### API Endpoints

The following API endpoints are available:
- **Health Check**

  Endpoint: /health/
  Method: GET
  Description: Returns a simple JSON response to confirm that the server is running.
  
  ```bash
  
  curl -X GET http://127.0.0.1:8000/health/
  ```
  Response:
  
  ```json
  
  {
      "status": "ok"
  }
  ```
- **Customer Statistics**

  Endpoint: /customers/<str:id>/stats/
  Method: GET
  Description: Retrieves daily statistics for a specific customer, starting from a given date.

  - **Parameters**:
     - id: Customer ID (e.g., cust_42)
     - from: Start date in YYYY-MM-DD format
  
   ```bash
     curl -X GET "http://127.0.0.1:8000/customers/cust_42/stats?from=2024-10-01"
   ```
   Response:
  
   ```json
  {
    "customer_id": "cust_42",
    "from_date": "2024-10-01",
    "stats": {
        "total_successful_requests": 150,
        "total_failed_requests": 25,
        "uptime": 85.71,
        "average_latency": 0.123,
        "median_latency": 0.115,
        "p99_latency": 0.300
    }
  }
   ```
### Load Log Data

Endpoint: `/load`
Method: `POST`
Description: Loads log data from a specified file (`api_requests.log`) into the database.

Example:

```bash
curl -X POST http://127.0.0.1:8000/load
```

Response:

```json
{
"status": "done"
}
```

### Loading Data

To load log data into the database, place the log file (`api_requests.log`) in the project root or specify its path in your code. This file is parsed and processed in batches to avoid memory overload when dealing with large datasets.

1. Use the `SimpleLogParser` to parse each log entry.
2. Process the file using `LogFileProcessor`.
3. Use `bulk_create` to insert log entries into the database efficiently.

#### Loading Data Using Standalone Script

This project includes a standalone script that allows you to load log data directly into the database without calling an API endpoint. This is useful for loading large files on demand.
- **Usage**

Ensure your virtual environment is activated:

```bash

# macOS/Linux
source venv/bin/activate

# Windows
.\venv\Scripts\activate
```
Run the script with the following command:
```bash

python logs/runner.py
```
Replace path/to/your_script.py with the actual path to the standalone script.

