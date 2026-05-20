import streamlit as st
import pandas as pd
import plotly.express as px
from sqlalchemy import create_engine

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="News Sentiment Dashboard",
    layout="wide"
)

# =========================
# DATABASE CONNECTION
# =========================

DATABASE_URL = (
    "postgresql+pg8000://postgres:newsdata123@"
    "news-db.ci5e44ikyqgx.us-east-1.rds.amazonaws.com:5432/newsdb"
)

engine = create_engine(DATABASE_URL)

# =========================
# REFRESH BUTTON
# =========================

if st.button("🔄 Refresh Data"):
    st.cache_data.clear()
    st.rerun()

# =========================
# LOAD DATA
# =========================

query = """
SELECT *
FROM news_sentiment
ORDER BY published_at DESC
LIMIT 50
"""

@st.cache_data(ttl=60)
def load_data():
    return pd.read_sql(query, engine)

df = load_data()

# =========================
# TITLE
# =========================

st.title("📰 News Sentiment Dashboard")

st.markdown("---")

# =========================
# METRICS
# =========================

positive = len(df[df["sentiment"] == "Positive"])
negative = len(df[df["sentiment"] == "Negative"])
neutral = len(df[df["sentiment"] == "Neutral"])

col1, col2, col3 = st.columns(3)

col1.metric("🟢 Positive News", positive)
col2.metric("🔴 Negative News", negative)
col3.metric("⚪ Neutral News", neutral)

st.markdown("---")

# =========================
# ANALYSIS CHARTS
# =========================

st.subheader("📊 Sentiment Analysis")

chart_col1, chart_col2 = st.columns(2)

# Sentiment Counts

sentiment_counts = df["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["Sentiment", "Count"]

# BAR CHART

bar_fig = px.bar(
    sentiment_counts,
    x="Sentiment",
    y="Count",
    color="Sentiment",
    title="News Sentiment Distribution"
)

chart_col1.plotly_chart(
    bar_fig,
    use_container_width=True
)

# PIE CHART

pie_fig = px.pie(
    sentiment_counts,
    names="Sentiment",
    values="Count",
    title="Sentiment Share"
)

chart_col2.plotly_chart(
    pie_fig,
    use_container_width=True
)

st.markdown("---")

# =========================
# FILTER
# =========================

sentiment_filter = st.selectbox(
    "Filter by Sentiment",
    ["All", "Positive", "Negative", "Neutral"]
)

if sentiment_filter != "All":
    df = df[df["sentiment"] == sentiment_filter]

# =========================
# COLOR FUNCTION
# =========================

def color_sentiment(val):

    if val == "Positive":
        return "background-color: green; color: white"

    elif val == "Negative":
        return "background-color: red; color: white"

    elif val == "Neutral":
        return "background-color: gray; color: white"

    return ""

# =========================
# STYLED TABLE
# =========================

st.subheader("🎨 Sentiment Highlighted Table")

styled_df = df.style.map(
    color_sentiment,
    subset=["sentiment"]
)

st.dataframe(
    styled_df,
    use_container_width=True
)

st.markdown("---")

# =========================
# RAW DATA (COLLAPSIBLE)
# =========================

with st.expander("📂 View Raw News Data"):

    st.dataframe(
        df,
        use_container_width=True
    )