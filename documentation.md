# Data Cleaning Documentation

**Technologies used:**

Google Sheets, BigQuery, Python

## Cleaning and Upload

**1) Upload the CSV files to Google Sheets**
---
![image](https://user-images.githubusercontent.com/31321037/212559707-e74c341f-23fa-43f0-8039-bf8465f57e4d.png)

**2) Perform basic formatting and cleaning**
---
  - Resize header cells.
  - Use conditional  formatting to check for empty cells. 
    - Specifically, to accomplish our business task, we need to ensure that the columns concerning ride times and
  rider membership are not null.
  - Use filters on columns with binary data to ensure the integrity of the data. 
    - The member_casual column should only contain 'casual' or 'member'.
  - Trim whitespace.
  - Check for and remove duplicates.
  - Ensure column data types are correct.
  - Take note of total number of rows per sheet.
  - Take note of null values and which columns are affected. 
    - A significant number of entries are missing values for start_station_name, start_station_id, end_station_name, end_station_id. We'll consult with the   team about those null values and possible options to fill in that data, 
  and in the meantime, will continue with the analysis with those null values included.
  - Download clean data into the previously created 'Cleaned_Cyclistic_01-15-23' folder as 'Cleaned_yyyymm-divvy-tripdata.csv'.
  - Repeat until all files are cleaned.

**Note:** While performing these actions, it was discovered that Google Sheets was incapable of processing the files from May to October due to the file sizes. 

![image](https://user-images.githubusercontent.com/31321037/212563412-d3bdc4d9-80e6-4ff8-b00e-fadff7dc456c.png)

Attempts to upload to BigQuery and Google Drive similarly failed. To circumvent this, [Python scripting was used to separate the files into two,](https://github.com/chrisdmancuso/google_da_capstone/blob/main/reduce_csv.py) and data cleaning proceeded as described above. Naming conventions for these files are handled by the Python script.

**3) Upload files to BigQuery**
---

Before uploading to BigQuery, we need to create a new project and dataset.

  1) Navigate to the BigQuery console and create a new project.

![image](https://user-images.githubusercontent.com/31321037/212565759-ab634595-6c9d-41fa-9f22-9d14b6864569.png)

  2) Navigate to the newly created project, and select the 3 dot option menu to create a new dataset.

