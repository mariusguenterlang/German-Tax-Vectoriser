'''
python script to ingest tax law data from a link and store it in a local directory

the function 'ingest' makes a call to the website to download a zip file containing a law

the file is saved in the "Downloads/Steuergesetze" directory of the user's home folder

the function returns the path to the saved file for further processing
'''

import os
import requests
from pathlib import Path

def ingest (law="estg"):

    # create folder for data if it doesn't exist
    target_dir = (Path.home() / "Downloads" / "Steuergesetze" / "raw")

    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)

    # access laws from the website
    base = "https://www.gesetze-im-internet.de/"
    attachment = "/xml.zip"

    url = base + law + attachment

    response = requests.get(url)

    # save file to target directory
    filepath = target_dir / f"{law}.zip"

    with open (filepath, "wb") as file:
        file.write(response.content)

    # return the path to the saved file for further processing
    return filepath

if __name__ == "__main__":
    ingest()












