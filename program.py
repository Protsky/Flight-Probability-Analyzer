import json
from collections import Counter, defaultdict
from datetime import datetime
from scipy.stats import poisson
import matplotlib.pyplot as plt
import numpy as np

# Set the minimum distance requirement for a flight to be included in the analysis
min_distance = 300

# Set the number of flights to analyze
num_flights = 2

# Load data from JSON file
with open('dataDavide.json', 'r') as f:
    data = json.load(f)

# Initialize counters for flights by week
flights_by_week = defaultdict(Counter)

# Count flights by week
for flight in data:
    date = datetime.strptime(flight['date'], '%d.%m.%Y')
    week = int(date.strftime("%U"))
    if flight['km'] > min_distance:
        flights_by_week[week]['flights'] += 1

# Calculate Poisson probabilities for each week
weeks = range(1, 53)
probs = []
for week in weeks:
    mu = flights_by_week[week]['flights']
    prob = 1 - sum([poisson.pmf(i, mu) for i in range(0, num_flights)])
    probs.append(prob)

# Calculate 95% confidence interval for each probability
z = 1.96  # 95% confidence interval z-score
n = sum([flights_by_week[week]['flights'] for week in weeks])
se = np.sqrt(np.array(probs) * (1 - np.array(probs)) / n)
ci = z * se

# Set the x-axis labels
labels = ['Week {}'.format(week) for week in weeks]

# Create the bar chart
plt.bar(weeks, probs, align='center', alpha=0.5)

# Add the y-axis label
plt.ylabel('Probability of more than {} flights (> {} km)'.format(num_flights, min_distance))

# Add the title
plt.title('Weekly probability of more than {} flights (> {} km)'.format(num_flights, min_distance))

# Add the error bars
plt.errorbar(weeks, probs, yerr=ci, fmt='none', capsize=3)

# Show the plot
plt.show()
