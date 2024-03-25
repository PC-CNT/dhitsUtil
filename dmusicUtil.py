import json
import re
import sys

import requests
from bs4 import BeautifulSoup

# TODO: dミュージックからアルバム画像を持ってきてURLごとにフォルダー分別する
# アルバム画像のサイズは640x640 https://img.lap.recochoku.jp/p1/imgkp?p=%2F12%2F5682%2F96098135.jpg&f=776E62&FFh=640&FFw=640&h=77451


def parseurl(url: str):
    if(re.match(r"https?:\/\/dhits\.docomo\.ne\.jp\/music\/[0-9]+", url)):
        downloadasong(url)
    elif(re.match(r"https?:\/\/dhits\.docomo\.ne\.jp\/program\/[0-9]+", url)):
        # TODO: bs4で全曲取得->forでダウソ
        return


def downloadasong(url: str):
    song_id = re.findall(r"https?:\/\/dhits\.docomo\.ne\.jp\/music\/([0-9]+)", url)[0]
    song_name = "a"
    m4a_url = f"https://recohls-mmd-cust.lldns.net/e1/bcapi/getMusicfile/service/dhitspc/id/{song_id}/quality/320/filename/{song_name}.mp4"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    print(soup.prettify())
    return

def parselyrics(id: str):
    lrcdata = ""
    url = "https://dhits.docomo.ne.jp/music/" + id
    BeautifulSoup(requests.get(url).text, "html.parser")
    
    return lrcdata


def parsemetadata(id: str):
    return


if __name__ == "__main__":
    if len(sys.argv) == 2:
        parseurl(sys.argv[1])
    else:
        parseurl(input("曲のURLを入力 > "))
