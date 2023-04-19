# pynih - nih reporter api access via python

pynih is a python library that provides easy access to the NIH's set of [Reporter APIs](https://api.reporter.nih.gov/).

## Installation

`pip install pynih`

## Example usage

```
from pynih import apis

# illustration of project api usage
search_criteria = {'appl_id':'9795459'}
include_fields = ['ApplId', 'ProjectTitle']
project_data = apis.query_project_api(include_fields=include_fields, search_criteria=search_criteria)

# illustration of publication api usage
search_criteria = {'pmid':'26657764'}
publication_data = apis.query_publication_api(search_criteria=search_criteria)
```
