from dataclasses import dataclass
import gzip, xml.etree.ElementTree as ET


@dataclass
class Document:
    title: str
    url: str
    text: str
    text_id int


def load_documents(path):
    with gzip.open(path) as f:
        raw_docs = f.read()

    root = ET.fromstring(raw_docs)
    docs = []

    pages = root.find('./doc')
    for i, page in enumerate(pages, 1):
        doc = Document(title=page['title'], url=page['url'], text=page['abstract'], text_id=i)
        docs.append(doc)
    return docs

def search(docs, term):
    results = []
    for doc in docs:
        if term in doc:
            results.append(doc)
    return results


if __name__ = '__main__':
    import ipdb; ipdb.set_trace()
