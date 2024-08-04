Project Description-->

The CSV Analysis Project is a Django-based web application designed to allow users to upload CSV files, 
perform basic data analysis, and visualize the results. The application provides a simple interface for uploading files, 
viewing summary statistics, handling missing values, and displaying data visualizations.

(A) File Upload: Users can upload CSV files through a web form.
(B) Data Processing: The application uses pandas to read and analyze the data, calculating summary statistics and handling missing values.
(c) Data Visualization: The application generates and displays histograms of numerical data using matplotlib and seaborn.
(D) User Interface: A user-friendly web interface displays data analysis results and visualizations.

Setup Instructions-->

(1) Clone the Repository--> 
      git clone <repository_url>

(2) Create a Virtual Environment-->
      python -m venv venv

(3) Install Dependencies-->
      pip install -r requirements.txt

(4) Apply Migrations-->
      python manage.py migrate

(5) Run the Development Server-->
      python manage.py runserver


