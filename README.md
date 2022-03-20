 # Final Project in Text Mining: Analyze FED announcements

In this project, we analyzed announcements by the central bank of the United States, the Federal Reserve System (FED). In particular, we used Text Mining techniques, Machine Learning techniques to analyze minutes of Federal Open Market Committee’s past meetings in order to predict the future market movement direction after a new announcement is published.

### How To
Prerequisites: Code has been tested with Python 3.8.12.

#### Data Aquisition
1. Run 01_GetData.py to aquire all required resources
2. Run 02_CleanData.py to clean the data
3. Run 03_AddFinancialData to add the respective S&P500 index prices and interest rates to each minute / speech / statement / testimony entry

#### Analysis
Run the respective Jupyter Notebooks in each of the folders. We've prepared the following analysis: 
- Latent Dirichlet Allocation (LDA)
- Sentiment Analysis 
- Feature Extraction
