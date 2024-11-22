import streamlit as st
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Food Sales Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Updated CSS with fixed styling
st.markdown("""
    <style>
    /* Main background color */
    .stApp {
        background-color: #16b0a0 !important;
    }
    
    /* Remove all default padding */
    .main {
        padding: 1rem !important;
    }
    
    /* Header styles */
    .header {
        background: linear-gradient(135deg, #1e88e5, #1565c0);
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        text-align: center;
        overflow: hidden;
    }
    
    /* Logo container styles */
    .logo-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 10px;
    }
    
    .food-logo {
        font-size: 3rem;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0% {
            transform: translateY(0px);
        }
        50% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0px);
        }
    }
    
    /* Bouncing text animation */
    .bouncing-text {
        display: inline-block;
        margin: 0;
        color: white;
        font-size: 2rem;
        font-weight: bold;
    }
    
    .letter {
        display: inline-block;
        opacity: 0;
        animation: bounce-in 0.8s cubic-bezier(0.18, 0.89, 0.32, 1.28) forwards;
    }
    
    @keyframes bounce-in {
        0% {
            transform: translateY(-100px);
            opacity: 0;
        }
        60% {
            transform: translateY(20px);
            opacity: 1;
        }
        80% {
            transform: translateY(-10px);
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }
    
    /* Filter group styles */
    .filters {
        background-color: white;
        padding: 30px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 20px;
    }
    
    .filter-group {
        width: 60%;
        text-align: center;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Data table styling */
    [data-testid="stDataFrame"] {
        background-color: #16b0a0;
        padding: 1rem;
        border-radius: 8px;
    }
    
    /* Filter label styling */
    .filter-label {
        color: white;
        font-size: 1.1rem;
        font-weight: 800;
        margin-bottom: 8px;
        text-align: center;
        font-family: sans-serif;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        return pd.read_csv('sampledatafoodsales_analysis.csv')
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

df = load_data()

if df is not None:
    # Header with food logo and bouncing text
    st.markdown("""
        <div class="header">
            <div class="logo-container">
                <div class="food-logo">🍽️</div>
                <h1 class="bouncing-text">
                    <span class="letter" style="animation-delay: 0.1s">W</span>
                    <span class="letter" style="animation-delay: 0.2s">E</span>
                    <span class="letter" style="animation-delay: 0.3s">L</span>
                    <span class="letter" style="animation-delay: 0.4s">C</span>
                    <span class="letter" style="animation-delay: 0.5s">O</span>
                    <span class="letter" style="animation-delay: 0.6s">M</span>
                    <span class="letter" style="animation-delay: 0.7s">E</span>
                    <span class="letter" style="animation-delay: 0.8s">&nbsp;</span>
                    <span class="letter" style="animation-delay: 0.9s">T</span>
                    <span class="letter" style="animation-delay: 1.0s">O</span>
                    <span class="letter" style="animation-delay: 1.1s">&nbsp;</span>
                    <span class="letter" style="animation-delay: 1.2s">F</span>
                    <span class="letter" style="animation-delay: 1.3s">O</span>
                    <span class="letter" style="animation-delay: 1.4s">O</span>
                    <span class="letter" style="animation-delay: 1.5s">D</span>
                    <span class="letter" style="animation-delay: 1.6s">&nbsp;</span>
                    <span class="letter" style="animation-delay: 1.7s">S</span>
                    <span class="letter" style="animation-delay: 1.8s">A</span>
                    <span class="letter" style="animation-delay: 1.9s">L</span>
                    <span class="letter" style="animation-delay: 2.0s">E</span>
                    <span class="letter" style="animation-delay: 2.1s">S</span>
                    <span class="letter" style="animation-delay: 2.2s">&nbsp;</span>
                    <span class="letter" style="animation-delay: 2.3s">D</span>
                    <span class="letter" style="animation-delay: 2.4s">A</span>
                    <span class="letter" style="animation-delay: 2.5s">S</span>
                    <span class="letter" style="animation-delay: 2.6s">H</span>
                    <span class="letter" style="animation-delay: 2.7s">B</span>
                    <span class="letter" style="animation-delay: 2.8s">O</span>
                    <span class="letter" style="animation-delay: 2.9s">A</span>
                    <span class="letter" style="animation-delay: 3.0s">R</span>
                    <span class="letter" style="animation-delay: 3.1s">D</span>
                </h1>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Filters
    col1, col2, col3 = st.columns(3)
    
    # Get unique dates
    dates = sorted(df['Date'].unique())
    
    with col1:
        st.markdown('<div class="filter-group">', unsafe_allow_html=True)
        st.markdown('<p class="filter-label">Date</p>', unsafe_allow_html=True)
        selected_date = st.selectbox(
            'Select Date',
            options=['All Dates'] + dates,
            key='date',
            label_visibility="collapsed"
        )

    with col2:
        st.markdown('<div class="filter-group">', unsafe_allow_html=True)
        st.markdown('<p class="filter-label">City:</p>', unsafe_allow_html=True)
        city = st.selectbox(
            'City',
            options=['All Cities'] + sorted(df['City'].unique().tolist()),
            key='city',
            label_visibility="collapsed"
        )

    with col3:
        st.markdown('<div class="filter-group">', unsafe_allow_html=True)
        st.markdown('<p class="filter-label">Category:</p>', unsafe_allow_html=True)
        category = st.selectbox(
            'Category',
            options=['All Categories'] + sorted(df['Category'].unique().tolist()),
            key='category',
            label_visibility="collapsed"
        )

    # Filter data
    filtered_df = df.copy()

    if selected_date != 'All Dates':
        filtered_df = filtered_df[filtered_df['Date'] == selected_date]
    if city != 'All Cities':
        filtered_df = filtered_df[filtered_df['City'] == city]
    if category != 'All Categories':
        filtered_df = filtered_df[filtered_df['Category'] == category]

    # Display data table
    st.dataframe(
        filtered_df,
        column_config={
            "ID": st.column_config.TextColumn("ID"),
            "Date": st.column_config.TextColumn("Date"),
            "Region": st.column_config.TextColumn("Region"),
            "City": st.column_config.TextColumn("City"),
            "Category": st.column_config.TextColumn("Category"),
            "Product": st.column_config.TextColumn("Product"),
            "Qty": st.column_config.NumberColumn("Qty"),
            "UnitPrice": st.column_config.NumberColumn(
                "Unit Price ($)",
                format="$%.2f"
            ),
            "TotalPrice": st.column_config.NumberColumn(
                "Total Price ($)",
                format="$%.2f"
            )
        },
        hide_index=True,
        use_container_width=True
    )
else:
    st.error("Unable to load data. Please check if the CSV file exists in the correct location.")