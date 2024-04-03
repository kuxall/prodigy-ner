import os
import docx
import json

def extract_text(doc_file):
    doc = docx.Document(doc_file)
    return [para.text for para in doc.paragraphs]

def to_jsonl(texts):
    return '\n'.join([json.dumps({'text': text}) for text in texts])

def docx_to_jsonl(doc_file):
    texts = extract_text(doc_file)
    return to_jsonl(texts)

if __name__ == '__main__':
    docx_directory = r'/home/kushal/Dropbox/dolphindrive/Dataset/resumes/Batch #1 - 250/'
    jsonl_directory = r"/home/kushal/Dropbox/dolphindrive/Dataset/resumes/Batch#1Jsonl-250/"
    
    # Loop through all the .docx files in the directory
    for filename in os.listdir(docx_directory):
        if filename.endswith('.docx'):
            doc_file = os.path.join(docx_directory, filename)
            jsonl = docx_to_jsonl(doc_file)
            output_file = os.path.join(jsonl_directory, os.path.splitext(filename)[0] + '.jsonl')
            with open(output_file, 'w') as f:
                f.write(jsonl)
