## 1. Problem Understanding
Marketing teams spend the same budget on all customers, but not all customers respond equally.
This project analyses customer profiles, spending patterns, and campaign responses to find:
- Who are the most valuable customers?
- Who are the most responsive customers?
- Which segments should be targeted in the next campaign?

## 2. Approach
1.  **Data Loading:** Loaded marketing data in Google Colab using Python / Pandas.
2.  **Cleaning:** Handled missing values in Income, removed duplicates, fixed data types.
3.  **Feature Engineering:** Created `Age = 2026 - Year_Birth`, `AgeBand` (Young <30, Middle 30-45, Mature 45-60, Senior 60+), and `MntTotal` as total spend.
4.  **EDA & Segmentation:** Grouped customers by Education, Country, and AgeBand.
5.  **Metrics:** Calculated Response Rate (%), Avg Spend, and Customer Count per segment.
6.  **SQL:** Created tables, views, and analytical queries to validate the same metrics.
7.  **Dashboard:** Built Streamlit dashboard with filters and visuals for stakeholders.

## 3. Key Findings
- **Most Responsive by Education:** Customers with Graduation / 2n Cycle education show the highest response rate.
- **Most Responsive by Country:** Response rate varies by country. The top country shows ~20% response rate, much higher than others. Campaigns should not be equal across all countries.
- **Most Valuable by Age:** Mature (45-60) and Senior (60+) customers have the highest Average Spend.
- **Segment-Level Summary:** High-spend segments are not always the highest responders. Value + Response must be used together for targeting.
- 
##dashboard screenshots

<img width="554" height="323" alt="m1" src="https://github.com/user-attachments/assets/fca4af73-2441-4cf5-9fcd-afeb34533958" />
<img width="522" height="334" alt="m2" src="https://github.com/user-attachments/assets/1b1d308f-b34e-487e-a07d-ef2b0b72d51b" />


## 4. Setup Instructions

### How to Run Notebook
1. Open `marketing_data.ipynb` in Google Colab.
2. Upload `marketing_data.csv` or mount Google Drive.
3. Run all cells: Runtime > Run all.
### How to Run Dashboard
```bash
pip install -r requirements.txt
streamlit run app.py





