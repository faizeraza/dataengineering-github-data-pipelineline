# Data Engineering Github Trending Repository Project

## Overview

In this updated version of project, I embarked on an exciting journey of exploring and analyzing trending repositories on GitHub.
I aimed to extract valuable insights from the repositories' data, rank them based on various criteria, and create a meaningful schema for further analysis.

## Workflow
Here's a high-level overview of the workflow I followed in this project:

1. Data Extraction: I fetched trending repositories' data from GitHub using web scraping techniques and the GitHub API.

2. Data Transformation: The extracted data was cleaned, transformed, and organized into a structured format suitable for analysis.

3. Schema Design: I designed a star schema that included dimension tables for users, repositories, time, and ranks, along with a fact table for repository information.

4. Database Creation: I set up a PostgreSQL database to store the structured data using the designed star schema.

5. Triggers and Functions: I implemented triggers and functions in PostgreSQL to handle the dynamic updates and insertions in the user dimension.

6. Ranking Algorithm: I developed a Python function to calculate rank values for repositories based on customizable weights.

7. Data Analysis: With the data in place, I conducted insightful analyses, such as identifying top repositories and understanding user behaviors.

Documentation and Sharing: I documented the entire project to capture challenges, solutions, workflow, and outcomes. This documentation serves as a valuable reference for both personal reflection and sharing with others.

## Challenges Faced and Solutions
Throughout the project, I encountered several challenges that pushed me to think creatively and problem-solve effectively:

## Data Extraction and Processing:

#### Challenge: Fetching data from GitHub and processing it efficiently for analysis.
Solution: I used Python with libraries like BeautifulSoup and the GitHub API to gather and process repository and user information.
Schema Design and Database Management:

#### Challenge: Designing a star schema to organize data effectively and managing primary and foreign keys.
Solution: I carefully designed the schema with proper relationships between dimensions and the fact table, ensuring data integrity.
Trigger and Function Implementation:

#### Challenge: Implementing triggers and functions to update user information while avoiding recursive loops.
Solution: I crafted triggers and functions in PostgreSQL to ensure smooth updates in the user dimension while maintaining control over the insertion process.
Ranking Algorithm Development:

#### Challenge: Developing an algorithm to rank repositories based on stars, forks, and contributions.
Solution: I created a Python function to calculate rank values using customizable weights and implemented the function in the PostgreSQL database.

## Tools and Technologies
1. Python pandas,psycopg2,PyGithub.
2. PostgreSQL.

## Star Schema Diagram
<code> <img src="https://github.com/faizeraza/dataengineering-github-data-pipelineline/blob/main/schema/star_schemaV1.2.png"></code>
## WorkLow Flow Diagram Over Local
<code> <img src="https://github.com/faizeraza/dataengineering-github-data-pipelineline/blob/main/GitHub Data Analytics - Page 1.png"></code>
## WorkLow Flow Diagram Over Cloud
<code> <img src="https://github.com/faizeraza/dataengineering-github-data-pipelineline/blob/main/GitHub Data Analytics.png"></code>
## important links
1. https://github.com/trending?since=daily
2. https://github.com/trending?since=weekly
3. https://github.com/trending?since=monthly
