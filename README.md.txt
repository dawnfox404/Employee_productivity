Employee Productivity Dashboard 📊

A Streamlit web application to analyze employee performance, productivity, and work efficiency using interactive KPIs and charts.

🔍 Features
- Upload custom dataset (CSV)
- Automatically calculated KPIs
- Best performing employees
- Department & job-based analysis
- Productivity over time
- Overtime vs performance
- Remote work distribution
📁 Sample Dataset Format

Required columns in the CSV:

- Date
- Employee_Name
- Employee_ID
- Department
- Job_Title
- Gender
- Project
- Years_At_Company
- Performance_Score
- Monthly_Salary
- Clocked_Hours
- Productive_Hours
- Tasks_Completed
- Meetings
- Break_Hours
- Training_Hours
- Overtime_Hours
- Remote_Work_Frequency
- Employee_Satisfaction_Score
- Resigned

🚀 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
