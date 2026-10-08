# ============================================================
# SALES DATA ANALYSIS - SIMPLE & STABLE EDA
# Clean plots with non-overlapping labels
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ------------------------------------------------------------
# 0. PLOT STYLE
# ------------------------------------------------------------

sns.set_theme(style="whitegrid")

plt.rcParams["figure.dpi"] = 100
plt.rcParams["axes.titlesize"] = 14
plt.rcParams["axes.labelsize"] = 11
plt.rcParams["xtick.labelsize"] = 10
plt.rcParams["ytick.labelsize"] = 10


# ------------------------------------------------------------
# 1. LOAD DATA
# ------------------------------------------------------------

try:

    df = pd.read_csv(
        "Sales Data.csv",
        encoding="unicode_escape"
    )

except FileNotFoundError:

    print("\n❌ ERROR: Sales Data.csv not found.")
    print("Please keep Sales Data.csv in the same folder as this Python file.")
    raise SystemExit


print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 2. DATA CLEANING
# ------------------------------------------------------------

# Remove unwanted columns only if they exist
for col in ["Status", "unnamed1", "Unnamed: 0"]:

    if col in df.columns:
        df.drop(col, axis=1, inplace=True)


# Convert Amount to numeric BEFORE removing missing values
if "Amount" in df.columns:

    df["Amount"] = (
        df["Amount"]
        .astype(str)
        .str.replace(",", "", regex=False)
    )

    df["Amount"] = pd.to_numeric(
        df["Amount"],
        errors="coerce"
    )

else:

    print("\n❌ ERROR: 'Amount' column not found.")
    raise SystemExit


# Convert Orders to numeric if available
if "Orders" in df.columns:

    df["Orders"] = pd.to_numeric(
        df["Orders"],
        errors="coerce"
    )


# Remove missing values
df.dropna(inplace=True)


# Remove rows where Amount could not be converted
df.dropna(
    subset=["Amount"],
    inplace=True
)


# Convert Amount to integer
df["Amount"] = df["Amount"].astype(int)


# ------------------------------------------------------------
# 3. BASIC INFORMATION
# ------------------------------------------------------------

print("\n========================================")
print("DATASET INFORMATION")
print("========================================")

print("Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nData Types:")
print(df.dtypes)


# ------------------------------------------------------------
# 4. DESCRIPTIVE STATISTICS
# ------------------------------------------------------------

print("\n========================================")
print("DESCRIPTIVE STATISTICS")
print("========================================")

print(df.describe())


# ------------------------------------------------------------
# 5. BUSINESS KPIs
# ------------------------------------------------------------

total_sales = df["Amount"].sum()


# Calculate total orders
if "Orders" in df.columns:

    total_orders = df["Orders"].sum()

else:

    total_orders = len(df)


average_sales = df["Amount"].mean()


if "User_ID" in df.columns:

    total_customers = df["User_ID"].nunique()

else:

    total_customers = len(df)


print("\n========================================")
print("BUSINESS KPIs")
print("========================================")

print(
    "Total Sales       :",
    f"₹{total_sales:,.0f}"
)

print(
    "Total Orders      :",
    f"{total_orders:,}"
)

print(
    "Average Sale      :",
    f"₹{average_sales:,.2f}"
)

print(
    "Total Customers   :",
    f"{total_customers:,}"
)


# ------------------------------------------------------------
# 6. GENDER ANALYSIS
# ------------------------------------------------------------

if "Gender" in df.columns:

    gender_sales = (
        df.groupby("Gender")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========================================")
    print("SALES BY GENDER")
    print("========================================")

    print(gender_sales)

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=gender_sales.index,
        y=gender_sales.values,
        hue=gender_sales.index,
        palette="Set2",
        legend=False
    )

    plt.title("Total Sales by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Sales Amount")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 7. AGE GROUP ANALYSIS
# ------------------------------------------------------------