![image](https://user-images.githubusercontent.com/31321037/212565801-8e6df095-5a14-49dd-b7c3-29161eeee1b4.png)

![image](https://user-images.githubusercontent.com/31321037/212566197-b9bfff47-d0e5-4ba2-9fb4-3caa6c76a2b0.png)

We are now ready to begin importing our CSVs into BigQuery.

1) Select the 3 dot option menu next to our dataset and select 'Create Table.'

![image](https://user-images.githubusercontent.com/31321037/212567139-bfe9bd56-13bf-4b61-8ae8-265b6f3f2264.png)

- For our source, we'll select 'Upload.' 
- Then, we'll select 'Browse' and navigate to our cleaned CSV file. The 'File Format' should automatically update to 'CSV.'
- Then, we'll name our table with the following convention: 'trips_mm'
- Then, we'll check the 'Auto detect' checkbox under the 'Schema' header.
- Finally, we'll confirm the project, dataset, and table names are correct, and then click 'Create Table'

![image](https://user-images.githubusercontent.com/31321037/212567854-47a7c77b-3fcd-4fd9-8752-a512ca5709bf.png)

We'll repeat this step for all of our complete CSVs. For our CSVs that were split into separate files, we'll perform the following steps to import them into our dataset.

1) Follow the above steps to create tables for our CSVs. Adjust table naming conventions to reflect the data: 'trips_mm_1st' and 'trips_mm_2nd'.
2) Run the following SQL queries to create main tables with the same schema as the complete files.
```
CREATE TABLE `capstone-bikes-374620.cyclistic_2022.trips_05` LIKE `capstone-bikes-374620.cyclistic_2022.trips_01`;
CREATE TABLE `capstone-bikes-374620.cyclistic_2022.trips_06` LIKE `capstone-bikes-374620.cyclistic_2022.trips_01`;
CREATE TABLE `capstone-bikes-374620.cyclistic_2022.trips_07` LIKE `capstone-bikes-374620.cyclistic_2022.trips_01`;
CREATE TABLE `capstone-bikes-374620.cyclistic_2022.trips_08` LIKE `capstone-bikes-374620.cyclistic_2022.trips_01`;
CREATE TABLE `capstone-bikes-374620.cyclistic_2022.trips_09` LIKE `capstone-bikes-374620.cyclistic_2022.trips_01`;
CREATE TABLE `capstone-bikes-374620.cyclistic_2022.trips_10` LIKE `capstone-bikes-374620.cyclistic_2022.trips_01`;
```

3) When separating our CSV files, our Python script added an additional column that we don't need. To remove, run the following commands.
```
ALTER TABLE `cyclistic_2022.trips_05_1st` DROP COLUMN int64_field_0; 
ALTER TABLE `cyclistic_2022.trips_05_2nd` DROP COLUMN int64_field_0;
ALTER TABLE `cyclistic_2022.trips_06_1st` DROP COLUMN int64_field_0; 
ALTER TABLE `cyclistic_2022.trips_06_2nd` DROP COLUMN int64_field_0;
ALTER TABLE `cyclistic_2022.trips_07_1st` DROP COLUMN int64_field_0; 
ALTER TABLE `cyclistic_2022.trips_07_2nd` DROP COLUMN int64_field_0;
ALTER TABLE `cyclistic_2022.trips_08_1st` DROP COLUMN int64_field_0; 
ALTER TABLE `cyclistic_2022.trips_08_2nd` DROP COLUMN int64_field_0;
ALTER TABLE `cyclistic_2022.trips_09_1st` DROP COLUMN int64_field_0; 
ALTER TABLE `cyclistic_2022.trips_09_2nd` DROP COLUMN int64_field_0;
ALTER TABLE `cyclistic_2022.trips_10_1st` DROP COLUMN int64_field_0; 
ALTER TABLE `cyclistic_2022.trips_10_2nd` DROP COLUMN int64_field_0;
```

4) Then, insert our separated tables into the main tables with the following commands.
```
INSERT INTO `cyclistic_2022.trips_05` SELECT * FROM `cyclistic_2022.trips_05_1st`; 
INSERT INTO `cyclistic_2022.trips_05` SELECT * FROM `cyclistic_2022.trips_05_2nd`;
INSERT INTO `cyclistic_2022.trips_06` SELECT * FROM `cyclistic_2022.trips_06_1st`; 
INSERT INTO `cyclistic_2022.trips_06` SELECT * FROM `cyclistic_2022.trips_06_2nd`;
INSERT INTO `cyclistic_2022.trips_07` SELECT * FROM `cyclistic_2022.trips_07_1st`; 
INSERT INTO `cyclistic_2022.trips_07` SELECT * FROM `cyclistic_2022.trips_07_2nd`;
INSERT INTO `cyclistic_2022.trips_08` SELECT * FROM `cyclistic_2022.trips_08_1st`; 
INSERT INTO `cyclistic_2022.trips_08` SELECT * FROM `cyclistic_2022.trips_08_2nd`;
INSERT INTO `cyclistic_2022.trips_09` SELECT * FROM `cyclistic_2022.trips_09_1st`; 
INSERT INTO `cyclistic_2022.trips_09` SELECT * FROM `cyclistic_2022.trips_09_2nd`;
INSERT INTO `cyclistic_2022.trips_10` SELECT * FROM `cyclistic_2022.trips_10_1st`; 
INSERT INTO `cyclistic_2022.trips_10` SELECT * FROM `cyclistic_2022.trips_10_2nd`;
```

