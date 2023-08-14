from github import Github
from github import Auth
import re
auth = Auth.Token("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")
g = Github(auth=auth)
ls=[]
repo = g.get_repo("Stability-AI/generative-models")
ls.append(repo.description)
print(ls[0])
# Get the list of contributors using the PaginatedList


# Iterate through the PaginatedList to access contributors
# interval = re.search(r'=\s*(.*)$',"https://github.com/trending?since=daily")
# print(interval.group(1))