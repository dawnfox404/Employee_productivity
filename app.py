import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from datetime import datetime

st.set_page_config(page_title="Employee Productivity Dashboard", layout="wide")
st.title(" Employee Productivity Dashboard")

# File uploader
uploaded_file = st.file_uploader("📁 Upload your employee productivity CSV file", type=["csv"])
with st.expander("📄 Dataset Format Reference"):
    st.markdown("""
    Please make sure CSV file has the following :

    | Column Name             | Description                                               |
    |------------------------|-----------------------------------------------------------|
    | `Date`                 | Date of the log (format: YYYY-MM-DD)                      |
    | `Employee_ID`          | Unique identifier for each employee                       |
    | `Employee_Name`        | Full name of the employee                                 |
    | `Department`           | Department the employee belongs to (e.g., IT, HR, Sales)  |
    | `Job_Title`            | Role or position held by the employee                     |
    | `Gender`               | Gender (Male, Female, Other)                              |
    | `Project`              | Name or ID of the project assigned                        |
    | `Years_At_Company`     | Tenure in years                                            |
    | `Performance_Score`    | Rating from 1 to 5                                         |
    | `Monthly_Salary`       | Salary in USD                                              |
    | `Clocked_Hours`        | Total hours logged                                         |
    | `Productive_Hours`     | Subset of `Clocked_Hours` spent on work                   |
    | `Tasks_Completed`      | Total tasks finished                                       |
    | `Meetings`             | Number of meetings attended                                |
    | `Break_Hours`          | Time spent on breaks (in hours)                            |
    | `Training_Hours`       | Training hours logged                                      |
    | `Overtime_Hours`       | Overtime hours in the year                                 |
    | `Remote_Work_Frequency`| Percentage of remote work (e.g., 0%, 50%, 100%)            |
    | `Employee_Satisfaction_Score` | Rating from 1.0 to 5.0                              |
    

    
    """)


@st.cache_data
def load_data(file):
    df = pd.read_csv(file, parse_dates=["Date"])
    df["Productivity"] = df["Productive_Hours"] / df["Clocked_Hours"] * 100
    df["Year"] = df["Date"].dt.year
    return df

if uploaded_file:
    df = load_data(uploaded_file)

    # Sidebar filters
    with st.sidebar:
        st.header("🔎 Filters")
        departments = st.multiselect("Department", options=sorted(df["Department"].unique()), default=sorted(df["Department"].unique()))
        years = st.multiselect("Year", options=sorted(df["Year"].unique()), default=sorted(df["Year"].unique()))
        remote_filter = st.slider("Remote Work %", 0, 100, (0, 100), step=25)

    # Apply filters
    filtered_df = df[
        df["Department"].isin(departments) &
        df["Year"].isin(years) &
        (df["Remote_Work_Frequency"].between(remote_filter[0], remote_filter[1]))
    ]

    # KPIs
    total_employees = filtered_df["Employee_ID"].nunique()
    avg_productivity = filtered_df["Productivity"].mean()
    avg_satisfaction = filtered_df["Employee_Satisfaction_Score"].mean()
    total_tasks = filtered_df["Tasks_Completed"].sum()

    st.markdown("### 📊 Key Performance Indicators")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("👥 Total Employees", total_employees)
    col2.metric("⚙️ Avg Productivity (%)", f"{avg_productivity:.2f}")
    col3.metric("😊 Avg Satisfaction", f"{avg_satisfaction:.2f}")
    col4.metric("✅ Total Tasks Completed", int(total_tasks))

    # Top 3 Employees
    top_employees = (
        filtered_df.groupby(["Employee_ID", "Employee_Name"])
        .agg({"Productivity": "mean"})
        .reset_index()
        .sort_values("Productivity", ascending=False)
        .head(3)
    )
    st.markdown("### 🏆 Top 3 Employees by Productivity")
    st.table(top_employees.round(2))

    # Productivity over time
    st.markdown("### 📈 Productivity Over Time")
    prod_time = (
        filtered_df.groupby("Date")["Productivity"]
        .mean()
        .reset_index()
        .sort_values("Date")
    )
    chart_prod = alt.Chart(prod_time).mark_line(point=True).encode(
        x="Date:T",
        y=alt.Y("Productivity:Q", title="Avg Productivity (%)"),
        tooltip=["Date", alt.Tooltip("Productivity", format=".2f")]
    ).properties(width=1000, height=400)
    st.altair_chart(chart_prod)

    # Department-wise Headcount
    st.markdown("### 🧮 Department-wise Headcount")
    dept_count = filtered_df.groupby("Department")["Employee_ID"].nunique().reset_index().rename(columns={"Employee_ID": "Count"})
    bar_headcount = alt.Chart(dept_count).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
        x=alt.X("Count:Q", title="Number of Employees"),
        y=alt.Y("Department:N", sort='-x'),
        color=alt.Color("Department:N", legend=None),
        tooltip=["Department", "Count"]
    ).properties(width=600, height=350)
    st.altair_chart(bar_headcount)

    # Average Productivity % by Department
    st.markdown("### 📊 Avg Productivity (%) by Department")
    dept_prod = filtered_df.groupby("Department").agg({"Productive_Hours":"sum", "Clocked_Hours":"sum"}).reset_index()
    dept_prod["Productivity_Percent"] = (dept_prod["Productive_Hours"] / dept_prod["Clocked_Hours"]) * 100
    bar_productivity = alt.Chart(dept_prod).mark_bar(cornerRadiusTopLeft=3, cornerRadiusTopRight=3).encode(
        x=alt.X("Productivity_Percent:Q", title="Avg Productivity (%)"),
        y=alt.Y("Department:N", sort='-x'),
        color=alt.Color("Productivity_Percent:Q", scale=alt.Scale(scheme="greens")),
        tooltip=["Department", alt.Tooltip("Productivity_Percent", format=".2f")]
    ).properties(width=600, height=350)
    st.altair_chart(bar_productivity)



else:
    st.info("👆 Upload a CSV file to begin.")