5) Finally, create a main table to aggregate our data into one source, and insert all other tables into it.
```
CREATE TABLE `capstone-bikes-374620.cyclistic_2022.trips_all` LIKE `capstone-bikes-374620.cyclistic_2022.trips_01`;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_01;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_02;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_03;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_04;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_05;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_06;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_07;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_08;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_09;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_10;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_11;
INSERT INTO `cyclistic_2022.trips_all` SELECT * FROM `cyclistic_2022.trips_12;
```

6) Double check our calculated aggregate row totals from CSV and BigQuery are equal.
```
SELECT COUNT(*) FROM `cyclistic_2022.trips_all`
```
- We should have 5,667,717 results

Before we start our analysis, we'll perform three more data manipulations to complete our data.

1) While exploring the data, it was discovered that 531 entries had trip end times before start times, or end times equal to start times. We'll remove these entries from our dataset. 
```
DELETE FROM capstone-bikes-374620.cyclistic_2022.trips_all
WHERE ended_at < started_at OR ended_at = started_at
```

2) After exploring the data, it was discovered that a significant amount of entries exist where the trip duration falls significantly outside the normal expected values, from trip durations of 1 second to 600 plus hours. After consulting with management, the decision was made to ignore results under 2 minutes, and results over 9 hours. The following queries will create a new table with the adjusted data.
```
CREATE TABLE `capstone-bikes-374620.cyclistic_2022`.trips_trunc(ride_id STRING, rideable_type STRING, 
  started_at TIMESTAMP, ended_at TIMESTAMP, trip_duration INTERVAL, day_of_week INTEGER, membership STRING);
INSERT INTO `capstone-bikes-374620.cyclistic_2022.trips_trunc` 
SELECT 
  ride_id, 
  rideable_type, 
  started_at,
  ended_at, 
  ended_at - started_at, 
  EXTRACT(DAYOFWEEK FROM started_at), 
  member_casual 
FROM `capstone-bikes-374620.cyclistic_2022.trips_all`;
SELECT 
  ride_id,
  rideable_type,
  membership,
  TIME(EXTRACT(HOUR FROM trip_duration), EXTRACT(MINUTE FROM trip_duration), EXTRACT(SECOND FROM trip_duration)) AS trip_duration,
  started_at,
  ended_at,
  day_of_week,
  
FROM `capstone-bikes-374620.cyclistic_2022.trips_trunc`
WHERE EXTRACT(HOUR FROM trip_duration) <= 9 AND CAST(trip_duration AS STRING) > '0-0 0 0:2:0'
ORDER BY trip_duration ASC;

``` 
3) Finally, we'll export the results to our Google Drive as CSV using BigQuery.

![image](https://user-images.githubusercontent.com/31321037/212783967-af7ea1d6-a02e-4912-bc08-627b8291022f.png)

With these steps complete, we can begin our analysis.

**NOTE:** During the analysis, it was determined that station id's and latitude and longitude coordinates could be necessary for data visualizations. The following queries will include those points, in addition to the above.
```
SELECT 
  `capstone-bikes-374620.cyclistic_2022.trips_trunc`.ride_id, 
  `capstone-bikes-374620.cyclistic_2022.trips_trunc`.rideable_type,
  day_of_week, 
  membership, 
  TIME(EXTRACT(HOUR FROM trip_duration), EXTRACT(MINUTE FROM trip_duration), EXTRACT(SECOND FROM trip_duration)) AS trip_duration,
  start_station_id, 
  start_station_name, 
  end_station_id, 
  end_station_name, 
  start_lat,
  start_lng,
  end_lat,
  end_lng
FROM `capstone-bikes-374620.cyclistic_2022.trips_all` 
LEFT JOIN `capstone-bikes-374620.cyclistic_2022.trips_trunc`
ON `capstone-bikes-374620.cyclistic_2022.trips_all`.ride_id = `capstone-bikes-374620.cyclistic_2022.trips_trunc`.ride_id
WHERE (start_station_id IS NOT NULL OR start_station_name IS NOT NULL) AND (end_station_id IS NOT NULL OR end_station_name IS NOT NULL) 
  AND EXTRACT(HOUR FROM trip_duration) < 24
  AND TIME(EXTRACT(HOUR FROM trip_duration), EXTRACT(MINUTE FROM trip_duration), EXTRACT(SECOND FROM trip_duration)) BETWEEN '00:02:00' AND '09:00:00'
```
