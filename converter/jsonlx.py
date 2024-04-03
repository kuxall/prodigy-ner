import pathlib
import srsly 
import datetime

today = datetime.datetime.now().strftime("%Y-%m-%d")
full_dataset = [] 
for path in pathlib.Path("/home/kushal/Documents/spacyprodigy/classification").glob("*.jsonl"):
    for ex in srsly.read_jsonl(path):
        full_dataset.append(ex)

srsly.write_jsonl(f"/home/kushal/Documents/spacyprodigy/classification/merged_classification/total_categorization.jsonl", full_dataset)