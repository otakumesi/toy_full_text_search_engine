import logging
from dataclasses import dataclass
import gzip, xml.etree.ElementTree as ET


@dataclass
class Document:
    title: str
    url: str
    text: str
    text_id: int


def load_documents(path):
    logging.info('Start to load documents')
    with gzip.open(path) as f:
        raw_docs = f.read()

    logging.info('Start to transform raw_documents to xml_formatted')
    root = ET.fromstring(raw_docs)
    docs = []

    logging.info('Start to transform xml to dataclasses')
    pages = root.findall('doc')
    for i, page in enumerate(pages, 1):
        doc = Document(title=page.find('title').text, url=page.find('url').text, text=page.find('abstract').text, text_id=i)
        docs.append(doc)
    return docs

def search(docs, term):
    results = []
    for doc in docs:
        if term in doc.title or term in doc.text:
            results.append(doc)
    return results


if __name__ == '__main__':
    docs = load_documents('./data/enwiki-latest-abstract1.xml.gz')
    import ipdb; ipdb.set_trace()
