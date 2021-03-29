#!/usr/bin/python3
# Sequester forked repos into separate org.
# Bart Massey 2021

import pathlib, re, sys

target = sys.argv[1]
assert target

home = pathlib.Path.home()
with open(home / ".githubuser", "r") as f:
    user = f.read().strip()
with open(home / ".github-oauthtoken", "r") as f:
    token = f.read().strip()

user_re = re.compile(f"https://github.com/{user}/")

import github

# https://github.com/PyGithub/PyGithub/pull/1749
def transfer(
    self, new_owner, teams=github.GithubObject.NotSet
):
    """
    :calls: POST /repos/:owner/:repo/transfer
    :param new_owner: string
    :param teams: list of team member ids
    """
    assert isinstance(new_owner, str), new_owner
    assert teams is github.GithubObject.NotSet or isInstance(
        teams, list
    ), teams
    post_parameters = {"new_owner": new_owner}
    if teams is not github.GithubObject.NotSet:
        post_parameters["team_ids"] = teams
    headers, data = self._requester.requestJsonAndCheck(
        "POST", self.url + "/transfer", input=post_parameters
    )

github.Repository.Repository.transfer = transfer

g = github.Github(token)
for repo in g.get_user().get_repos():
    if not repo.fork:
        continue
    if repo.organization is not None:
        continue
    if not user_re.match(repo.html_url):
        continue
    print(repo.name, repo.html_url)
    repo.transfer(target)
