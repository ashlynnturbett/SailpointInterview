import os

import requests
import smtplib
from email.message import EmailMessage
from datetime import date, timedelta


def get_prs():
    token = input("Please enter your token: ")
    headers = {'Authorization': 'token ' + token}

    path = input("Please enter repo name: ")
    url = "https://api.github.com/repos/" + path + "/pulls"
    allInfo = requests.get(url, params={'state': 'all'}, headers=headers)
    allInfo = allInfo.json()

    return allInfo


def send_email(allInfo):
    EMAIL_ADDRESS = "sailpointinterview@gmail.com"
    EMAIL_PASSWORD = "Sailpoint8*"

    contacts = ["ashlynnturbett@gmail.com"]

    start = date.today() - timedelta(7)
    count, draft, closed = 0, 0, 0

    msg = EmailMessage()

    msg['Subject'] = 'Github statistics'
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = contacts

    for x in allInfo:
        if x["created_at"][:10] >= start.strftime("%Y-%m-%d"):
            if x["state"] == "closed":
                closed += 1
            elif not x["draft"]:
                count += 1
            else:
                draft += 1
        else:
            break

    msg.set_content('There are ' + str(count) + " open requests, " + str(closed) + " closed requests, and " + str(
        draft) + " requests in draft in the last week.")

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)


if __name__ == '__main__':
    allInfo = get_prs()
    send_email(allInfo)
