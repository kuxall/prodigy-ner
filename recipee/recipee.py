import time
from typing import List

from rich import box
from rich.table import Table
from rich.console import Console

import spacy
from prodigy.components.preprocess import add_tokens
import prodigy
from prodigy.components.loaders import JSONL


class ProgressTable:
    def __init__(self):
        self.start_time = time.time()
        self.n_examples = {
            "n_accept": 0,
            "n_reject": 0,
            "n_skip": 0,
        }
        self.console = Console()

    def make_table(self):
        """Generates a pretty Rich table from the results."""
        seconds_sofar = time.time() - self.start_time
        minutes = seconds_sofar / 60
        total_counts = sum(self.n_examples.values())
        time_mark = f"{int(seconds_sofar // 60)}m{int(seconds_sofar % 60)}s"
        table = Table(title=f"Summary at {time_mark}", box=box.SIMPLE)

        table.add_column("Answer", style="magenta", footer="Total")
        table.add_column(
            "Count", justify="right", style="cyan", footer=str(total_counts)
        )
        table.add_column(
            "Annot per Hour",
            justify="right",
            style="green",
            footer=str(int(total_counts / minutes) * 60),
        )

        for key, value in self.n_examples.items():
            table.add_row(key, str(value), str(int(value / seconds_sofar * 60 * 60)))
        table.show_footer = True
        return table

    def update(self, examples: List[dict]):
        self.n_examples["ORG"] += len([e for e in examples if e["spans"]["label"] == "ORG"])
        table = self.make_table()
        self.console.print(table)

@prodigy.recipe(
    "progress",
    dataset=("Dataset to save answers to", "positional", None, str),
)

# be sure to add in spacy_model and source
def progress(dataset: str, spacy_model: str, source: str):
    stream = JSONL(source)
    nlp = spacy.load(spacy_model)
    stream = add_tokens(nlp, stream) # this adds in tokens, which are needed for `ner`
    ptable = ProgressTable()

    return {
        "dataset": dataset,
        "view_id": "ner",
        "stream": stream,
        "update": ptable.update,
    }