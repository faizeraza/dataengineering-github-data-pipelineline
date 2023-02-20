# Data Engineering Github Trending Repository Project

## Overview

Live Trending Repository is a feature provided by GitHub that shows the most popular repositories in real-time. The trending repositories are based on various metrics such as the users, repository, number of stars, forks, and recent contributions.
This project basically scraps , manages , analyze the changes takes place in trending repository data on Github .

## Project Goals
1. Data Extraction - Built a mechanism to ingest data from different html pages using crawler and scraper. 
2.  Data Transformation - Scraped the data from html pages and transformed them to CSV file.
3.  Data Load - Moved the data to database using PostgrSQL and psycopg2.
4.  Data Analysis -  Analyzed the data based on their different aspects.

## Tools and Technologies
1. Python pandas,psycopg2,matplotlib.
2. PostgreSQL.

## Data Flow Diagram
<code> <img src="https://github.com/faizeraza/dataengineering-github-data-pipelineline/blob/main/data_flow.png"></code>

## important links
1. https://github.com/trending?since=daily
2. https://github.com/trending?since=weekly
3. https://github.com/trending?since=monthly
