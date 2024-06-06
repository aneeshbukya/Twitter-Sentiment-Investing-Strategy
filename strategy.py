import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import yfinance as yf

plt.style.use('ggplot')

# Load cleaned data
sentiment_df = pd.read_csv("sentiment_data_new.csv")

# Convert date column to datetime
sentiment_df['date'] = pd.to_datetime(sentiment_df['date'])

# Set date and symbol as the index
sentiment_df = sentiment_df.set_index(['date', 'symbol'])

# Calculate engagement ratio
sentiment_df['engagement_ratio'] = sentiment_df['twitterComments'] / sentiment_df['twitterLikes']

# Filter stocks with low engagement
sentiment_df = sentiment_df[(sentiment_df['twitterLikes'] > 20) & (sentiment_df['twitterComments'] > 10)]

# Aggregate data by month and symbol
aggregated_df = (sentiment_df.reset_index('symbol').groupby([pd.Grouper(freq='ME'), 'symbol'])
                 [['engagement_ratio']].mean())

# Rank stocks by engagement ratio within each month
aggregated_df['rank'] = (aggregated_df.groupby(level=0)['engagement_ratio']
                         .transform(lambda x: x.rank(ascending=False)))

# Filter top 5 ranked stocks each month
filtered_df = aggregated_df[aggregated_df['rank'] < 6].copy()
filtered_df = filtered_df.reset_index(level=1)
filtered_df.index = filtered_df.index + pd.DateOffset(1)
filtered_df = filtered_df.reset_index().set_index(['date', 'symbol'])

# Get unique dates and stocks list
dates = filtered_df.index.get_level_values('date').unique().tolist()
fixed_dates = {}
for d in dates:
    fixed_dates[d.strftime('%Y-%m-%d')] = filtered_df.xs(d, level=0).index.tolist()

stocks_list = sentiment_df.index.get_level_values('symbol').unique().tolist()

# Download stock prices data
prices_df = yf.download(tickers=stocks_list, start='2021-01-01', end='2023-03-01')

# Calculate log returns
returns_df = np.log(prices_df['Adj Close']).diff().dropna()

# Construct portfolio returns
portfolio_df = pd.DataFrame()
for start_date in fixed_dates.keys():
    end_date = (pd.to_datetime(start_date) + pd.offsets.MonthEnd()).strftime('%Y-%m-%d')
    cols = fixed_dates[start_date]
    temp_df = returns_df[start_date:end_date][cols].mean(axis=1).to_frame('portfolio_return')
    portfolio_df = pd.concat([portfolio_df, temp_df], axis=0)

# Download NASDAQ-100 index data
qqq_df = yf.download(tickers='QQQ', start='2021-01-01', end='2023-03-01')
qqq_ret = np.log(qqq_df['Adj Close']).diff().to_frame('nasdaq_return')

# Merge portfolio and NASDAQ returns
portfolio_df = portfolio_df.merge(qqq_ret, left_index=True, right_index=True)

# Calculate cumulative returns
portfolios_cumulative_return = np.exp(np.log1p(portfolio_df).cumsum()).sub(1)

# Plot cumulative returns
portfolios_cumulative_return.plot(figsize=(16, 6))
plt.title('Twitter Engagement Ratio Strategy Return Over Time')
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1))
plt.ylabel('Return')
plt.show()
