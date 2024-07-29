import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    y = df['CSIRO Adjusted Sea Level']
    x = df['Year']

    # Create scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y, label='Data')

    # Create first line of best fit
    res = linregress(x, y)
    x_pred = range(1880, 2051)
    y_pred = res.slope * pd.Series(x_pred) + res.intercept
    ax.plot(x_pred, y_pred, 'r', label='Fit Line (1880-2050)')

    # Create second line of best fit
    new_df = df[df['Year'] >= 2000]
    new_x = new_df['Year']
    new_y = new_df['CSIRO Adjusted Sea Level']
    res_2 = linregress(new_x, new_y)
    x_pred2 = range(2000, 2051)
    y_pred2 = res_2.slope * pd.Series(x_pred2) + res_2.intercept
    ax.plot(x_pred2, y_pred2, 'green', label='Fit Line (2000-2050)')

    # Add labels, title, and legend
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()