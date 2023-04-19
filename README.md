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
data = apis.query_project_api(include_fields=include_fields, search_criteria=search_criteria)

print(data)

[{'appl_id': 9795459, 'project_title': 'Evaluating Whether a Concurrent Retinoid X Receptor Agonist can Enhance the Efficacy of the HER2-IGFPB2-IGF1R Vaccine in Eliminating Existing Ductal Carcinoma in Situ and Preventing Progression of Inv'}]
```
