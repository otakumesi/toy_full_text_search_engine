from collections import defaultdict
from engines import document, indexer, searcher


if __name__ == '__main__':
    docs = document.load_documents('./data/enwiki-latest-abstract1.xml.gz')
    index = defaultdict(list)
    indexer.add_index(index, docs)

    query = 'band'
    matched_ids = searcher.search(index, query)

    for doc_id in matched_ids:
        doc = docs[doc_id - 1]
        print(f'{doc_id}\t{doc.text}')

    import ipdb; ipdb.set_trace()
