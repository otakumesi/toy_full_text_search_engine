import logging
from engines import text_analyzer

def add_index(index, docs):
    logging.info('Start to index...')
    for doc in docs:
        if not doc.text:
            continue
        for token in text_analyzer.analyze(doc.text):
            ids = index[token]
            if ids and ids[-1] == doc.text_id:
                continue
            index[token].append(doc.text_id)
