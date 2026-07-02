from pypdf import PdfReader
import re

def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    full_text = ""
    for page in reader.pages:
        full_text += page.extract_text()
    return full_text

def split_into_chunks(text, chuck_size=800, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chuck_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    return chunks

def chunk_stat(chunks):
    lengths = [len(chunk) for chunk in chunks]
    total = len(chunks)
    average = sum(lengths) / total
    return{
        "count": total,
        "average_size": round(average),
        "min_size": min(lengths),
        "max_size": max(lengths),
    }

def clean_text(text):
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n", text)
    text = re.sub(r" *\n *", "\n", text)
    return text.strip()



if __name__ == "__main__":
    text = extract_text("data/lecture.pdf")
    text = clean_text(text)
    chunks = split_into_chunks(text)

    stats = chunk_stat(chunks)
    print("Total chunks:", stats["count"])
    print("Average size:", stats["average_size"])
    print("The biggest:", stats["max_size"])
    print("The smallest:", stats["min_size"])

    print("Fisrt chunk")
    print(chunks[0])
    print("Second chunk")
    print(chunks[1])
