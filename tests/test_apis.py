from pynih.apis import query_project_api, query_publication_api

# test datapoints
project_test_datapoint = [{'appl_id': 9795459, 'project_title': 'Evaluating Whether a Concurrent Retinoid X Receptor Agonist can Enhance the Efficacy of the HER2-IGFPB2-IGF1R Vaccine in Eliminating Existing Ductal Carcinoma in Situ and Preventing Progression of Inv'}]
publication_test_datapoint = [{'coreproject': 'ZIKDE000726', 'pmid': 26657764, 'applid': 10491636}]


# test query_project_api
def test_query_project_api():
    search_criteria = {'appl_id':'9795459'}
    include_fields = ['ApplId', 'ProjectTitle', 'ProjectStart', 'Project']
    project_datapoint = query_project_api(include_fields=include_fields, search_criteria=search_criteria)
    assert project_datapoint == project_test_datapoint


# test query_publication_api
def test_query_publication_api():
    search_criteria = {'pmid':'26657764'}
    publication_datapoint = query_publication_api(search_criteria=search_criteria)
    assert publication_datapoint == publication_test_datapoint