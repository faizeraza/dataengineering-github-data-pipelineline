from bs4 import BeautifulSoup
import requests
from github import Github
from github import Auth
import datetime
import re

class Extracter:
    def __init__(self,url) -> None:
        pass
        self.url =url
        self.auth = Auth.Token("you api token")
        self.g = Github(auth=self.auth)
        self.repodf = {}
        self.userdf = {}

    def get_trending_repositories(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            repos = soup.find_all('article', class_='Box-row')
            repo_list = [a['href'][1:] for a in soup.select('article.Box-row h2.h3 a[href]')]
            return repo_list
        else:
            print('Failed to fetch trending repositories.')  

    def get_repo_information(self):
        repos = self.get_trending_repositories()
        stars=[]
        forks=[]
        contributions = []
        language_id = []
        topics = []
        descriptions = []
        self.repodf["repoid"] = repos
        intervalstr = re.search(r'=\s*(.*)$',self.url).group(1)
        for repoid in repos:
            repo = self.g.get_repo(repoid)
            stars.append(repo.stargazers_count)
            forks.append(repo.forks_count)
            contributions.append(len([contributor.login for contributor in repo.get_contributors()]))
            language_id.append(repo.language)
            topics.append(repo.get_topics())
            descriptions.append(repo.description if repo.description else "None")
        self.repodf["repo_name"] = [repo.split("/")[1] for repo in repos]
        self.repodf["user_id"] = [x.split("/")[0] for x in repos]
        self.repodf["time_id"] = [datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") for i in range(len(repos))]
        self.repodf["stars"] = stars
        self.repodf["forks"] = forks
        self.repodf["contributions"] = contributions
        self.repodf["language_id"] = language_id
        self.repodf["topics"] = topics
        self.repodf["description"] = descriptions
        self.repodf["interval"] = [intervalstr for i in range(len(repos))]
        return self.repodf
    
    def get_user_information(self):
        repos = self.get_trending_repositories()
        self.userdf["user_id"] = self.repodf["user_id"]
        followers=[]
        location=[]
        total_repos = []
        total_gists = []
        email = []
        join_date = []
            
        for repoid in repos:
            user = self.g.get_user(repoid.split('/')[0])
            followers.append(user.followers)
            location.append(user.location)
            total_repos.append(user.public_repos)
            total_gists.append(user.public_gists)
            email.append(user.email)
            join_date.append(user.created_at)

        self.userdf["followers"] = followers
        self.userdf["location"] = location
        self.userdf["total_repos"] = total_repos
        self.userdf["total_gists"] = total_gists
        self.userdf["email"] = email
        self.userdf["join_date"] = join_date
        return self.userdf
            

# if __name__=="__main__":
#     extracter = Extracter("https://github.com/trending?since=daily")
#     repos = extracter.get_trending_repositories()
#     dfrepo = extracter.get_repo_information(repos)
#     # dfuser = extracter.get_user_information(repos)
#     print(dfrepo)
#     # print("user:/n")
#     # print(dfuser)
