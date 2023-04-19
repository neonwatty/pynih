import requests
import time
from requests.exceptions import RequestException
from typing import Dict, List


# retry function requests
def retry_post_request(url: str,
                       params: Dict,
                       max_retries: int = 5,
                       retry_delay: int = 10,
                       timeout: int = 45) -> List[Dict]:
    # make request with retries
    for retry_count in range(max_retries):
        try:
            # make request
            response = requests.post(url, json=params, timeout=timeout)
            # check status code - else return data
            if response.status_code >= 400 and response.status_code < 500:
                print(f"Bad request: {response.text}")
                if retry_count < max_retries - 1:
                    print(f"Retrying after {retry_delay} seconds...")
                    time.sleep(retry_delay)
                else:
                    raise Exception(f"Failed to complete POST request after {max_retries} attempts")
            else:
                data = response.json()['results']
                return data
        except RequestException as e:
            print(f"POST request failed: {e}")
            if retry_count < max_retries - 1:
                print(f"Retrying after {retry_delay} seconds...")
                time.sleep(retry_delay)
    raise Exception(f"Failed to complete POST request after {max_retries} attempts")


# function to collect data from NIH Reporter API (projects)
def query_project_api(include_fields: List[str] = None,
                      search_criteria: Dict[str, str] = {},
                      limit: int = 1,
                      offset: int = 0) -> List[Dict]:
    # Set up API request parameters
    endpoint_url = 'https://api.reporter.nih.gov/v2/projects/search'

    # package up params
    params = {
                'criteria': search_criteria,
                'limit': limit,
                'offset': offset
                }
    if include_fields is not None:
        params['include_fields'] = include_fields
    # Make API request and retrieve JSON response
    data = retry_post_request(endpoint_url, params)
    # If there are no more pages of results, break out of loop
    if data is None:
        print("No results found")
        return None
    return data


# function to collect data from NIH Reporter API (projects)
def query_publication_api(search_criteria: Dict[str, str] = {},
                          limit: int = 1,
                          offset: int = 0) -> List[Dict]:
    # Set up API request parameters
    endpoint_url = 'https://api.reporter.nih.gov/v2/publications/search'

    # package up params
    params = {
                'criteria': search_criteria,
                'limit': limit,
                'offset': offset
                }

    # Make API request and retrieve JSON response
    data = retry_post_request(endpoint_url, params)
    # If there are no more pages of results, break out of loop
    if data is None:
        print("No results found")
        return None
    return data
