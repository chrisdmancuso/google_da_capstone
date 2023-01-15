# Data Cleaning Documentation

Technologies used:

Google Sheets, BigQuery, Python

Basic process:

1) Upload the CSV to Google Sheets

![image](https://user-images.githubusercontent.com/31321037/212559707-e74c341f-23fa-43f0-8039-bf8465f57e4d.png)

2) Perform basic formatting and cleaning

  -Resize header cells
  -Use conditonal formatting to check for empty cells. Specifically, to accomplish our business task, we need to ensure that the columns concerning ride times and
  rider membership are not null.
  -Use filters on columns with binary data to ensure the integrity of the data. Specifically, the member_casual column should only contain 'casual' or 'member'
  -Trim whitespace
  -Check for and remove duplicates
  -Ensure column data types are correct
  -Take note of total number of rows per sheet
  -Take note of null values and which columns are affected. 
  Specifically, a significant number of entries are missing values for start_station_name, start_station_id, end_station_name, end_station_id. We'll consult with the team about those null values and possible options to fill in that data, 
  and in the meantime, will continue with the analysis with those null values included.
  -Download clean data into the previously created 'Cleaned_Cyclistic_01-15-23' folder as 'Cleaned_yyyymm-divvy-tripdata.csv'
  -Repeat until all files are cleaned
