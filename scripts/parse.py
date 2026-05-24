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

        paragraphs = norm.find_all("P")

        for i, p in enumerate(paragraphs, start=1):
            paragraph_text = p.get_text(strip=True)

            data.append({
                "jurabk": jurabk,
                "enbez": enbez,
                "titel": titel,
                "paragraph_number": i,
                "paragraph_text": paragraph_text
            })

    df = pd.DataFrame(data)

    return df


if __name__ == "__main__":
    extr_path = Path.home() / "Downloads" / "Steuergesetze" / "extracted" / "estg.xml"
    df = parse_xml(extr_path)
    pars_path = Path.home() / "Downloads" / "Steuergesetze" / "extracted" / "estg.csv"
    df.to_csv(pars_path, index=False)