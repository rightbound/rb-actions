from pydriller import Repository
from pprint import pprint
import re
import os
#import sys
#from git import Repo

#owner = "rightbound"
#repo = "rb"
#path = '/home/nimrod/.rb'
#path = sys.argv[1]
#path = "https://github.com/rightbound/rb.git"

#git_repo = Repo(path)
#latest_tag = git_repo.tags[len(git_repo.tags) - 1]
#start_tag = git_repo.tags[len(git_repo.tags) - 50]

#latest_tag = "v1.0.288"
#start_tag = "v1.0.280"

path = os.environ['INPUT_PATH']
from_tag = os.environ['INPUT_FROM_TAG']
to_tag = os.environ['INPUT_TO_TAG']

search_pattern = "[rR][bB].?([0-9][0-9][0-9][0-9])"
users_and_jira_dict = {}

commits = list(Repository(path, from_tag=from_tag, to_tag=to_tag, only_in_branch='master').traverse_commits())

for commit in commits:
    jira_tickets = re.findall(search_pattern, commit.msg)
    if jira_tickets:
        jira_tickets = {f'RB-{jira_ticket}' for jira_ticket in jira_tickets}
        users_and_jira_dict[commit.author.name] = users_and_jira_dict.get(commit.author.name, set())
        users_and_jira_dict[commit.author.name].update(jira_tickets)

pprint(users_and_jira_dict)

