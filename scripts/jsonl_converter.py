import argparse, glob, json, pdfplumber, re


class FileToJsonl:
    "A Wrapper class for converting files to JSONLs"

    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path
        self.file = str()

    def txt_from_file(self):
        "Extract text from a file"
        if self.file.endswith(".pdf"):
            text = str()
            with pdfplumber.open(self.file) as pdf:
                for page in pdf.pages:
                    text += page.extract_text()
            return text
        elif self.file.endswith(".txt"):
            with open(self.file, 'r') as f:
                text = f.read()
            return text
        else:
            return None

    def clean_text(self, text):
        "Remove sequential duplicates of \n"
        text = re.sub(r'[^\x00-\x7F]+',"", text)
        return text

    def save_to_jsonl(self, texts):
        "Save list of strings to a JSONL file"

        # Output file name
        json_file = (
            self.output_path
            + "/"
            + self.file.split("/")[-1].split(".")[0]
            + ".jsonl"
        )

        dicts = [{"text": text} for text in texts]

        with open(json_file, "w") as f:
            for dict_ in dicts:
                json.dump(dict_, f)
                f.write("\n")
        print(f"Successfully converted {self.file} to {json_file}")

    def __call__(self, file):
        "Convert File to JSON lines"
        self.file = file
        text = self.txt_from_file()
        if text is None:
            return
        text = self.clean_text(text)
        texts = text.split("\n")  
        self.save_to_jsonl(texts)



def main():
    files = glob.glob(args.input_path + "/*")
    for file in files:
        FileToJsonl(input_path=args.input_path, output_path=args.output_path)(file)
    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Input Folder, Output Folder")
    parser.add_argument(
        "--input_path",
        type=str,
        default="./PDF_input",
        help="Path of directory containing PDF, TEXT files.",
    )
    parser.add_argument(
        "--output_path",
        type=str,
        default="./outputs",
        help="Path of directory that stores target JSONL files.",
    )
    args = parser.parse_args()

    main()