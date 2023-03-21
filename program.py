import json
from collections import Counter, defaultdict
from datetime import datetime
from scipy.stats import poisson

# Load data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Initialize counters for flights by month
flights_by_month = defaultdict(Counter)

# Count flights by month
for flight in data:
    date = datetime.strptime(flight['date'], '%d.%m.%Y')
    month = date.month
    if flight['km'] > 200:
        flights_by_month[month]['flights'] += 1

# Calculate Poisson probabilities for each month
for month in range(1, 13):
    mu = flights_by_month[month]['flights']
    prob = 1 - sum([poisson.pmf(i, mu) for i in range(0, 6)])
    print(f"Probability of having at least 6 flights of more than 700 km in month {month}: {prob*100:.2f}%")
