# Smart Electricity Consumption Analyzer using Apache Hadoop MapReduce

## 1. Project Overview

The Smart Electricity Consumption Analyzer is a data analysis project that uses Apache Hadoop MapReduce and Python to analyze household electricity consumption.

It processes electricity usage records, calculates total consumption for each household, and displays the results through an interactive Streamlit dashboard.

## 2. Objectives

- Analyze electricity consumption across multiple households.
- Calculate total electricity usage using Hadoop MapReduce.
- Identify households with higher electricity consumption.
- Visualize daily and hourly usage patterns.
- Estimate electricity bills based on the consumption rate.

## 3. Technologies Used

- **Apache Hadoop 3.4.3** – MapReduce processing
- **Python** – Mapper and Reducer implementation
- **Pandas** – Data analysis
- **Streamlit** – Interactive dashboard
- **Plotly** – Data visualization
- **CSV** – Dataset storage

## 4. Dataset Description

The project uses a synthetically generated electricity consumption dataset.

- Number of households: 10
- Number of days: 30
- Readings per household per day: 24
- Total records: 7,200

Dataset columns:

| Column | Description |
|---|---|
| date | Date of electricity reading |
| household_id | Unique household identifier |
| hour | Hour of the day |
| consumption_kwh | Electricity consumed in kWh |

## 5. MapReduce Workflow

1. **Input:** Electricity consumption CSV dataset.
2. **Mapper:** Reads each record and emits household ID with consumption.
3. **Shuffle and Sort:** Groups records by household ID.
4. **Reducer:** Calculates total consumption for each household.
5. **Output:** Household-wise electricity consumption totals.

## 6. Dashboard Features

- Total electricity consumption.
- Estimated electricity bill.
- Household-wise consumption bar chart.
- Household consumption distribution donut chart.
- Daily electricity consumption trend.
- Hourly electricity usage analysis.
- Electricity usage heatmap.
- High-consumption alerts.
- Household filtering and CSV download.

## 7. Project Results

The Hadoop MapReduce job successfully processed 7,200 records and generated consumption totals for 10 households.

- Total consumption: 5,031.28 kWh
- Average consumption per household: 503.128 kWh
- Highest consumption: H009 – 513.56 kWh
- Lowest consumption: H005 – 492.33 kWh

## 8. How to Run the Project

### Prerequisites

- Python 3
- Java 17
- Apache Hadoop 3.4.3
- Required Python libraries

### Install Python libraries

```bash
pip install streamlit pandas numpy plotly
```

### Run the Hadoop MapReduce job

From the project directory:

```bash
rm -rf output/household_results
```

```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.4.3.jar \
-input data/electricity.csv \
-output output/household_results \
-mapper "python3 mapper.py" \
-reducer "python3 reducer.py" \
-file mapper.py \
-file reducer.py
```

### View MapReduce output

```bash
cat output/household_results/part-00000
```

### Run the Streamlit dashboard

```bash
streamlit run dashboard/app.py
```

Open the dashboard in your browser:

http://localhost:8501

## 9. Future Enhancements

- Integration with real smart electricity meters.
- Real-time electricity consumption monitoring.
- Machine learning-based anomaly detection.
- Electricity cost prediction.
- Deployment as a web application.

## 10. Conclusion

This project demonstrates how Apache Hadoop MapReduce can process household electricity consumption data efficiently. The Streamlit dashboard makes the results easier to understand through interactive charts and visualizations.

---

**Project:** Smart Electricity Consumption Analyzer  
**Domain:** Big Data Analytics  
**Technologies:** Apache Hadoop, Python, Streamlit and Plotly
