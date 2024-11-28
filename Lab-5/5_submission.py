import yfinance as yf
import pandas as pd
from hmmlearn.hmm import GaussianHMM
import numpy as np
import matplotlib.pyplot as plt

ticker = 'MSFT' 
data = yf.download(ticker, start='2013-01-01', end='2023-01-01')

print(data.head())

data.to_csv('microsoft_stock_data.csv')

data = data[['Adj Close']]

data['Returns'] = data['Adj Close'].pct_change()

data = data.dropna()

print(data.head())
returns = data['Returns'].values.reshape(-1, 1)

model = GaussianHMM(n_components=2, covariance_type="diag", n_iter=1000)
model.fit(returns)

hidden_states = model.predict(returns)

data['Hidden State'] = hidden_states

print(data.head())
means = model.means_
covariances = model.covars_

print("Means of each hidden state:")
print(means)

print("\nCovariances (variances) of each hidden state:")
print(covariances)

transition_matrix = model.transmat_

print("Transition Matrix:")
print(transition_matrix)
plt.figure(figsize=(10, 6))
plt.plot(data['Adj Close'], label='Adjusted Close', color='black')

plt.scatter(data.index, data['Adj Close'], c=data['Hidden State'], cmap='coolwarm', marker='.', label='Hidden State')

plt.title('Stock Prices with Inferred Hidden States')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.show()

current_state = hidden_states[-1]
next_state_probabilities = transition_matrix[current_state]

print(f"Next state probabilities (current state {current_state}):")
print(next_state_probabilities)

next_state = np.argmax(next_state_probabilities)
print(f"Most likely next state: {next_state}")
