# README
# Yelp Reviews Sentiment Analysis

## Repository Contents
This repository contains all the necessary files and scripts for conducting sentiment analysis on Yelp restaurant reviews in the city of Philadelphia, PA. The analysis aims to determine whether compound sentiment scores based on user reviews, in addition to the average star review and the number of such reviews, can help predict a restaurant’s likelihood of remaining open or closing down.

## 1. Software and Platform

### Programming Languages and Software
- **Python**: For data preprocessing, sentiment analysis, and merging datasets
- **R**: For developing and evaluating the decision tree model

### Python Packages
- `pandas` – Data manipulation
- `nltk` – Natural Language Processing, including VADER sentiment analysis
- `json` – Parsing JSON data
- `matplotlib` – General graphing purposes for exploratory data analysis

### R Packages
- `tree` – Decision tree modeling
- `pROC` – ROC curve and AUC evaluation
- `dplyr` – Data filtering
- `ggplot2` – General graphing purposes for the decision tree modeling
- `patchwork` – Assistance for graph layouts (i.e. stacking graphs together)
- `kableExtra` – Assistance for table layouts 

### Platform Compatibility
Developed and tested on Mac, but should work on Windows and Linux with appropriate installations.

## 2. Project Folder Structure

```
📂 Yelp-Sentiment-Analysis  
 ├── 📂 data/  
 ├──── 📂 INITIAL/
 │   │   ├── business.json  
 │   │   ├── review.json  
 ├──── 📂 FINAL/
 │   │   ├── FINAL_yelp_dataframe.csv  
 │   │ YelpAnalysisDataAppendix.pdf
 │  
 ├── 📂 scripts/  
 │   ├── 01_proprocessing_sentiment.py  
 │   ├── 02_eda.R
 │   ├── 03_decision_tree.Rmd
 │  
 ├── 📂 output/plots/  
 │   ├── exploratory_plots.jpeg
 │  
 ├── README.md   
```



## 3. Instructions for Reproducing Results

### Stage 1: Data Preparation and Sentiment Analysis in Python
- Download the Yelp Open Dataset from Yelp Dataset.
- Extract the JSON files and place them in your `data/` directory.
- Run `01_proprocessing_sentiment.py` to do the following:
  - Open the following JSON files in Python: `reviews.json` and `business.json`
  - If these lines do not work, you may need to run `pip install json` in your console if you do not have this package installed already.
  - Subset the data to include only restaurants based in Philadelphia.
  - Run a sentiment analysis using the VADER package.
  - If this doesn’t work, you may need to run `pip install nltk` in your console if you do not have this package installed already.
  - Merge the data frames that are associated with the general business information (from `business.json`) and the compound score from the sentiment analysis conducted on the dataframe associated with the `reviews.json` file. 
  - This code file also exports the final merged dataframe as a `.csv` file to conduct further analysis. This file is called `FINAL_yelp_dataframe.csv`. Make sure to save the location of the file to use in future stages!

### Stage 2: Exploratory Data Analysis in R
- Open up RStudio to run `02_eda.R`
- You may need to use the following commands in the R console to install the appropriate packages (if you don’t have them already):
  ```r
  install.packages("dplyr")
  install.packages("ggplot2")
  install.packages("patchwork")
  ```
- Import `FINAL_yelp_dataframe.csv` from wherever you have this saved.
- Run the code file to obtain the following graphs:
  - Distribution of Open and Closed Restaurants in Philadelphia
  - Distribution of Average Star Rating by Restaurant Status for Philadelphia
  - Histogram of Average Star Rating by Restaurant Status for Philadelphia
  - Distribution of Average Compound Score by Restaurant Status for Philadelphia

### Stage 3: Decision Tree Modeling and Evaluation in R
- Once again, open up RStudio to run `03_decision_tree.Rmd`
- You may need to use the following commands in the R console to install the appropriate packages (if you don’t have them already):
  ```r
  install.packages("kableExtra")
  install.packages("pROC")
  install.packages("tree")
  ```
- Import `FINAL_yelp_dataframe.csv` from wherever you have this saved.
- Run the code file to obtain the relevant figures. Since we are using the `kableExtra` package, all figures will only appear when you knit your `.Rmd` file. Knitting to HTML has been found to be the easiest way to do this. The following is an outline of the figures:
  - **Baseline Decision Tree** (contains tree)
  - **Pruning Decision Tree** (contains cross-validation plot and tree)
  - **Assessing Model Performance** (contains the ROC curve)
  - **Table Formatting** (contains Decision Tree Performance Metrics and Confusion Matrix)

