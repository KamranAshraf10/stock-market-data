# Stock Market Data

## Overview

The "Stock Market Data" project is designed to automate the process of gathering, cleaning, and integrating stock market data into the Stocks Telegraph website. Utilizing web scraping techniques, data is extracted daily from MarketWatch and Finviz, offering users up-to-date financial information through a REST API.

## Features

- **Data Scraping**: Automated scraping of stock market data from MarketWatch and Finviz.
- **Data Cleaning and Processing**: Cleans and processes the raw data to extract essential information.
- **REST API**: Provides a RESTful API to integrate the processed data into the Stocks Telegraph website, making it easily accessible for web applications.
- **Automation**: Utilizes a cron job for daily updates, ensuring the data remains current without manual intervention.

## Technologies

- **Python**: The core language used for scripting the data extraction and processing.
- **Django**: Employs Django framework for building the REST API and handling backend operations.
- **Windows Scheduler**: Utilizes Windows Scheduler to automate the daily task of data scraping and updating.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- Requests (Python library)
- BeautifulSoup (Python library)

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/<KamranAshraf10>/stock-market-data.git
```

2. Navigate to the project directory:

```bash
cd stock-market-data
```

3. Install the required Python libraries:

```bash
pip install -r requirements.txt
```

4. Set up the Django project (migrate and create a superuser):

```bash
python manage.py migrate
python manage.py createsuperuser
```

5. Run the Django development server:

```bash
python manage.py runserver
```

6. Schedule the cron job for daily data updates:

- Open Windows Task Scheduler and create a new task.
- Set the trigger to run the script daily at your specified time.
- Under Actions, specify the path to your Python executable and the path to `manage.py` with the `update_data` custom command as arguments.

## Usage

After starting the Django development server, you can access the REST API at:

```
http://localhost:8000/api/
```

Replace `localhost:8000` with your server's address and port if you're hosting it elsewhere.

## Contributing

Contributions to "Stock Market Data" are welcome. Please feel free to fork the repository, make changes, and submit pull requests. For major changes or new feature requests, please open an issue first to discuss what you would like to change.
