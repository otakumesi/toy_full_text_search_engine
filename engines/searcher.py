from engines import text_analyzer

def search(index, query):
    results = None

    for token in text_analyzer.analyze(query):
        ids = set(index[token])
        if ids:
            if results:
                results = results & ids
            else:
                results = ids

    return results
