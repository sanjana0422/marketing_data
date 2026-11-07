import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Marketing Dashboard", layout="wide")
st.title("📊 Marketing Campaign Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv('cleaned_marketing_data.csv')
    df['Total_Spend'] = df[['MntWines','MntFruits','MntMeatProducts','MntFishProducts','MntSweetProducts','MntGoldProds']].sum(axis=1)
    return df

df = load_data()

# --- FILTERS ---
st.sidebar.header("🔍 Filters")
country = st.sidebar.multiselect("Country", df['Country'].unique(), default=list(df['Country'].unique()))
education = st.sidebar.multiselect("Education", df['Education'].unique(), default=list(df['Education'].unique()))
age = st.sidebar.multiselect("Age Band", df['Age_Band'].unique(), default=list(df['Age_Band'].unique()))

fdf = df[(df['Country'].isin(country)) & (df['Education'].isin(education)) & (df['Age_Band'].isin(age))]

# --- KPIs ---
c1, c2, c3 = st.columns(3)
c1.metric("Total Customers", f"{len(fdf):,}")
c2.metric("Response Rate", f"{fdf['Response'].mean()*100:.2f}%")
c3.metric("Avg Spend", f"${fdf['Total_Spend'].mean():,.0f}")

# --- CHART 1: By Education ---
st.subheader("1. Response Rate by Education (%)")
fig1, ax1 = plt.subplots()
fdf.groupby('Education')['Response'].mean().mul(100).plot(kind='bar', color='skyblue', ax=ax1)
ax1.set_ylabel("Response %")
st.pyplot(fig1)

# --- CHART 2: By Country ---
st.subheader("2. Response Rate by Country (%)")
fig2, ax2 = plt.subplots()
fdf.groupby('Country')['Response'].mean().mul(100).plot(kind='bar', color='orange', ax=ax2)
ax2.set_ylabel("Response %")
st.pyplot(fig2)

# --- CHART 3: By Age Band ---
st.subheader("3. Avg Spend by Age Band")
fig3, ax3 = plt.subplots()
fdf.groupby('Age_Band')['Total_Spend'].mean().plot(kind='bar', color='green', ax=ax3)
ax3.set_ylabel("Avg Spend")
st.pyplot(fig3)

# --- TABLE ---
st.subheader("Segment-Level Summary")
summary = fdf.groupby(['Education','Marital_Status','Country']).agg(
    customers=('ID','count'),
    response_rate=('Response','mean'),
    avg_spend=('Total_Spend','mean')
).reset_index()
st.dataframe(summary, use_container_width=True)
