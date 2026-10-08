import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# PAGE
# ============================================================

st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# PROFESSIONAL STREAMLIT STYLE
# ============================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #f5f7ff, #eef4ff);
}

.block-container {
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main title */
.main-title {
    text-align: center;
    font-size: 46px;
    font-weight: 800;
    color: #172554;
    margin-bottom: 5px;
}

.main-subtitle {
    text-align: center;
    color: #64748b;
    font-size: 17px;
    margin-bottom: 30px;
}

/* KPI */
[data-testid="stMetric"] {
    background: white;
    padding: 22px;
    border-radius: 20px;
    box-shadow: 0 8px 25px rgba(30, 64, 175, 0.10);
    border: 1px solid #e5e7eb;
    transition: all 0.3s ease;
}

[data-testid="stMetric"]:hover {
    transform: translateY(-7px);
    box-shadow: 0 18px 40px rgba(37, 99, 235, 0.18);
}

[data-testid="stMetricLabel"] {
    font-weight: 600;
    color: #64748b;
}

[data-testid="stMetricValue"] {
    font-size: 30px;
    font-weight: 800;
    color: #172554;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    border-radius: 12px;
    border: 1px solid #dbe3ef;
    background: white;
}

div[data-baseweb="select"] > div:hover {
    border-color: #6366f1;
}

/* Tabs */
button[data-baseweb="tab"] {
    font-weight: 700;
    font-size: 15px;
}

button[data-baseweb="tab"]:hover {
    color: #4f46e5;
}

/* Section headings */
.section-header {
    font-size: 28px;
    font-weight: 800;
    color: #172554;
    margin-top: 20px;
    margin-bottom: 5px;
}

.section-text {
    color: #64748b;
    margin-bottom: 20px;
}

/* Insight */
.insight {
    background: white;
    padding: 16px 20px;
    margin: 8px 0;
    border-radius: 15px;
    border-left: 5px solid #6366f1;
    box-shadow: 0 5px 18px rgba(15,23,42,0.07);
    transition: 0.3s;
}

.insight:hover {
    transform: translateX(6px);
}

/* Footer */
.footer {
    text-align: center;
    padding: 25px;
    margin-top: 40px;
    color: #64748b;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv(
        "Sales Data.csv",
        encoding="unicode_escape"
    )

    # Remove unnecessary columns
    for col in ["Status", "unnamed1", "Unnamed: 0"]:
        if col in data.columns:
            data.drop(columns=col, inplace=True)

    # Amount
    if "Amount" in data.columns:
        data["Amount"] = (
            data["Amount"]
            .astype(str)
            .str.replace(",", "", regex=False)
        )

        data["Amount"] = pd.to_numeric(
            data["Amount"],
            errors="coerce"
        )

    # Orders
    if "Orders" in data.columns:
        data["Orders"] = pd.to_numeric(
            data["Orders"],
            errors="coerce"
        )

    data.dropna(subset=["Amount"], inplace=True)

    return data


# ============================================================
# LOAD
# ============================================================

try:

    df = load_data()

except FileNotFoundError:

    st.error("❌ Sales Data.csv not found.")

    st.info(
        "Make sure Sales Data.csv and app.py are inside the same folder."
    )

    st.stop()

except Exception as error:

    st.error(f"❌ Dataset error: {error}")

    st.stop()


# ============================================================
# HERO
# ============================================================

st.markdown(
    '<div class="main-title">📊 Sales Analytics Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Interactive Business Intelligence • Sales • Customers • Products • Geography'
    '</div>',
    unsafe_allow_html=True
)

st.write(
    "💡 Explore trends, compare categories, discover customer patterns "
    "and understand business performance."
)

st.divider()


# ============================================================
# FILTER SECTION
# ============================================================

st.subheader("🎛️ Smart Data Filters")

st.caption(
    "Use the filters below to dynamically explore your sales dataset."
)


def options_for(column):

    if column not in df.columns:
        return ["All"]

    values = (
        df[column]
        .dropna()
        .astype(str)
        .sort_values()
        .unique()
        .tolist()
    )

    return ["All"] + values


# ============================================================
# FILTERS
# ============================================================

f1, f2, f3 = st.columns(3)

with f1:

    gender = st.selectbox(
        "👤 Gender",
        options_for("Gender")
    )

with f2:

    age = st.selectbox(
        "🎂 Age Group",
        options_for("Age Group")
    )

with f3:

    marital = st.selectbox(
        "💍 Marital Status",
        options_for("Marital_Status")
    )


f4, f5, f6 = st.columns(3)

with f4:

    state = st.selectbox(
        "📍 State",
        options_for("State")
    )

with f5:

    occupation = st.selectbox(
        "💼 Occupation",
        options_for("Occupation")
    )

with f6:

    category = st.selectbox(
        "🛍️ Product Category",
        options_for("Product_Category")
    )


st.write("🏆 **Number of Top Items**")

top_n = st.slider(
    "Top N",
    min_value=5,
    max_value=20,
    value=10,
    step=1,
    label_visibility="collapsed"
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered = df.copy()


if gender != "All" and "Gender" in filtered.columns:

    filtered = filtered[
        filtered["Gender"].astype(str) == gender
    ]


if age != "All" and "Age Group" in filtered.columns:

    filtered = filtered[
        filtered["Age Group"].astype(str) == age
    ]


if marital != "All" and "Marital_Status" in filtered.columns:

    filtered = filtered[
        filtered["Marital_Status"].astype(str) == marital
    ]


if state != "All" and "State" in filtered.columns:

    filtered = filtered[
        filtered["State"].astype(str) == state
    ]


if occupation != "All" and "Occupation" in filtered.columns:

    filtered = filtered[
        filtered["Occupation"].astype(str) == occupation
    ]


if category != "All" and "Product_Category" in filtered.columns:

    filtered = filtered[
        filtered["Product_Category"].astype(str) == category
    ]


# ============================================================
# EMPTY
# ============================================================

if filtered.empty:

    st.warning(
        "⚠️ No records found for the selected filters."
    )

    st.stop()


# ============================================================
# KPI
# ============================================================

total_sales = filtered["Amount"].sum()

if "Orders" in filtered.columns:

    total_orders = filtered["Orders"].sum()

else:

    total_orders = len(filtered)


average_sale = filtered["Amount"].mean()


if "User_ID" in filtered.columns:

    customers = filtered["User_ID"].nunique()

else:

    customers = len(filtered)


# ============================================================
# KPI DISPLAY
# ============================================================

st.divider()

k1, k2, k3, k4 = st.columns(4)

with k1:

    st.metric(
        "💰 Total Sales",
        f"₹{total_sales:,.0f}"
    )

with k2:

    st.metric(
        "📦 Total Orders",
        f"{total_orders:,.0f}"
    )

with k3:

    st.metric(
        "💳 Average Sale",
        f"₹{average_sale:,.0f}"
    )

with k4:

    st.metric(
        "👥 Customers",
        f"{customers:,.0f}"
    )


st.divider()


# ============================================================
# TABS
# ============================================================

overview, customers_tab, products_tab, geography_tab, analytics_tab = st.tabs(
    [
        "📊 Overview",
        "👥 Customers",
        "🛍️ Products",
        "🌎 Geography",
        "📈 Analytics"
    ]
)


# ============================================================
# PLOT FUNCTION
# ============================================================

def professional_layout(fig, height=450):

    fig.update_layout(
        template="plotly_white",
        height=height,
        margin=dict(
            l=30,
            r=30,
            t=70,
            b=30
        ),
        hovermode="x unified",
        transition_duration=700
    )

    return fig


# ============================================================
# OVERVIEW
# ============================================================

with overview:

    st.markdown(
        '<div class="section-header">📊 Sales Overview</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">'
        'Understand customer demographics and revenue performance.'
        '</div>',
        unsafe_allow_html=True
    )


    # Gender
    if "Gender" in filtered.columns:

        gender_sales = (
            filtered.groupby("Gender", as_index=False)["Amount"]
            .sum()
            .sort_values("Amount", ascending=False)
        )

        fig = px.bar(
            gender_sales,
            x="Gender",
            y="Amount",
            text_auto=".2s",
            title="💰 Sales by Gender"
        )

        fig = professional_layout(fig)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


    # Age
    if "Age Group" in filtered.columns:

        age_sales = (
            filtered.groupby("Age Group", as_index=False)["Amount"]
            .sum()
        )

        fig = px.bar(
            age_sales,
            x="Age Group",
            y="Amount",
            text_auto=".2s",
            title="🎂 Sales by Age Group"
        )

        fig = professional_layout(fig)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


    # Category donut
    if "Product_Category" in filtered.columns:

        category_sales = (
            filtered.groupby(
                "Product_Category",
                as_index=False
            )["Amount"]
            .sum()
            .sort_values(
                "Amount",
                ascending=False
            )
            .head(top_n)
        )

        fig = px.pie(
            category_sales,
            names="Product_Category",
            values="Amount",
            hole=0.55,
            title="🛍️ Revenue Contribution"
        )

        fig = professional_layout(fig, 500)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


# ============================================================
# CUSTOMERS
# ============================================================

with customers_tab:

    st.markdown(
        '<div class="section-header">👥 Customer Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">'
        'Analyze customer contribution and sales distribution.'
        '</div>',
        unsafe_allow_html=True
    )


    if "User_ID" in filtered.columns:

        customer_sales = (
            filtered.groupby(
                "User_ID",
                as_index=False
            )["Amount"]
            .sum()
            .sort_values(
                "Amount",
                ascending=False
            )
            .head(top_n)
        )

        fig = px.bar(
            customer_sales,
            x="User_ID",
            y="Amount",
            text_auto=".2s",
            title=f"🏆 Top {top_n} Customers"
        )

        fig = professional_layout(fig, 500)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


    if "Gender" in filtered.columns:

        fig = px.box(
            filtered,
            x="Gender",
            y="Amount",
            title="📦 Sales Distribution by Gender"
        )

        fig = professional_layout(fig)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


# ============================================================
# PRODUCTS
# ============================================================

with products_tab:

    st.markdown(
        '<div class="section-header">🛍️ Product Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">'
        'Identify the strongest product categories and order patterns.'
        '</div>',
        unsafe_allow_html=True
    )


    if "Product_Category" in filtered.columns:

        product_sales = (
            filtered.groupby(
                "Product_Category",
                as_index=False
            )["Amount"]
            .sum()
            .sort_values(
                "Amount",
                ascending=False
            )
            .head(top_n)
        )

        fig = px.bar(
            product_sales,
            x="Amount",
            y="Product_Category",
            orientation="h",
            text_auto=".2s",
            title=f"💰 Top {top_n} Product Categories"
        )

        fig.update_yaxes(
            categoryorder="total ascending"
        )

        fig = professional_layout(fig, 550)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


    if (
        "Product_Category" in filtered.columns
        and
        "Orders" in filtered.columns
    ):

        product_orders = (
            filtered.groupby(
                "Product_Category",
                as_index=False
            )["Orders"]
            .sum()
            .sort_values(
                "Orders",
                ascending=False
            )
            .head(top_n)
        )

        fig = px.bar(
            product_orders,
            x="Product_Category",
            y="Orders",
            text_auto=".2s",
            title=f"📦 Top {top_n} Categories by Orders"
        )

        fig = professional_layout(fig, 500)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


# ============================================================
# GEOGRAPHY
# ============================================================

with geography_tab:

    st.markdown(
        '<div class="section-header">🌎 Geographic Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">'
        'Compare sales and orders across different states.'
        '</div>',
        unsafe_allow_html=True
    )


    if "State" in filtered.columns:

        state_sales = (
            filtered.groupby(
                "State",
                as_index=False
            )["Amount"]
            .sum()
            .sort_values(
                "Amount",
                ascending=False
            )
            .head(top_n)
        )

        fig = px.bar(
            state_sales,
            x="State",
            y="Amount",
            text_auto=".2s",
            title=f"📍 Top {top_n} States by Revenue"
        )

        fig = professional_layout(fig, 550)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


    if (
        "State" in filtered.columns
        and
        "Orders" in filtered.columns
    ):

        state_orders = (
            filtered.groupby(
                "State",
                as_index=False
            )["Orders"]
            .sum()
            .sort_values(
                "Orders",
                ascending=False
            )
            .head(top_n)
        )

        fig = px.bar(
            state_orders,
            x="State",
            y="Orders",
            text_auto=".2s",
            title=f"📦 Top {top_n} States by Orders"
        )

        fig = professional_layout(fig, 550)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


# ============================================================
# ANALYTICS
# ============================================================

with analytics_tab:

    st.markdown(
        '<div class="section-header">📈 Advanced Analytics</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-text">'
        'Explore sales distribution and numerical relationships.'
        '</div>',
        unsafe_allow_html=True
    )


    # Distribution
    fig = px.histogram(
        filtered,
        x="Amount",
        nbins=35,
        marginal="box",
        title="💰 Sales Amount Distribution"
    )

    fig = professional_layout(fig, 500)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={"displaylogo": False}
    )


    # Correlation
    numeric = filtered.select_dtypes(
        include=np.number
    )

    if numeric.shape[1] >= 2:

        correlation = numeric.corr()

        fig = px.imshow(
            correlation,
            text_auto=".2f",
            aspect="auto",
            title="🔗 Correlation Matrix"
        )

        fig = professional_layout(fig, 550)

        st.plotly_chart(
            fig,
            use_container_width=True,
            config={"displaylogo": False}
        )


# ============================================================
# BUSINESS INSIGHTS
# ============================================================

st.divider()

st.markdown(
    '<div class="section-header">💡 Automated Business Insights</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-text">'
    'Important observations from the selected dataset.'
    '</div>',
    unsafe_allow_html=True
)


if "Gender" in filtered.columns:

    best_gender = (
        filtered.groupby("Gender")["Amount"]
        .sum()
        .idxmax()
    )

    st.success(
        f"👤 Highest revenue gender: **{best_gender}**"
    )


if "Age Group" in filtered.columns:

    best_age = (
        filtered.groupby("Age Group")["Amount"]
        .sum()
        .idxmax()
    )

    st.info(
        f"🎂 Highest revenue age group: **{best_age}**"
    )


if "State" in filtered.columns:

    best_state = (
        filtered.groupby("State")["Amount"]
        .sum()
        .idxmax()
    )

    st.success(
        f"📍 Highest revenue state: **{best_state}**"
    )


if "Product_Category" in filtered.columns:

    best_category = (
        filtered.groupby(
            "Product_Category"
        )["Amount"]
        .sum()
        .idxmax()
    )

    st.info(
        f"🛍️ Best performing category: **{best_category}**"
    )


if "Occupation" in filtered.columns:

    best_occupation = (
        filtered.groupby(
            "Occupation"
        )["Amount"]
        .sum()
        .idxmax()
    )

    st.success(
        f"💼 Highest revenue occupation: **{best_occupation}**"
    )


# ============================================================
# DATASET INFO
# ============================================================

st.divider()

st.info(
    f"📌 Currently analyzing **{len(filtered):,} records**"
)


with st.expander("🔎 View Filtered Dataset"):

    st.dataframe(
        filtered,
        use_container_width=True,
        height=350
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "📊 Sales Analytics Dashboard  •  "
    "Built with Streamlit • Pandas • Plotly  •  "
    "Interactive Sales Data Analysis & Business Insights"
)