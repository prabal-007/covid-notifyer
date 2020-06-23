from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(title, message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "F:\\vsCode-python\\covid-19_project\\icon.ico",
        timeout = 10
    )

def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    # notifyMe("prabal", "this topic is on covid-19 pendamic.")
    while True:
        covidData = getData("https://www.mohfw.gov.in//")

        soup = BeautifulSoup(covidData, 'html.parser')

        myDataStr = ""

        for tr in soup.find_all('tbody')[0].find_all('tr'):
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
        listItem = myDataStr.split("\n\n")

        states = ["Delhi", "Maharashtra", "Uttar Pradesh"]

        for item in listItem[0:34]:
            listItem1 = item.split("\n")
            if listItem1[1] in states:
                nTitle = 'Covid-19 Update'
                nInfo = f"State : {listItem1[1]}\nActive : {listItem1[2]}\nCured : {listItem1[3]} & Deaths : {listItem1[4]}\nTotal : {listItem1[5]}"
                notifyMe(nTitle,nInfo)
                time.sleep(2)
        time.sleep(720)
