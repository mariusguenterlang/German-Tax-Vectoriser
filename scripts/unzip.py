'''
the function extract_zip unzips the downloaded law data.

the data comes from the directory set in ingestion.py
'''

import zipfile
import shutil
from pathlib import Path

def extract_zip(filepath: Path, law="estg"):
    target_dir = (Path.home() / "Downloads" / "Steuergesetze" / "extracted")

    if not target_dir.exists():
        target_dir.mkdir(parents=True, exist_ok=True)

    (Path.home() / "Downloads" / "Steuergesetze" / "tmp").mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(filepath / f'{law}.zip', 'r') as zip_ref:
        zip_ref.extractall(filepath.parent / 'tmp')

    xml_file = (filepath.parent / 'tmp').glob('*.xml')

    new_file = target_dir / f"{law}.xml"

    shutil.move(str(next(xml_file)), new_file)

    shutil.rmtree(filepath.parent / 'tmp')

    

if __name__ == "__main__":
    # Example usage
    zip_path = Path.home() / "Downloads" / "Steuergesetze" / "raw"
    extracted_files = extract_zip(zip_path, law="estg")
