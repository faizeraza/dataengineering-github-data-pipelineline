import ast
import psycopg2
import pandas as pd
from sympy import total_degree

class Loader:

    def __init__(self) -> None:
        self.conn = psycopg2.connect(
        host='localhost',
        database='gdadatawarehouse',
        user='postgres',
        password="yourpassword"
        )
        self.cur = self.conn.cursor()

    def load_user(self,userdf):
        for index, row in userdf.iterrows():
            self.cur.execute("""
                INSERT INTO user_dimension (user_name, followers, user_location, total_repos, total_gists, email, join_date)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (row['user_id'], row['followers'], row['location'], row["total_repos"], row["total_gists"], row["email"], row["join_date"]))

    def load_repository(self,reposdf):
        for index, row in reposdf.iterrows():
            if type(row["topics"]) == str:
                topics_str = "{" + ",".join(ast.literal_eval(row["topics"])) + "}"
            else:
                topics_str = "{" + ",".join(row["topics"]) + "}"
            self.cur.execute("""
                INSERT INTO repository_dimension (repo_name, repo_language, topics, description)
                VALUES (%s, %s, %s, %s)
            """, (row['repo_name'], row['language_id'], topics_str, row['description']))
            
    def load_time(self,timedf):
        for index, row in timedf.iterrows():
            #  print(f"row{index}")
             self.cur.execute("""
                INSERT INTO time_dimension ( time_stamp, day_of_week, month, year)
                VALUES (%s, %s, %s, %s)
            """, (row['timestamp'], row['dow'], row['month'], row['year']))
    
    def load_rank(self,rankdf):
        for index, row in rankdf.iterrows():
            self.cur.execute("""
                INSERT INTO rank_dimension ( rank_category, rank_value)
                VALUES (%s,%s)
            """, (row['interval'], row['rank_value']))
                        
    def load_fact(self,repodf,userdf):        
        rawdf = pd.merge(repodf,userdf,how="inner",on="user_id")
        rawdf = rawdf.drop_duplicates(subset=['repoid'], keep='first')
        rawdf = rawdf.reset_index(drop=True)
        # print(rawdf.shape)
        for index, row in rawdf.iterrows():
            # Find the corresponding repository_id and user_id based on the repo_name and user_name
            indx = 24-index

            self.cur.execute("""
                SELECT repository_id FROM repository_dimension ORDER BY repository_id DESC LIMIT 1 OFFSET %s
            """, (indx,))
            repository_id = self.cur.fetchone()[0]
            # print(repository_id)

            self.cur.execute("""
                SELECT user_id FROM user_dimension where user_name = %s
            """, (row['user_id'],))
            user_id = self.cur.fetchone()[0]
            # print(user_id)

            self.cur.execute("""
                SELECT time_id FROM time_dimension ORDER BY time_id DESC LIMIT 1 OFFSET %s
            """, (indx,))
            time_id = self.cur.fetchone()[0]

            

            self.cur.execute("""
                SELECT rank_id FROM rank_dimension ORDER BY rank_id DESC LIMIT 1 OFFSET %s
            """, (indx,))
            rank_id = self.cur.fetchone()[0]

            # Insert data into the fact table using the foreign keys

            self.cur.execute("""
                INSERT INTO trending_repositories_fact 
                (fact_id,repository_id, user_id, stars, forks, contributions, time_id, rank_id)
                VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s)
            """, (repository_id, user_id, row['stars'], row['forks'], row['contributions'], time_id, rank_id))

            
    def commit_data(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    
