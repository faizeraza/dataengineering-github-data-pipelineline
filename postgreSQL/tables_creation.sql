-- Create Dimension Tables

-- repository_dimension
CREATE TABLE repository_dimension (
    repository_id SERIAL PRIMARY KEY,
    repo_name VARCHAR(100) NOT NULL,
    repo_language VARCHAR(50),
    topics TEXT[],
    description TEXT
);

-- user_dimension
CREATE TABLE user_dimension (
    user_id SERIAL PRIMARY KEY,
    user_name VARCHAR(100) NOT NULL,
    followers INTEGER,
    user_location VARCHAR(100),
    total_repos INTEGER,
    total_gists INTEGER,
    email VARCHAR(100),
    join_date DATE
);

-- rank_dimension
CREATE TABLE rank_dimension (
    rank_id SERIAL PRIMARY KEY,
    rank_category VARCHAR(20),
    rank_value INTEGER
);

-- Create Time Dimension (Optional, if needed)

-- time_dimension
CREATE TABLE time_dimension (
    time_id SERIAL PRIMARY KEY,
    time_stamp TIMESTAMP
);

-- Create Fact Table

-- trending_repositories_fact
CREATE TABLE trending_repositories_fact (
    fact_id SERIAL PRIMARY KEY,
    repository_id INTEGER REFERENCES repository_dimension(repository_id),
    user_id INTEGER REFERENCES user_dimension(user_id),
    stars INTEGER,
    forks INTEGER,
    contributions INTEGER,
    rank_id INTEGER REFERENCES rank_dimension(rank_id),
    time_id INTEGER REFERENCES time_dimension(time_id)
);
