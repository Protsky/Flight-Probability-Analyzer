import json
from collections import Counter, defaultdict
from datetime import datetime
from scipy.stats import poisson
import matplotlib.pyplot as plt

# Load data from JSON file
with open('data.json', 'r') as f:
    data = json.load(f)

# Initialize counters for flights by month
flights_by_month = defaultdict(Counter)

# Count flights by month
for flight in data:
    date = datetime.strptime(flight['date'], '%d.%m.%Y')
    month = date.month
    if flight['km'] > 700:
        flights_by_month[month]['flights'] += 1

# Calculate Poisson probabilities for each month
months = range(1, 13)
probs = []
for month in months:
    mu = flights_by_month[month]['flights']
    prob = 1 - sum([poisson.pmf(i, mu) for i in range(0, 6)])
    probs.append(prob)

# Create the bar chart
fig, ax = plt.subplots()
ax.bar(months, probs)
ax.set_xlabel('Month')
ax.set_ylabel('Probability')
ax.set_ylim([0, 1])
ax.set_xticks(months)
ax.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax.set_title('Probability of having at least 6 flights of more than 700 km')
plt.show()
