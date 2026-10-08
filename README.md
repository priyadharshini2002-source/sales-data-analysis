# 📊 Sales Data Analysis & Business Insights

An interactive **Sales Data Analysis and Business Intelligence Dashboard** built using Python, Pandas, Plotly, and Streamlit to analyze sales performance, customer behavior, product performance, and regional business trends.

---

## 🚀 Live Demo

🔗 **Streamlit Dashboard:** 
🔗 [View Live Dashboard](https://sales-data-analysis-vxxfqjmtqvutcrk6mixrt8.streamlit.app/)

---

## 📌 Project Overview

This project performs comprehensive exploratory data analysis on a sales dataset to identify meaningful business patterns, customer purchasing behavior, product performance, and regional sales trends.

The project combines **Python-based EDA** with an **interactive Streamlit dashboard** to transform raw sales data into meaningful and actionable business insights.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Analyze overall sales performance
- Identify high-performing customer segments
- Determine the best-performing product categories
- Analyze sales across different states
- Understand customer purchasing patterns
- Compare sales performance across gender and age groups
- Identify top customers and products
- Generate automated business insights
- Build an interactive Business Intelligence dashboard

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data analysis and application development |
| Pandas | Data cleaning and manipulation |
| NumPy | Numerical operations |
| Plotly | Interactive data visualization |
| Matplotlib | Statistical visualization |
| Seaborn | Exploratory data visualization |
| Streamlit | Interactive dashboard |
| Git & GitHub | Version control and project hosting |

---

## 🔄 Project Workflow

Raw Sales Dataset  
↓  
Data Loading  
↓  
Data Cleaning  
↓  
Data Preprocessing  
↓  
Exploratory Data Analysis  
↓  
Statistical Analysis  
↓  
Business Insights  
↓  
Interactive Visualizations  
↓  
Streamlit Dashboard

---

## 🧹 Data Preprocessing

The dataset is processed before performing analysis.

- Loading the sales dataset
- Handling CSV encoding
- Removing unnecessary columns
- Handling missing values
- Removing duplicate records
- Converting numerical columns into appropriate data types
- Validating required columns
- Preparing the dataset for analysis

---

## 📊 Key Performance Indicators

| KPI | Value |
|---|---:|
| 💰 Total Sales | ₹106,249,132 |
| 🛒 Total Orders | 27,981 |
| 📈 Average Sale | ₹9,454 |
| 👥 Customers | 3,752 |
| 📋 Records | 11,239 |

---

## 🔎 Interactive Dashboard Features

The dashboard provides interactive filters for:

- Gender
- Age Group
- Marital Status
- State
- Occupation
- Product Category
- Top N selection

Users can dynamically filter the dataset and explore changes in sales performance and business metrics.

---

## 📈 Sales Analysis

### Sales by Gender

![Sales by Gender](sales-by-gender.png)

### Sales by Age Group

![Sales by Age Group](sales-by-age-group.png)

### Sales Amount Distribution

![Sales Amount Distribution](sales-amount-distribution.png)

### Sales Distribution by Gender

![Sales Distribution by Gender](sales-distribution-by-gender.png)

### Revenue Contribution by Product Category

![Revenue Contribution](-revenue-contribution.png)

---

## 👥 Customer Analysis

### Top Customers by Sales

![Top Customers](top-16-customers.png)

---

## 📦 Product Analysis

### Top Product Categories

![Top Product Categories](top-16-product-categories.png)

### Top Categories by Orders

![Top Categories by Orders](top-16-categories-by-orders.png)

---

## 🌎 Geographic Analysis

### Top States by Revenue

![Top States by Revenue](top-16-states-by-revenue.png)

### Top States by Orders

![Top States by Orders](top-16-states-by-orders.png)

---

## 📊 Correlation Analysis

### Correlation Matrix

![Correlation Matrix](correlation-matrix.png)

---

# 📸 Dashboard Screenshots

## 🏠 Dashboard Home

| Dashboard Home | Dashboard Overview |
|---|---|
| ![Dashboard Home](home_page1.png) | ![Dashboard Overview](home_page2.png) |

| Dashboard Analytics | Sales by Gender |
|---|---|
| ![Dashboard Analytics](home_page3.png) | ![Sales by Gender](sales-by-gender.png) |

---

## 📊 Sales Analysis

| Sales by Age Group | Sales Amount Distribution |
|---|---|
| ![Sales by Age Group](sales-by-age-group.png) | ![Sales Amount Distribution](sales-amount-distribution.png) |

| Sales Distribution by Gender | Revenue Contribution |
|---|---|
| ![Sales Distribution by Gender](sales-distribution-by-gender.png) | ![Revenue Contribution](-revenue-contribution.png) |

---

## 👥 Customer & Product Analysis

| Top Customers | Top Product Categories |
|---|---|
| ![Top Customers](top-16-customers.png) | ![Top Product Categories](top-16-product-categories.png) |

| Top Categories by Orders | Correlation Matrix |
|---|---|
| ![Top Categories by Orders](top-16-categories-by-orders.png) | ![Correlation Matrix](correlation-matrix.png) |

---

## 🌎 Geographic Analysis

| Top States by Revenue | Top States by Orders |
|---|---|
| ![Top States by Revenue](top-16-states-by-revenue.png) | ![Top States by Orders](top-16-states-by-orders.png) |

---

## 💡 Key Business Insights

Based on the analysis:

- **Female customers** generate the highest overall sales.
- The **26–35 age group** contributes the highest revenue.
- **Uttar Pradesh** is the highest-revenue state.
- **Food** is the best-performing product category.
- **IT Sector** is the highest-revenue occupation segment.
- Customer-level analysis helps identify high-value customers.
- Product category analysis highlights major revenue contributors.
- Geographic analysis reveals important regional sales patterns.

---

## 📂 Project Structure

```text
sales-data-analysis/
│
├── app.py
├── sales_predict.py
├── Sales Data.csv
├── requirements.txt
│
├── home_page1.png
├── home_page2.png
├── home_page3.png
├── sales-by-gender.png
├── sales-by-age-group.png
├── sales-amount-distribution.png
├── sales-distribution-by-gender.png
├── -revenue-contribution.png
├── top-16-customers.png
├── top-16-product-categories.png
├── top-16-categories-by-orders.png
├── top-16-states-by-revenue.png
├── top-16-states-by-orders.png
└── correlation-matrix.png
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/priyadharshini2002-source/sales-data-analysis.git
```

### 2. Navigate to the Project Directory

```bash
cd sales-data-analysis
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default web browser.

---

## 🔬 Run the EDA Script

```bash
python sales_predict.py
```

The script performs:

- Data inspection
- Data cleaning
- Statistical analysis
- Customer analysis
- Product analysis
- Geographic analysis
- Correlation analysis
- Visualization
- Automated business insights

---

## ☁️ Deployment

The Streamlit dashboard can be deployed using **Streamlit Community Cloud**.

Once deployed, the live application URL can be added to the **Live Demo** section.

---

## 🚀 Future Enhancements

- Sales forecasting using Machine Learning
- Customer segmentation using clustering
- Customer Lifetime Value analysis
- Recommendation systems
- Advanced RFM analysis
- Automated report generation
- Real-time data integration
- Advanced KPI monitoring
- Power BI integration
- Cloud database integration

---

## ⭐ Project Highlights

- 📊 Interactive Business Intelligence Dashboard
- 🐍 Python-based Data Analysis
- 📈 Interactive Plotly Visualizations
- 🎨 Streamlit Dashboard
- 👥 Customer Behavior Analysis
- 📦 Product Performance Analysis
- 🌎 Regional Sales Analysis
- 📌 Automated Business Insights
- 🔎 Exploratory Data Analysis
- 💼 Portfolio-ready Data Science Project

---

## 👩‍💻 Author

**S. Priyadharshini**

MSc Data Science  
Data Science | Business Analytics | Python | SQL | Data Visualization

---

## 📜 License

This project is created for educational, portfolio, and data analysis purposes.
