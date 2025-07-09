from flask import Flask, render_template, request, send_file
import yfinance as yf
import pandas as pd
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    # Get user input from the form
    ticker = request.form.get('ticker')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')

    # Fetch data using yfinance
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    if stock_data.empty:
        return "No data available for this stock or date range."

    # Convert data to Excel format
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        stock_data.to_excel(writer, index=True, sheet_name='Stock Data')
    output.seek(0)

    # Send the Excel file as response
    return send_file(output, as_attachment=True, download_name=f'{ticker}_stock_data.xlsx', mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

if __name__ == '__main__':
    app.run(debug=True)
