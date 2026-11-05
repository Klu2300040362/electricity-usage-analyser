import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Smart Electricity Analyzer",
    page_icon="⚡",
    layout="wide"
)

st.title("⚡ Smart Electricity Consumption Analyzer")
st.caption("Big Data Analytics using Apache Hadoop MapReduce")

# Load dataset
df = pd.read_csv("data/electricity.csv")
df["date"] = pd.to_datetime(df["date"])

# Load Hadoop results
result = pd.read_csv(
    "output/household_results/part-00000",
    sep="\t",
    names=["household_id", "total_kwh"]
)

# Sidebar
st.sidebar.header("Settings")
rate = st.sidebar.number_input(
    "Electricity rate (₹/kWh)",
    min_value=1.0,
    value=6.0
)

households = ["All"] + sorted(df["household_id"].unique())

selected = st.sidebar.selectbox(
    "Select Household",
    households
)

# Filter data
if selected != "All":
    df = df[df["household_id"] == selected]
    result = result[result["household_id"] == selected]

total = df["consumption_kwh"].sum()
bill = total * rate

# KPI cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Consumption", f"{total:,.2f} kWh")
c2.metric("Estimated Bill", f"₹{bill:,.2f}")
c3.metric("Households", df["household_id"].nunique())
c4.metric("Records", f"{len(df):,}")

st.divider()

# Household comparison
st.subheader("🏠 Household-wise Consumption")

fig1 = px.bar(
    result,
    x="household_id",
    y="total_kwh",
    color="total_kwh",
    title="Total Electricity Consumption"
)

st.plotly_chart(fig1, use_container_width=True)

# Daily consumption
st.subheader("📅 Daily Consumption Trend")

daily = df.groupby("date")["consumption_kwh"].sum().reset_index()

fig2 = px.line(
    daily,
    x="date",
    y="consumption_kwh",
    markers=True,
    title="Daily Electricity Usage"
)

st.plotly_chart(fig2, use_container_width=True)

# Hourly consumption
st.subheader("⏰ Peak Hour Analysis")

hourly = df.groupby("hour")["consumption_kwh"].mean().reset_index()

fig3 = px.bar(
    hourly,
    x="hour",
    y="consumption_kwh",
    title="Average Consumption by Hour"
)

st.plotly_chart(fig3, use_container_width=True)

# Anomaly detection
st.subheader("🚨 High Consumption Alerts")

threshold = df["consumption_kwh"].quantile(0.95)

alerts = df[df["consumption_kwh"] > threshold]

st.write(f"High consumption threshold: {threshold:.2f} kWh")
st.write(f"Unusual readings detected: {len(alerts)}")

st.dataframe(alerts, use_container_width=True)

st.success("Electricity consumption analysis completed!")
st.divider()
st.header("📊 Smart Energy Insights")

peak_hour = hourly.loc[hourly["consumption_kwh"].idxmax()]
peak_day = daily.loc[daily["consumption_kwh"].idxmax()]

col1, col2 = st.columns(2)

col1.metric("Peak Usage Hour", f"{int(peak_hour['hour'])}:00")
col2.metric(
    "Highest Usage Day",
    peak_day["date"].strftime("%d %b %Y")
)

st.subheader("📥 Download Reports")

st.download_button(
    "Download Household Summary",
    result.to_csv(index=False),
    file_name="household_summary.csv"
)

st.download_button(
    "Download High Usage Alerts",
    alerts.to_csv(index=False),
    file_name="high_consumption_alerts.csv"
)

st.download_button(
    "Download Complete Dataset",
    df.to_csv(index=False),
    file_name="electricity_dataset.csv"
)
# Household-wise electricity consumption pie chart

st.subheader("Household-wise Consumption Distribution")

fig_pie = px.pie(
    result,
    names="household_id",
    values="total_kwh",
    title="Share of Electricity Consumption by Household",
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Bold
)

fig_pie.update_traces(
    textposition="inside",
    textinfo="label+percent",
    pull=[0.03] * len(result)
)

fig_pie.update_layout(
    template="plotly_dark",
    showlegend=True
)

st.plotly_chart(fig_pie, use_container_width=True)
# Electricity Usage Heatmap

st.subheader("Electricity Usage Heatmap")

st.caption(
    "Explore average electricity consumption "
    "for each hour across the 30-day period."
)

heatmap_data = df.copy()

heatmap_data["date_label"] = (
    heatmap_data["date"].dt.strftime("%d %b")
)

heatmap_table = heatmap_data.pivot_table(
    index="date_label",
    columns="hour",
    values="consumption_kwh",
    aggfunc="mean"
)

fig_heatmap = px.imshow(
    heatmap_table,
    labels={
        "x": "Hour of Day",
        "y": "Date",
        "color": "Average Consumption (kWh)"
    },
    title="Daily and Hourly Electricity Consumption",
    color_continuous_scale="YlOrRd",
    aspect="auto"
)

fig_heatmap.update_layout(
    template="plotly_dark",
    xaxis_title="Hour of Day",
    yaxis_title="Date"
)

st.plotly_chart(fig_heatmap, use_container_width=True)