if "Age Group" in df.columns:

    age_sales = (
        df.groupby("Age Group")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========================================")
    print("SALES BY AGE GROUP")
    print("========================================")

    print(age_sales)

    plt.figure(figsize=(10, 5))

    sns.barplot(
        x=age_sales.index,
        y=age_sales.values,
        hue=age_sales.index,
        palette="viridis",
        legend=False
    )

    plt.title("Sales by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Sales Amount")

    plt.xticks(
        rotation=20,
        ha="right"
    )

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 8. STATE ANALYSIS - TOP 10 ORDERS
# ------------------------------------------------------------

if (
    "State" in df.columns
    and
    "Orders" in df.columns
):

    state_orders = (
        df.groupby("State")["Orders"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========================================")
    print("TOP 10 STATES BY ORDERS")
    print("========================================")

    print(state_orders)

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=state_orders.values,
        y=state_orders.index,
        hue=state_orders.index,
        palette="Blues_r",
        legend=False
    )

    plt.title("Top 10 States by Orders")
    plt.xlabel("Orders")
    plt.ylabel("State")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 9. STATE SALES - TOP 10
# ------------------------------------------------------------

if "State" in df.columns:

    state_sales = (
        df.groupby("State")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========================================")
    print("TOP 10 STATES BY SALES")
    print("========================================")

    print(state_sales)

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=state_sales.values,
        y=state_sales.index,
        hue=state_sales.index,
        palette="Greens_r",
        legend=False
    )

    plt.title("Top 10 States by Sales")
    plt.xlabel("Sales Amount")
    plt.ylabel("State")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 10. MARITAL STATUS
# ------------------------------------------------------------

if "Marital_Status" in df.columns:

    marital_sales = (
        df.groupby("Marital_Status")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========================================")
    print("SALES BY MARITAL STATUS")
    print("========================================")

    print(marital_sales)

    plt.figure(figsize=(8, 5))

    sns.barplot(
        x=marital_sales.index,
        y=marital_sales.values,
        hue=marital_sales.index,
        palette="Set3",
        legend=False
    )

    plt.title("Sales by Marital Status")
    plt.xlabel("Marital Status")
    plt.ylabel("Sales Amount")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 11. MARITAL STATUS + GENDER
# ------------------------------------------------------------

if (
    "Marital_Status" in df.columns
    and
    "Gender" in df.columns
):

    marital_gender = (
        df.groupby(
            ["Marital_Status", "Gender"]
        )["Amount"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(9, 5))

    sns.barplot(
        data=marital_gender,
        x="Marital_Status",
        y="Amount",
        hue="Gender",
        palette="Set2"
    )

    plt.title("Sales by Marital Status and Gender")
    plt.xlabel("Marital Status")
    plt.ylabel("Sales Amount")

    plt.legend(
        title="Gender",
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 12. OCCUPATION ANALYSIS
# ------------------------------------------------------------

if "Occupation" in df.columns:

    occupation_sales = (
        df.groupby("Occupation")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========================================")
    print("SALES BY OCCUPATION")
    print("========================================")

    print(occupation_sales)

    plt.figure(
        figsize=(
            12,
            max(
                6,
                len(occupation_sales) * 0.4
            )
        )
    )

    sns.barplot(
        x=occupation_sales.values,
        y=occupation_sales.index,
        hue=occupation_sales.index,
        palette="magma",
        legend=False
    )

    plt.title("Sales by Occupation")
    plt.xlabel("Sales Amount")
    plt.ylabel("Occupation")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 13. PRODUCT CATEGORY - SALES
# ------------------------------------------------------------

if "Product_Category" in df.columns:

    category_sales = (
        df.groupby("Product_Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========================================")
    print("SALES BY PRODUCT CATEGORY")
    print("========================================")

    print(category_sales)

    plt.figure(
        figsize=(
            12,
            max(
                6,
                len(category_sales) * 0.45
            )
        )
    )

    sns.barplot(
        x=category_sales.values,
        y=category_sales.index,
        hue=category_sales.index,
        palette="viridis",
        legend=False
    )

    plt.title("Sales by Product Category")
    plt.xlabel("Sales Amount")
    plt.ylabel("Product Category")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 14. PRODUCT CATEGORY - ORDERS
# ------------------------------------------------------------

if (
    "Product_Category" in df.columns
    and
    "Orders" in df.columns
):

    category_orders = (
        df.groupby("Product_Category")["Orders"]
        .sum()
        .sort_values(ascending=False)
    )

    print("\n========================================")
    print("ORDERS BY PRODUCT CATEGORY")
    print("========================================")

    print(category_orders)

    plt.figure(
        figsize=(
            12,
            max(
                6,
                len(category_orders) * 0.45
            )
        )
    )

    sns.barplot(
        x=category_orders.values,
        y=category_orders.index,
        hue=category_orders.index,
        palette="coolwarm",
        legend=False
    )

    plt.title("Orders by Product Category")
    plt.xlabel("Orders")
    plt.ylabel("Product Category")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 15. TOP 10 PRODUCTS BY ORDERS
# ------------------------------------------------------------

if (
    "Product_ID" in df.columns
    and
    "Orders" in df.columns
):

    top_products_orders = (
        df.groupby("Product_ID")["Orders"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========================================")
    print("TOP 10 PRODUCTS BY ORDERS")
    print("========================================")

    print(top_products_orders)

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_products_orders.values,
        y=top_products_orders.index.astype(str),
        hue=top_products_orders.index.astype(str),
        palette="Blues_r",
        legend=False
    )

    plt.title("Top 10 Products by Orders")
    plt.xlabel("Orders")
    plt.ylabel("Product ID")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 16. TOP 10 PRODUCTS BY SALES
# ------------------------------------------------------------

if "Product_ID" in df.columns:

    top_products_sales = (
        df.groupby("Product_ID")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========================================")
    print("TOP 10 PRODUCTS BY SALES")
    print("========================================")

    print(top_products_sales)

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_products_sales.values,
        y=top_products_sales.index.astype(str),
        hue=top_products_sales.index.astype(str),
        palette="Greens_r",
        legend=False
    )

    plt.title("Top 10 Products by Sales")
    plt.xlabel("Sales Amount")
    plt.ylabel("Product ID")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 17. SALES DISTRIBUTION
# ------------------------------------------------------------

plt.figure(figsize=(10, 5))

sns.histplot(
    df["Amount"],
    bins=30,
    kde=True,
    color="steelblue"
)

plt.title("Distribution of Sales Amount")
plt.xlabel("Sales Amount")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# ------------------------------------------------------------
# 18. SALES BY AGE GROUP AND GENDER
# ------------------------------------------------------------

if (
    "Age Group" in df.columns
    and
    "Gender" in df.columns
):

    age_gender = (
        df.groupby(
            ["Age Group", "Gender"]
        )["Amount"]
        .sum()
        .reset_index()
    )

    plt.figure(figsize=(11, 6))

    sns.barplot(
        data=age_gender,
        x="Age Group",
        y="Amount",
        hue="Gender",
        palette="Set2"
    )

    plt.title("Sales by Age Group and Gender")
    plt.xlabel("Age Group")
    plt.ylabel("Sales Amount")

    plt.xticks(
        rotation=20,
        ha="right"
    )

    plt.legend(
        title="Gender",
        bbox_to_anchor=(1.02, 1),
        loc="upper left"
    )

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 19. CORRELATION
# ------------------------------------------------------------

numeric_data = df.select_dtypes(
    include=np.number
)

if numeric_data.shape[1] >= 2:

    correlation = numeric_data.corr()

    print("\n========================================")
    print("CORRELATION MATRIX")
    print("========================================")

    print(correlation)

    plt.figure(figsize=(9, 7))

    sns.heatmap(
        correlation,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=0.5,
        square=True
    )

    plt.title("Correlation Heatmap")

    plt.tight_layout()
    plt.show()

else:

    print(
        "\n⚠️ Not enough numeric columns "
        "to calculate correlation."
    )


# ------------------------------------------------------------
# 20. SALES BY GENDER - BOX PLOT
# ------------------------------------------------------------

if "Gender" in df.columns:

    plt.figure(figsize=(8, 5))

    sns.boxplot(
        data=df,
        x="Gender",
        y="Amount",
        hue="Gender",
        palette="Set2",
        legend=False
    )

    plt.title("Sales Distribution by Gender")
    plt.xlabel("Gender")
    plt.ylabel("Sales Amount")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 21. CATEGORY REVENUE CONTRIBUTION
# ------------------------------------------------------------

if "Product_Category" in df.columns:

    category_percentage = (
        df.groupby("Product_Category")["Amount"]
        .sum()
        .sort_values(ascending=False)
    )

    # Calculate percentage
    category_percent = (
        category_percentage
        / category_percentage.sum()
        * 100
    )

    # Create clean labels for legend
    legend_labels = [
        f"{category} - {percentage:.1f}%"
        for category, percentage
        in category_percent.items()
    ]

    # Create figure
    fig, ax = plt.subplots(
        figsize=(12, 10)
    )

    # Pie chart
    wedges, _ = ax.pie(
        category_percentage.values,
        labels=None,
        startangle=90,
        counterclock=False,
        wedgeprops={
            "edgecolor": "white",
            "linewidth": 1.2
        }
    )

    # Title
    ax.set_title(
        "Revenue Contribution by Product Category",
        fontsize=16,
        fontweight="bold",
        pad=20
    )

    # Legend at bottom
    ax.legend(
        wedges,
        legend_labels,
        title="Product Categories",
        loc="upper center",
        bbox_to_anchor=(0.5, -0.05),
        ncol=3,
        fontsize=10,
        title_fontsize=11,
        frameon=True
    )

    # Keep pie circular
    ax.axis("equal")

    # Give enough space for legend
    plt.subplots_adjust(
        bottom=0.30,
        top=0.90
    )

    plt.show()


# ------------------------------------------------------------
# 22. TOP CUSTOMERS
# ------------------------------------------------------------

if "User_ID" in df.columns:

    top_customers = (
        df.groupby("User_ID")["Amount"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )

    print("\n========================================")
    print("TOP 10 CUSTOMERS BY SALES")
    print("========================================")

    print(top_customers)

    plt.figure(figsize=(10, 6))

    sns.barplot(
        x=top_customers.values,
        y=top_customers.index.astype(str),
        hue=top_customers.index.astype(str),
        palette="rocket",
        legend=False
    )

    plt.title("Top 10 Customers by Sales")
    plt.xlabel("Sales Amount")
    plt.ylabel("Customer ID")

    plt.tight_layout()
    plt.show()


# ------------------------------------------------------------
# 23. AUTOMATIC BUSINESS INSIGHTS
# ------------------------------------------------------------

print("\n")
print("============================================================")
print("                  KEY BUSINESS INSIGHTS")
print("============================================================")


if "Gender" in df.columns:

    best_gender = (
        df.groupby("Gender")["Amount"]
        .sum()
        .idxmax()
    )

    print(
        f"\nHighest Revenue Gender    : {best_gender}"
    )


if "Age Group" in df.columns:

    best_age = (
        df.groupby("Age Group")["Amount"]
        .sum()
        .idxmax()
    )

    print(
        f"Highest Revenue Age Group : {best_age}"
    )


if "State" in df.columns:

    best_state = (
        df.groupby("State")["Amount"]
        .sum()
        .idxmax()
    )

    print(
        f"Highest Revenue State     : {best_state}"
    )


if "Product_Category" in df.columns:

    best_category = (
        df.groupby("Product_Category")["Amount"]
        .sum()
        .idxmax()
    )

    print(
        f"Best Product Category     : {best_category}"
    )


if "Occupation" in df.columns:

    best_occupation = (
        df.groupby("Occupation")["Amount"]
        .sum()
        .idxmax()
    )

    print(
        f"Top Revenue Occupation    : {best_occupation}"
    )


if "Product_ID" in df.columns:

    best_product = (
        df.groupby("Product_ID")["Amount"]
        .sum()
        .idxmax()
    )

    print(
        f"Top Revenue Product       : {best_product}"
    )


print(
    f"\nTotal Revenue             : ₹{total_sales:,.0f}"
)

print(
    f"Total Orders              : {total_orders:,}"
)

print(
    f"Average Transaction       : ₹{average_sales:,.2f}"
)

print(
    f"Total Customers           : {total_customers:,}"
)


print("\n============================================================")
print("                    EDA COMPLETED")
print("============================================================")