#Twitter Engagement Ratio Investment Strategy

Project Overview

This project aims to develop and backtest an investment strategy based on Twitter engagement ratios for various stocks. By analyzing Twitter comments and likes, the strategy identifies the top five stocks each month with the highest engagement ratios and constructs a portfolio based on these stocks. The performance of this portfolio is then compared against the NASDAQ-100 index (QQQ).

Data

Input Data
sentiment_data.csv: Contains Twitter sentiment data for various stocks, including the number of likes and comments.
Output Data
sentiment_data_new.csv: A cleaned version of sentiment_data.csv with rows containing the word "ATVI" removed.
Steps to Execute the Project

Data Cleaning

Remove rows containing the word "ATVI" from sentiment_data.csv.
Convert the date column to datetime format and set the date and symbol as the index.
Calculate the engagement ratio as the number of Twitter comments divided by the number of Twitter likes.
Filter out stocks with low engagement (less than 20 likes or 10 comments).
Data Aggregation and Ranking

Aggregate the data by month and symbol, calculating the mean engagement ratio for each group.
Rank stocks within each month based on their engagement ratio.
Filter the top 5 ranked stocks for each month.
Portfolio Construction

Identify unique dates and corresponding top-ranked stocks.
Download stock price data using yfinance for the identified stocks.
Calculate daily log returns for each stock.
Construct a portfolio return series by averaging the returns of the top-ranked stocks each month.
Benchmark Comparison

Download NASDAQ-100 index data using yfinance.
Calculate daily log returns for the NASDAQ-100 index.
Merge portfolio returns with NASDAQ-100 returns for comparison.
Calculate cumulative returns for both the portfolio and the NASDAQ-100 index.
Visualization

Plot cumulative returns of the portfolio and the NASDAQ-100 index over time.
Dependencies

pandas
numpy
matplotlib
yfinance
How to Run the Project

Set up the environment:

Ensure you have Python installed (preferably version 3.7 or higher).
Install the required packages using pip:
sh
Copy code
pip install pandas numpy matplotlib yfinance
Run the Data Cleaning Script:

Execute the script to remove rows containing "ATVI" from the input data and save the cleaned data.
sh
Copy code
python clean_data.py
Run the Main Script:

Execute the main script to perform the analysis and generate the plot.
sh
Copy code
python main.py
Files

clean_data.py: Script to remove rows containing "ATVI" from the input data.
main.py: Main script that performs the data analysis, constructs the portfolio, and generates the plot.
sentiment_data.csv: Input file containing raw sentiment data.
sentiment_data_new.csv: Output file containing cleaned sentiment data.
Results

The project produces a plot showing the cumulative returns of the Twitter engagement ratio strategy compared to the NASDAQ-100 index. This visualization helps in evaluating the performance of the strategy over the specified period.

Contact

For any queries or further information, please contact [Your Name] at [Your Email].
