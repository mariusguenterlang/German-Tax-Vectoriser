'''
function parses xml file from unzip.py into csv file
'''

from bs4 import BeautifulSoup
from pathlib import Path
import pandas as pd

def parse_xml(xmlfile):
    with open(xmlfile, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "xml")

    data = []

    for norm in soup.find_all("norm"):
        jurabk = norm.find("jurabk").text if norm.find("jurabk") else None
        enbez = norm.find("enbez").text if norm.find("enbez") else None
        titel = norm.find("titel").text if norm.find("titel") else None

        data.append({
            "jurabk": jurabk,
            "enbez": enbez,
            "titel": titel
        })

    df = pd.DataFrame(data)

    return df


if __name__ == "__main__":
    path = Path.home() / "Downloads" / "Steuergesetze" / "extracted" / "estg.xml"
    df = parse_xml(path)
    df.to_csv("estg.csv", index=False)