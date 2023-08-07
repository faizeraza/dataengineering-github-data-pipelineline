import pandas as pd
from extracting import extracter

class Processor:
    def __init__(self,user,repo) -> None:
        self.user = user
        self.repo = repo
        self.rank_value = []

    def get_user_table(self):
        return self.user
    
    def calculate_rank(self,stars, forks, contributions):
        stars_weight = 0.4
        forks_weight = 0.3
        contributions_weight = 0.3

        rank_score = (stars * stars_weight) + (forks * forks_weight) + (contributions * contributions_weight)
        return rank_score
    

    def get_time_table(self):
        timedf = {}
        timedf["timestamp"] = self.repo["time_id"]
        timedf["dow"] = self.repo["time_id"].dt.strftime("%a")
        timedf["month"] = self.repo['time_id'].dt.strftime("%B")
        timedf["year"] = self.repo["time_id"].dt.strftime("%Y")
        return pd.DataFrame(timedf)
    
    def get_repository_table(self):
        repository = self.repo[["repo_name","language_id","topics","description"]]
        return repository

    def get_fact_table(self):
        fact = self.repo[["stars","forks","contributions"]]
        return fact
    
    def get_rank_table(self):
        rank = self.repo[["interval"]]
        for index,row in self.repo.iterrows():
            curr_rank = self.calculate_rank(row["stars"],row["forks"],row["contributions"])
            self.rank_value.append(curr_rank)
        rank["rank_value"] = self.rank_value
        return rank
    
    