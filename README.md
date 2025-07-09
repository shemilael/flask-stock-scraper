
# Stock Data Downloader - Python Flask App

This Python Flask web application allows users to download historical stock data in Excel format using the Yahoo Finance API (`yfinance`). The user simply enters a stock ticker symbol and selects a date range, and the app fetches the stock data for that range, converting it into an Excel file ready for download.

## Features

- **Stock Data Download**: Allows users to enter a stock ticker, a start date, and an end date to retrieve historical stock data.
- **Excel Export**: The stock data is exported in an Excel format for easy offline analysis.
- **User-Friendly Interface**: Simple web interface for entering the stock ticker and date range.

## Prerequisites

Before running the application, ensure that you have the following installed:

- Python 3.x
- Flask
- yfinance
- pandas
- openpyxl

To install the required dependencies, run:

```bash
pip install flask yfinance pandas openpyxl
```

## Application Structure

The project consists of two main components:

1. **Flask App (Python)**: This file contains the logic to handle user input, fetch stock data, and generate the Excel file.
2. **HTML Template (index.html)**: This is the front-end form where users can input stock tickers and select date ranges.

### Directory Structure

```plaintext
stock-data-downloader/
│
├── app.py           # Python Flask application file
├── templates/
│   └── index.html   # HTML template for the user interface
└── requirements.txt # List of dependencies
```

## Running the Application

1. Clone or download the repository.
2. Navigate to the project directory.
3. Run the Flask application using the following command:

```bash
python app.py
```

4. Open your web browser and go to `http://127.0.0.1:5000/`.
5. Enter a stock ticker, start date, and end date, then click **Download Data** to get the stock data in Excel format.

## Code Explanation

### Flask App (`app.py`)

- **Imports**: 
  - `Flask`, `render_template`, `request`, and `send_file` from `flask` handle web server functionality.
  - `yfinance` fetches stock data from Yahoo Finance.
  - `pandas` is used to convert the data into an Excel file format.
  - `BytesIO` is used to handle the in-memory byte stream for sending the file.

- **Routes**:
  - **`/`**: The homepage where the user can input the stock ticker and date range.
  - **`/download`**: A POST route that handles the data download by fetching the stock data and converting it into an Excel file.

- **Logic**:
  - The `download` route processes the form input (stock ticker, start date, and end date).
  - It fetches the stock data using `yfinance` and checks if the data is empty.
  - If data is available, it is converted into an Excel file using `pandas.ExcelWriter`.
  - The file is then sent to the user as a downloadable Excel file.

### HTML Template (`templates/index.html`)

The HTML template provides a simple form with the following inputs:
- **Stock Ticker**: A text input for the user to enter the stock symbol (e.g., "AAPL").
- **Start Date**: A date input for selecting the start date.
- **End Date**: A date input for selecting the end date.

When the form is submitted, the data is sent to the `/download` route in a POST request.

### Created by:

- Muntaqim Asbuch
- GitHub: [@shemilael](https://github.com/shemilael)
- Instagram: [@shemilael](https://www.instagram.com/shemilael)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
