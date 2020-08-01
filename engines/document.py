from dataclasses import dataclass
import re, logging, gzip, xml.etree.ElementTree as ET


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

    # Don't do this in production, it's a security risk. term needs to be sanitized.
    ptn = re.compile(rf'\b{term}\b', re.IGNORECASE)
    for doc in docs:
        if doc.title and ptn.match(doc.title):
            results.append(doc)
        if doc.text and ptn.match(doc.text):
            results.append(doc)
    return results


if __name__ == '__main__':
    docs = load_documents('./data/enwiki-latest-abstract1.xml.gz')
    search(docs, 'band')
    import ipdb; ipdb.set_trace()
