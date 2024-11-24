import streamlit as st
import pandas as pd
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Food Sales Dashboard",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Updated CSS with fixed styling and bounce animation
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
        background-color: #3B82F6;
        padding: 1.5rem;
        border-radius: 8px;
        margin-bottom: 1.5rem;
        text-align: center;
    }
    
    /* Logo container styles */
    .logo-container {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }
    
    .food-logo {
        font-size: 3.5rem;
        animation: float 3s ease-in-out infinite;
        margin-bottom: 10px;
    }
    
    /* Welcome text styles with bounce animation */
    .welcome-text {
        color: white;
        margin: 0;
        font-size: 2.5rem;
        font-weight: 900;
        animation: bounce 1s ease-in-out;
    }
    
    /* Add bounce keyframes animation */
    @keyframes bounce {
        0% { transform: translateY(-100px); opacity: 0; }
        50% { transform: translateY(20px); }
        75% { transform: translateY(-10px); }
        100% { transform: translateY(0); opacity: 1; }
    }
    
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0px); }
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
        width: 100%;
        text-align: center;
        padding: 10px;
    }
    
    /* Date range container */
    .date-range-container {
        display: flex;
        gap: 20px;
        align-items: center;
        justify-content: center;
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

    /* Date input styling */
    [data-testid="stDateInput"] label {
        font-size: 1.1rem !important;
        font-weight: 800 !important;
        color: white !important;
    }

    /* Style for the date input container */
    [data-testid="stDateInput"] {
        margin-bottom: 0.5rem;
    }

    .date-input-label {
        color: white;
        font-size: 1.1rem;
        font-weight: 800;
        margin-bottom: 8px;
        text-align: center;
        font-family: sans-serif;
    }

    /* Style for the apply button */
    [data-testid="stButton"] {
        display: flex;
        justify-content: center;
        margin-top: 1rem;
    }

    /* Custom styles for date input */
    [data-testid="stDateInput"] input {
        font-size: 1.1rem !important;
        text-align: center !important;
        color: #333 !important;
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

    /* Info message styling */
    [data-testid="stInfo"] {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        font-size: 1.1rem;
        margin-top: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    try:
        # Read the specific sheet 'FoodSales' from the Excel file
        df = pd.read_excel('sampledatafoodsales_analysis .xlsx', sheet_name='FoodSales')
        # Convert date column to datetime
        df['Date'] = pd.to_datetime(df['Date'])
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None

# Load the initial data for getting filter values
df = load_data()

if df is not None:
    # Header with food logo and welcome text
    st.markdown("""
        <div class="header">
            <div class="logo-container">
                <div class="food-logo">🍽️</div>
                <h1 class="welcome-text">Welcome to Food Sales Dashboard</h1>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Initialize session state for tracking filter selections
    if 'filter_applied' not in st.session_state:
        st.session_state.filter_applied = False

    # Get min and max dates from the dataset
    min_date = datetime(2018, 1, 1).date()  # Set minimum date to January 1, 2018
    max_date = datetime(2023, 12, 31).date()  # Set maximum date to December 31, 2023

    # Filters
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown('<div class="filter-group">', unsafe_allow_html=True)
        
        date_col1, date_col2 = st.columns(2)
        
        with date_col1:
            st.markdown('<p class="date-input-label">Start Date</p>', unsafe_allow_html=True)
            start_date = st.date_input(
                "",
                value=datetime(2018, 1, 1).date(),  # Set default start date to January 1, 2018
                min_value=min_date,
                max_value=max_date,
                key='start_date',
                label_visibility="collapsed",
                format="MM/DD/YYYY"
            )
            
        with date_col2:
            st.markdown('<p class="date-input-label">End Date</p>', unsafe_allow_html=True)
            end_date = st.date_input(
                "",
                value=datetime(2023, 12, 31).date(),  # Set default end date to December 31, 2023
                min_value=start_date,  # Ensure end date is not before start date
                max_value=max_date,
                key='end_date',
                label_visibility="collapsed",
                format="MM/DD/YYYY"
            )

    with col2:
        st.markdown('<div class="filter-group">', unsafe_allow_html=True)
        st.markdown('<p class="filter-label">City</p>', unsafe_allow_html=True)
        city = st.selectbox(
            'City',
            options=['All Cities'] + sorted(df['City'].unique().tolist()),
            key='city',
            label_visibility="collapsed"
        )

    with col3:
        st.markdown('<div class="filter-group">', unsafe_allow_html=True)
        st.markdown('<p class="filter-label">Category</p>', unsafe_allow_html=True)
        category = st.selectbox(
            'Category',
            options=['All Categories'] + sorted(df['Category'].unique().tolist()),
            key='category',
            label_visibility="collapsed"
        )

    # Add Apply Filter button
    col1, col2, col3 = st.columns([4, 2, 4])
    with col2:
        if st.button('Search', type='primary'):
            st.session_state.filter_applied = True

    # Validate date range
    if start_date > end_date:
        st.error('Start date must be before or equal to end date')
    else:
        # Only show data when filters are applied
        if st.session_state.filter_applied:
            # Filter data
            filtered_df = df.copy()

            # Apply date filter
            filtered_df = filtered_df[
                (filtered_df['Date'].dt.date >= start_date) & 
                (filtered_df['Date'].dt.date <= end_date)
            ]
            
            if city != 'All Cities':
                filtered_df = filtered_df[filtered_df['City'] == city]
            if category != 'All Categories':
                filtered_df = filtered_df[filtered_df['Category'] == category]

            # Display data table
            st.dataframe(
                filtered_df,
                column_config={
                    "ID": st.column_config.TextColumn("ID"),
                    "Date": st.column_config.DateColumn(
                        "Date",
                        format="MM/DD/YYYY"
                    ),
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
    st.error("Unable to load data. Please check if the Excel file exists in the correct location.")
