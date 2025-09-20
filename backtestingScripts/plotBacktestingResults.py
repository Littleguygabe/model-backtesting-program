import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def aggregateTotalPortfolioValue(tracking_df_arr):
    value_cols = [df['cumulative_return'] for df in tracking_df_arr]
    returns_df = pd.DataFrame(value_cols).T
    returns_df['portfolio_return'] = returns_df.sum(axis=1)
    returns_df['portfolio_return%'] =returns_df['portfolio_return']*100 

    return returns_df

def plotResults(tracking_df_arr):
    output_df = aggregateTotalPortfolioValue(tracking_df_arr)

    plt.figure(1,figsize=(12,8))
    plt.plot(output_df['portfolio_return%'],label='portfolio return %')

    # plot average regression line
    max_pr = output_df.tail(1)['portfolio_return%'].values[0]
    min_pr = output_df.head(1)['portfolio_return%'].values[0]
    plt.plot(np.linspace(min_pr,max_pr,len(output_df)),label='Average Return Regression Line')

    # plt.plot()


    plt.title('Total Portfolio Return Value Over Time')
    plt.xlabel('Days Since First Trade')
    plt.ylabel('Total Portfolio Return (%)')

    plt.grid(True)
    plt.legend()
    plt.show()

