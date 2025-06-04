#  Streamlit-Based Employee Productivity Analytics 

A Streamlit-based interactive dashboard to analyze employee productivity, efficiency, and overall company performance using smart KPIs and visualizations.

[![11.png](https://i.postimg.cc/d1ggZKTL/11.png)](https://postimg.cc/ftj81pCN)




### Features ✅
- Upload your own dataset (CSV format)
- Auto-calculates productivity KPIs like:
  - Total Clocked & Productive Hours
  - Top 3 Best Performing Employees
  - Department-wise & Project-wise Efficiency
  - Resignation trends & Employee Satisfaction
- Visuals: Bar Charts, Pie Charts, Line Graphs, and More
- Year and Department filters
- Designed for CEOs, HR heads, and decision-makers'


[![22.png](https://i.postimg.cc/9QcK7bzt/22.png)](https://postimg.cc/8jnZ8hRj)
[![33.png](https://i.postimg.cc/XNyRSXTF/33.png)](https://postimg.cc/5jb7899N)
[![44.png](https://i.postimg.cc/vHrCTk8Z/44.png)](https://postimg.cc/ykNLrfSM)

### Built With 🛠️
- Python (Pandas, Plotly, Streamlit)
- Git & GitHub for Version Control
- Streamlit Cloud for Hosting


###  🔗Try it Live
## https://dawnfoxdoesstuff.streamlit.app

### Usage Instructions
Upload Your Dataset

After launching the app, upload a .csv file via the uploader on the homepage.

Once uploaded, all KPIs and visualizations will update dynamically.

### 📁Dataset Requirements
Your CSV must contain the following columns exactly as shown (case-sensitive):
| Column Name                   | Description                                            |
| ----------------------------- | ------------------------------------------------------ |
| `Date`                        | Date of the entry (format: YYYY-MM-DD)                 |
| `Employee_ID`                 | Unique identifier for each employee                    |
| `Employee_Name`               | Full name of the employee                              |
| `Department`                  | Department name (e.g., HR, IT, Sales)                  |
| `Job_Title`                   | Job designation (e.g., Analyst, Manager)               |
| `Gender`                      | Gender of the employee (e.g., Male, Female)            |
| `Project`                     | Assigned project name or code                          |
| `Years_At_Company`            | Number of years the employee has been at the company   |
| `Performance_Score`           | Performance rating (numeric or categorical)            |
| `Monthly_Salary`              | Salary in numbers                                      |
| `Clocked_Hours`               | Total hours clocked (per month or per entry)           |
| `Productive_Hours`            | Productive hours worked                                |
| `Tasks_Completed`             | Number of tasks completed                              |
| `Meetings`                    | Number of meetings attended                            |
| `Break_Hours`                 | Time spent on breaks (in hours)                        |
| `Training_Hours`              | Time spent in training                                 |
| `Overtime_Hours`              | Overtime hours worked                                  |
| `Remote_Work_Frequency`       | Frequency of remote work (e.g., Rarely, Often, Always) |
| `Employee_Satisfaction_Score` | Satisfaction rating (e.g., 1 to 5 or 0–100 scale)      |


### After Upload

The dashboard will auto-generate productivity metrics, visualizations, and employee performance insights.

Filters are available for department, job title, date range, and more.

### Installation & Setup 💻



Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dawnfox404/Employee_productivity.git
cd Employee_productivity
```
### 3️⃣ Install Required Dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Run the App Locally
```bash
streamlit run app.py
```

