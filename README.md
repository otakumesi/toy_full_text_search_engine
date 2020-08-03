# About This Repository
This repository is ported from a project of the url below.  
https://artem.krylysov.com/blog/2020/07/28/lets-build-a-full-text-search-engine/

# Installation
```sh
# please, clone this repository
cd {THIS_REPOSITORY_FOLDER}
poetry install
```

# Usage
```sh
poetry run python main.py

# outputs sample results

ipdb> searcher.search(index, '{YOUR_SEARCH_TERMS}')
```
