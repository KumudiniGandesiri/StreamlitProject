Streamlit Data Visualization App

Overview
The Streamlit Data Visualization App is a simple web application built with Streamlit, designed for interactive data exploration and visualization. It allows users to upload datasets, perform basic exploratory data analysis (EDA), and generate a variety of plots using common data visualization libraries.

This project serves as a powerful tool for anyone who wants to visualize data quickly and interactively without needing to write extensive code.

Features
File Upload: Supports CSV file uploads for data analysis.
Data Preview: Displays the first few rows of the dataset for inspection.
Basic Statistics: Shows summary statistics of the dataset, including mean, median, and standard deviation.
Interactive Plots: Allows users to create different types of charts such as:
Line Charts
Bar Charts
Scatter Plots
Histograms

Customizable Visualizations: Users can choose which columns to visualize and customize the type of plot.
Technologies Used
Backend: Python, Streamlit
Visualization Libraries: Pandas, Matplotlib, Seaborn, Plotly
Installation
Prerequisites
Python 3.x
Pip (Python package manager)


teps to Run Locally
Clone the repository:

bash
Copy code
git clone https://github.com/KumudiniGandesiri/StreamlitProject.git
cd streamlit-app
Create and activate a virtual environment (optional):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Open your browser and go to http://localhost:8501/ to interact with the app.

Project Structure
plaintext
Copy code
├── app.py                  # Main Streamlit app file
├── requirements.txt        # List of dependencies
├── datasets/               # Folder for storing sample datasets (optional)
├── README.md               # Project documentation
└── .gitignore              # Git ignore file
Usage
Upload a Dataset:

On the app's homepage, click the "Browse files" button to upload a CSV file for analysis.
Data Preview:

The app will automatically display the first 5 rows of the uploaded dataset.
Exploratory Data Analysis:

Summary statistics of the dataset (mean, median, standard deviation) are automatically calculated and displayed.
Visualizations:

Select the type of chart you want to generate (e.g., line chart, bar chart, scatter plot) from the sidebar.
Choose the columns from the dataset you want to visualize, and Streamlit will render the chart interactively.
Screenshots
(Include screenshots to showcase the app's features, such as file upload, data preview, and charts)

Example Datasets
You can use any publicly available dataset (in CSV format) to test the app, or download and use one of the sample datasets provided in the datasets/ folder.

