from dataclasses import dataclass
import logging, gzip, xml.etree.ElementTree as ET


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
        title = page.find('title').text
        url = page.find('url').text
        text = page.find('abstract').text
        doc = Document(title=title, url=url, text=text, text_id=i)
        docs.append(doc)
    return docs
