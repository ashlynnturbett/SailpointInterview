# Coding Challenge
This project contains the script to find the count of how many open, closed, and in draft pull requests there are in a given repo in the last week.

## Prerequisites
You will need a GitHub token to be authorized to pull data from the repo.

## Summary of functions
### get_prs()
This function takes in the token and the path to the repository and returns the 30 most recent pull requests using the GitHub API.

### send_email()
This function takes in the pull requests found in get_prs() and parses them to determine if they were created within the last week and determines how many closed, open, and in draft prs there are. It then creates and sends an email with this information.