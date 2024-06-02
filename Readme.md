# Car Search Web Application

This is a web application built with Django 4.2 and MySQL that allows users to search for cars based on various criteria (length, weight, velocity, color) and download the search results in XML format.

## Features

- Search for cars using multiple criteria simultaneously.
- Download the search results as an XML file.
- Pagination support for search results.
- Fully tested to ensure software quality and execution.

## Requirements

- Python 3.x
- Django 4.2
- MySQL

## Installation

1. **Clone the repository:**

    ```bash
    git clone git@github.com:russell310/project_car.git
    cd project_car
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the env:**

    Copy `.env.example` with `.env` and add necessary settings for your environment

5. **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

6. **Load initial data:**

    ```bash
    python manage.py populate_cars 100
    ```

7. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

8. **Access the application:**

    Open your web browser and go to http://localhost:8000/.

## Usage

- **Search for Cars:**
  - Use the search form to filter cars based on length, weight, velocity, and color.
  - Click the search button to view the results.

- **Download Search Results:**
  - Perform a search using the desired criteria.
  - Click the "Export to XML" button to download the search results as an XML file.

## Testing

### Run Tests

To run the tests, use the following command:

```bash
coverage run manage.py test
coverage report
```

This will run the tests and provide a coverage report.

### Static Code Analysis

#### Flake8
Run Flake8 to check for code style issues:

```bash
flake8 car
```

#### Bandit

Run Bandit to check for security issues:

```bash
bandit -r car
```

## Performance Testing with Locust

### Run Locust to test load

```bash
locust -f car/locustfile.py --host=http://localhost:8000
```

### Open Locust Web Interface

Open your web browser and go to http://localhost:8089.

### Configure and Start the Load Test

- Set the **Number of total users to simulate** (e.g., 100).
- Set the **Hatch rate** (number of users to spawn per second, e.g., 10).
- Click the **Start swarming** button to start the load test.

### Monitor the Test

Monitor the performance metrics in the Locust web interface, including requests per second, response times, and number of failures.

## Author

Hamim Al Mahdi Russell

## Contact

- Email: russell310@gmail.com
- LinkedIn: [linkedin.com/in/russell310](https://www.linkedin.com/in/russell310)
- GitHub: [github.com/russell310](https://github.com/russell310)
- Web: [hamim.dev](https://hamim.dev)

For any further questions or contributions, please contact me via email or LinkedIn.
