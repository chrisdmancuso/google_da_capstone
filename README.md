# Google Data Analytics Capstone Project

### Key Information

For this scenario, we have been provided information about the team/shareholders of the fictional company Cyclistic.

**Cyclistic:** A bike-share program that features more than 5,800 bicycles and 600 docking stations. Cyclistic sets itself
apart by also offering reclining bikes, hand tricycles, and cargo bikes, making bike-share more inclusive to people with
disabilities and riders who can’t use a standard two-wheeled bike. The majority of riders opt for traditional bikes; about
8% of riders use the assistive options. Cyclistic users are more likely to ride for leisure, but about 30% use them to
commute to work each day.

**Lily Moreno:** The director of marketing and your manager. Moreno is responsible for the development of campaigns
and initiatives to promote the bike-share program. These may include email, social media, and other channels.

**Cyclistic marketing analytics team:** A team of data analysts who are responsible for collecting, analyzing, and
reporting data that helps guide Cyclistic marketing strategy.

**Cyclistic executive team:** The notoriously detail-oriented executive team will decide whether to approve the
recommended marketing program.

**Data:** The data used for this scenario has been sourced by [Motivate International Inc.](https://motivateco.com/) under this [license](https://ride.divvybikes.com/data-license-agreement). The data used in this scenario can be accessed [here](https://divvy-tripdata.s3.amazonaws.com/index.html).
We will be using the yearly data from 2022, starting with 202201-divvy-tripdata.zip and ending with 202212-divvy-tripdata.zip.

## Scenario

You are a junior data analyst working in the marketing analyst team at Cyclistic, a bike-share company in Chicago. The director
of marketing believes the company’s future success depends on maximizing the number of annual memberships. Therefore,
your team wants to understand how casual riders and annual members use Cyclistic bikes differently. From these insights,
your team will design a new marketing strategy to convert casual riders into annual members. But first, Cyclistic executives
must approve your recommendations, so they must be backed up with compelling data insights and professional data
visualizations.

You have been assigned to the team responsible for answering the following question:

#### How do annual members and casual riders use Cyclistic bikes differently?

To answer this question, we'll follow the 6 step process to produce deliverables for our shareholders

1) Ask
2) Prepare
3) Process
4) Analyze
5) Share
6) Act

## Ask

Consider the problem to solve and key stakeholders in the project, and identify the business task to accomplish.

**Business task:** Analyze bike-share data, collected by Cyclistic during 2022, to discover insights to help lead the marketing push to convert casual riders to annual members.

## Prepare

Gather and properly store data to analyze, and identify how it's organized.

**Data source:** Data was collected internally and stored as 12 separate CSV files, which were compressed to zip and hosted by AWS. Data was downloaded locally from AWS and extracted into a single folder with the following naming convention: "Original_Company_mm-dd-yy". CSV files were then standardized as: "yyyymm-divvy-tripdata". Data was then copied into a separate folder with the following naming convention "Copy_Company_mm-dd-yy" and was assigned as the working directory for the project.

