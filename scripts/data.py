import requests
import zipfile
import os
import shutil


def get_estg():
    if os.path.exists("downloads/estg.xml"):
        print("estg.xml already exists. Skipping download.")
        return f"estg.xml already exists. Skipping download."
    
    os.makedirs("downloads", exist_ok=True)

    url = "https://www.gesetze-im-internet.de/estg/xml.zip"

    response = requests.get(url)
    response.raise_for_status() # check for success

    filename = "estg_xml.zip"

    with open(filename, "wb") as file:
        file.write(response.content)

    with zipfile.ZipFile(filename, 'r') as zip_ref:
        internal_name = zip_ref.namelist()[0] # get the name of the file inside the zip
        zip_ref.extractall(".")

    os.rename(internal_name, "estg.xml")

    shutil.move("estg.xml", "downloads/estg.xml")

    os.remove(filename) # remove file


if __name__ == "__main__":
    get_estg()
