import csv
from pathlib import Path
from .observations import get_observations

def to_csv(filename="journal_export.csv"):
    observations = get_observations()
    
    base_dir = Path(__file__).resolve().parent.parent
    file_path = base_dir / filename

    with open(file_path, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "researcher", "mineral", "note"])
        
        for entry in observations:
            writer.writerow([
                entry["date"],
                entry["researcher"],
                entry["mineral"],
                entry["note"]
            ])
            
    return f"Журнал експортовано у файл '{filename}'"