# Analysis Documentation

### Technologies used:

R programming language, ggplot2, tidyverse, lubridate, readr

## Setup

Before we begin our analysis, we'll perform some basic setup steps within R studio. For our analysis, we'll need the R packages
ggplot2, tidyverse, readr, and lubridate. To install and load the packages, we can run the following code. Repeat while replacing
the package name to install and load all of the necessary packages.
```
install.packages("ggplot2")
library("ggplot2")
```
Alternatively, we can load the packages by forgoing the library function, and using the "packages" tab in the bottom right window
in R Studio. Once we've installed and loaded our packages, we can begin our analysis.

## Analysis

To start our analysis, we'll begin by loading our cleaned CSV into R Studio as a dataframe by using the read_csv function
from readr.

```
df <- read_csv("cleaned_cyclistic_data_01-16-23.csv")
```
This code assumes the file is in the current working directory. To check the current working directory, and change it if desired,
run the following code.
```
getwd()
setwd("path/of/the/desired/directory")
```
After following these steps, we'll now have a dataframe of our cleaned data within R.

To start, we'll check to ensure the columns were properly read and assigned. Run the following command to print all of the column names to the console.
```
colnames(df)
```
![image](https://user-images.githubusercontent.com/31321037/213304648-1b1e84a2-d980-45de-83c8-c08a058114cd.png)

With our data, we should have 13 columns.

We can further ensure the accuracy of our data by displaying a tibble with the following command.
```
tibble(df)
```
![image](https://user-images.githubusercontent.com/31321037/213304714-59cbeefd-65d3-4c9b-a72e-6e883c5b1179.png)

This will display the first ten results from our dataframe, while also displaying some of our columns and the data types of those columns. Alternatively, we can
use the head function to display all of the columns with 6 rows of data, or the str function to display column names and types, and return the first few rows of data.
```
head(df)
```
![image](https://user-images.githubusercontent.com/31321037/213304971-54219000-b6a3-4bc0-8b04-47b01b83e606.png)

```
str(df)
```
![image](https://user-images.githubusercontent.com/31321037/213305563-7564c335-f595-4406-93c4-e75e228b9c73.png)

After inspecting our data and verifying it's accuracy compared to our cleaned CSV file, we can perform some basic statistical analysis to discover insights to help us answer
our business task.

1) First we'll calculate basic statistics for the trip_duration column. We'll find the mean, median, max, and min.
```
mean(df$trip_duration)
median(df$trip_duration)
max(df$trip_duration)
min(df$trip_duration)
```
We discover that the mean trip duration is 1019.03 seconds, or approximately 16.98 minutes. The median trip duration is 658 secs, or approximately 10.96 minutes.
The max and min are 32386 and 120 seconds, or 9 hours and 2 minutes, respectively, which is the expected value range that we set while cleaning our data.

2) Next, we'll calculate the same statistics, but separated by membership
```
aggregate(df$trip_duration ~ df$membership, FUN=mean)
aggregate(df$trip_duration ~ df$membership, FUN=median)
aggregate(df$trip_duration ~ df$membership, FUN=max)
aggregate(df$trip_duration ~ df$membership, FUN=min)
```
We discover, based on our data range, that the min and max trip duration for both casual and members are equal at 2 minutes and 9 hours, respectively. However, the mean
and median both lean in favor of the casual rider, with the mean being 1397.0479s (23.28m) and the median being 854s (14.23m), compared to the members mean 761.3836s 
(12.69m) and median 559s (9.31m).

We'll continue our analysis by calculating statistics for trip duration, grouped by day and membership.
```
dfmean <- aggregate(df$trip_duration ~ df$membership + df$day_of_week, FUN=mean)
dfmed <- aggregate(df$trip_duration ~ df$membership + df$day_of_week, FUN=median)
view(dfmean)
view(dfmed)
```
On the left, the mean table, and on the right, the median table. Sunday is the start of the week, and is represented with '1', and Saturday is the end of the week, represented
with '7.'

![image](https://user-images.githubusercontent.com/31321037/213311957-8e23cd01-cd5c-4ec1-aca8-70180a61187a.png)
![image](https://user-images.githubusercontent.com/31321037/213312204-ea95c78c-8a04-444a-aca1-88a8ad629742.png)

First, this confirms our previous findings that casual riders tend to ride for longer durations than members. Second, by filtering trip duration in descending order,
we can see that Saturday and Sunday are when the longest trips are typically taken for both groups. Third, there may be a trend of casual ride durations dropping more sharply during the weekdays
when compared to members. We'll visualize this in R with a bar graph to explore further.
```
df %>% group_by(membership, day_of_week) %>% 
summarise(number_of_rides=n(), average_duration=mean(trip_duration)) %>% 
arrange(membership, day_of_week) %>% 
ggplot(aes(x=day_of_week, y=average_duration, fill=membership)) + 
geom_col(position = "dodge") + 
labs(title="Average Trip Duration by Day and Membership") + 
xlab("Days of the Week") + 
ylab("Average Trip Duration (Seconds)") + 
scale_x_continuous(breaks=seq(1, 7, 1), labels=c("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))

df %>% group_by(membership, day_of_week) %>% 
summarise(number_of_rides=n(), median_duration=median(trip_duration)) %>% 
arrange(membership, day_of_week) %>% 
ggplot(aes(x=day_of_week, y=median_duration, fill=membership)) + 
geom_col(position = "dodge") + 
labs(title="Median Trip Duration by Day and Membership") + 
xlab("Days of the Week") + 
ylab("Median Trip Duration (minutes)") + 
scale_x_continuous(breaks=seq(1, 7, 1), labels=c("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"))
```
![image](https://user-images.githubusercontent.com/31321037/213342890-da0bc787-757b-4ff5-afda-601d75f261a0.png)
![image](https://user-images.githubusercontent.com/31321037/213343560-ac8e5489-f324-4b3a-8c19-9bc40e05a83f.png)


At a quick glance, the data seems to show that casual trip duration falls off at a faster rate than members when entering the beginning of the week.
Doing some quick math, we can see that the relative, day-to-day change for casual riders looks like this

**Mean:** Sun(0%) -> Mon(-10%) -> Tue(-14%) -> Wed(-3%). This results in a change of -24% from Sun(1588.7415s) -> Wed(1208.2288s) 

**Median:** Sun(0%) -> Mon(-14%) -> Tue(-12%) -> Wed(-1%). This results in a change of -25%  from Sun(992s) -> Wen(744s)

While the relative change day-to-day for members looks like this

**Mean:** Sun(0%) -> Mon(-14%) -> Tue(-2%) -> Wed(+1%). This results in a change of -15% from Sun(849.2829s) -> Wed(725.7085s)

**Median:** Sun(0%) -> Mon(-13%) -> Tue(0%) -> Wed(+1%). This results in a change of -11% from Sun(613s) -> Wed(543s)

3) After calculating statistics for trip_duration, we'll calculate the total number of trips by day and membership.
```
df %>% group_by(membership, day_of_week) %>% 
summarise(number_of_rides=n(), average_duration=mean(trip_duration)) %>% 
arrange(membership, day_of_week)
```

![image](https://user-images.githubusercontent.com/31321037/213345827-983a1214-694f-4e2b-b7b9-c43d823cc646.png)

Based on this table, we can reasonably assume that members are taking more trips during the work week, while casual riders are more active during the weekend.
We can also infer that members take more trips than casual riders.
Some quick calculations can back this insight up. Percentages are relative to the previous day.

**Casual(Percent):** Sun(0%) -> Mon(-30%) -> Tue(-7%) -> Wed(+4%) -> Thu(+13%) -> Fri(+8%) -> Sat(+48%)

**Casual(Count):** Sun(293010) -> Mon(205069) -> Tue(191246) -> Wed(198172) -> Thu(224008) -> Fri(242085) -> Sat(357430)

**Member(Percent):** Sun(0%) -> Mon(+26%) -> Tue(+10%) -> Wed(0%) -> Thu(+1%) -> Fri(-13%) -> Sat(-6%)

**Member(Count):** Sun(286054) -> Mon(360567) -> Tue(395644) -> Wed(397067) -> Thu(399780) -> Fri(346081) -> Sat(325211)


4) A quick summation shows that casual trips equals 1,711,020, while member trips equals 2,510,404. We'll visualize this so we can quickly communicate this
```
df %>% group_by(membership, day_of_week) %>% 
summarise(number_of_rides=n()) %>% 
arrange(membership, day_of_week) %>% 
ggplot(aes(x=day_of_week, y=number_of_rides, fill=membership)) + 
geom_col(position="dodge") + 
labs(title="Total Trips by Day and Membership") + 
xlab("Days of the Week") + ylab("Total Trips") + 
scale_x_continuous(breaks=seq(1, 7, 1), labels=c("Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat")) + scale_y_continuous(labels=scales::comma)
```
![image](https://user-images.githubusercontent.com/31321037/213341546-84df7fca-50a2-48b8-bab5-de9377a5ed1d.png)

5) Export the aggregate tables to CSV for ease of access
```
counts <- df %>% group_by(membership, day_of_week) %>% 
summarise(number_of_rides=n(), average_duration=mean(trip_duration)) %>% 
arrange(membership, day_of_week)
write.csv(counts, 'avg_trip_duration.csv')

counts <- df %>% group_by(membership, day_of_week) %>%
summarise(number_of_rides=n(), median_duration=median(trip_duration)) %>% 
arrange(membership, day_of_week)
write.csv(counts, 'med_trip_duration.csv')
```

# Summary


## Casual Riders

Casual riders are more active during the weekends, taking 293,010 trips on Sunday, and 357,430 trips on Saturday. 
Casual riders are less active during Monday thru Friday,
seeing their trip numbers fall between 191,246 and 242,085, with the lowest number of trips occuring on Tuesday(191,246).
Casual riders average trip duration is 23.28 minutes, and the median trip duration is 14.23 minutes.
Casual riders take longer trips on the weekends, around 26 minutes on average, with a median of around 16.5 minutes.
During the week, casual riders ride for 21.5 minutes on average, with a median of around 13.1 minutes.

## Members

Members are more active during the weekdays, taking between 360,567 and 399,780 trips, with Thursday having the highest number of trips(399,780).
Members are less active during the weekend, with 325,211 trips on Saturday, and a low of 286,054 on Sunday.
Members average trip duration is 12.69 minutes, and the median trip duration is 9.31 minutes.
Members take longer trips on the weekends, around 14.18 minutes on average, with a median of around 10.32 minutes.
During the week, members ride for 12.2 minutes on average, with a median of around 9.4 minutes.

## Comparisons

Casual riders are more active during the weekend than members, taking 650,440 total trips, compared to 611,265 trips. Casual riders will ride, on average, for longer
periods of time than members throughout the entire week, riding on the weekends for an average of 26 minutes compared to 14.18 minutes, and 21.5 minutes compared to 12.2 minutes
during the week. Casual riders also have a median trip duration greater than members, with a weekend trip duration of
16.5 minutes compared to 10.32 minutes, and a weekday median of 13.1 minutes compared to 9.4 minutes.
Members are more active during the week than casual riders, taking 1,899,139 total trips, compared to 1,060,580 trips.


