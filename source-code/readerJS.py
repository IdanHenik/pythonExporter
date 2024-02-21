import requests
import json
import os
import logging
from datetime import datetime, timedelta
from collections import OrderedDict

# Set up logging
logging.basicConfig(filename='error.log', level=logging.ERROR)

api_url = os.environ.get('API_URL', 'https://example.com/api/v2/')
token = os.environ.get('API_TOKEN', 'your_default_token')
headers = {'Authorization': 'Bearer ' + token}

def handle_key_error(data):
    for key, value in data.items():
        if isinstance(value, dict):
            handle_key_error(value)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, dict):
                    handle_key_error(item)
        else:
            if value is None:
                data[key] = ""
    return data

def get_data_jobs():
    try:
        api_endpoint = 'jobs'
        url = f'{api_url}' + f'/{api_endpoint}' + '/'
        payload = {}

        # makes request to controller user endpoint
        response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)

        # Parse JSON response
        json_data = response.json()

        cutoff_time = datetime.utcnow() - timedelta(hours=24)

        # Extract desired fields for each object under "results"
        desired_data = []
        for result in json_data.get('results', []):
            desired_item = {
                "name": result.get("name", ""),
                "created": result.get("created", ""),
                "modified": result.get("modified", ""),
                "launch_type": result.get("launch_type", ""),
                "status": result.get("status", ""),
                "started": result.get("started", ""),
                "finished": result.get("finished", ""),
                "canceled_on": result.get("canceled_on", ""),
                "elapsed": result.get("elapsed", ""),
                "controller_node": result.get("controller_node", ""),
                "playbook": result.get("playbook", ""),
            }

            try:
                desired_item["job_template"] = {
                    "id": result["summary_fields"]["job_template"]["id"],
                    "name": result["summary_fields"]["job_template"]["name"],
                    "description": result["summary_fields"]["job_template"]["description"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_jobs: {e}')
                desired_item["job_template"] = {
                    "id": "",
                    "name": "",
                    "description": "",
                }

            try:
                desired_item["organization"] = {
                    "id": result["summary_fields"]["organization"]["id"],
                    "name": result["summary_fields"]["organization"]["name"],
                    "description": result["summary_fields"]["organization"]["description"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_jobs: {e}')
                desired_item["organization"] = {
                    "id": "",
                    "name": "",
                    "description": "",
                }

            try:
                desired_item["inventory"] = {
                    "id": result["summary_fields"]["inventory"]["id"],
                    "name": result["summary_fields"]["inventory"]["name"],
                    "description": result["summary_fields"]["inventory"]["description"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_jobs: {e}')
                desired_item["inventory"] = {
                    "id": "",
                    "name": "",
                    "description": "",
                }

            try:
                desired_item["execution_environment"] = {
                    "id": result["summary_fields"]["execution_environment"]["id"],
                    "name": result["summary_fields"]["execution_environment"]["name"],
                    "description": result["summary_fields"]["execution_environment"]["description"],
                    "image": result["summary_fields"]["execution_environment"]["image"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_jobs: {e}')
                desired_item["execution_environment"] = {
                    "id": "",
                    "name": "",
                    "description": "",
                    "image": "",
                }

            try:
                desired_item["project"] = {
                    "id": result["summary_fields"]["project"]["id"],
                    "name": result["summary_fields"]["project"]["name"],
                    "description": result["summary_fields"]["project"]["description"],
                    "status": result["summary_fields"]["project"]["status"],
                    "scm_type": result["summary_fields"]["project"]["scm_type"],
                    "allow_override": result["summary_fields"]["project"]["allow_override"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_jobs: {e}')
                desired_item["project"] = {
                    "id": "",
                    "name": "",
                    "description": "",
                    "status": "",
                    "scm_type": "",
                    "allow_override": "",
                }

            desired_data.append(desired_item)
        print(f'This is jobs data: {desired_data}')
        return desired_data
    except Exception as e:
        logging.error(f'Error in get_data_jobs: {e}')
        return []

def get_data_teams():
    try:
        api_endpoint = 'teams'
        url = f'{api_url}' + f'/{api_endpoint}' + '/'
        payload = {}

        # makes request to controller user endpoint
        response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)

        # Ensure the request was successful
        response.raise_for_status()

        # Parse JSON response
        json_data = response.json()

        # Extract desired fields for each object under "results"
        desired_data = []
        for result in json_data.get('results', []):
            desired_item = {
                "name": result.get("name", ""),
                "id": result.get("id", ""),
                "type": result.get("type", ""),
                "url": result.get("url", ""),
                "created": result.get("created", ""),
                "modified": result.get("modified", ""),
                "description": result.get("description", ""),
            }

            try:
                desired_item["organization"] = {
                    "id": result["summary_fields"]["organization"]["id"],
                    "name": result["summary_fields"]["organization"]["name"],
                    "description": result["summary_fields"]["organization"]["description"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_teams - organization: {e}')
                desired_item["organization"] = {
                    "id": "",
                    "name": "",
                    "description": "",
                }

            try:
                desired_item["created_by"] = {
                    "id": result["summary_fields"]["created_by"]["id"],
                    "username": result["summary_fields"]["created_by"]["username"],
                    "first_name": result["summary_fields"]["created_by"]["first_name"],
                    "last_name": result["summary_fields"]["created_by"]["last_name"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_teams - created_by: {e}')
                desired_item["created_by"] = {
                    "id": "",
                    "username": "",
                    "first_name": "",
                    "last_name": "",
                }

            desired_data.append(desired_item)
        print(f'This is teams data: {desired_data}')
        return desired_data
    except Exception as e:
        logging.error(f'Error in get_data_teams: {e}')
        return []

def get_data_inventory():
    try:
        api_endpoint = 'inventories'
        url = f'{api_url}' + f'/{api_endpoint}' + '/'
        payload = {}

        # makes request to controller user endpoint
        response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)

        # Ensure the request was successful
        response.raise_for_status()

        # Parse JSON response
        json_data = response.json()

        # Extract desired fields for each object under "results"
        desired_data = []
        for result in json_data.get('results', []):
            desired_item = {
                "name": result.get("name", ""),
                "id": result.get("id", ""),
                "created": result.get("created", ""),
                "modified": result.get("modified", ""),
                "description": result.get("description", ""),
            }

            try:
                desired_item["organization"] = {
                    "id": result["summary_fields"]["organization"]["id"],
                    "name": result["summary_fields"]["organization"]["name"],
                    "description": result["summary_fields"]["organization"]["description"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_inventory - organization: {e}')
                desired_item["organization"] = {
                    "id": "",
                    "name": "",
                    "description": "",
                }

            try:
                desired_item["created_by"] = {
                    "id": result["summary_fields"]["created_by"]["id"],
                    "username": result["summary_fields"]["created_by"]["username"],
                    "first_name": result["summary_fields"]["created_by"]["first_name"],
                    "last_name": result["summary_fields"]["created_by"]["last_name"],
                }
            except KeyError as e:
                logging.error(f'KeyError occurred in get_data_inventory - created_by: {e}')
                desired_item["created_by"] = {
                    "id": "",
                    "username": "",
                    "first_name": "",
                    "last_name": "",
                }

            desired_data.append(desired_item)
        print(f'This is INV data: {desired_data}')
        return desired_data
    except Exception as e:
        logging.error(f'Error in get_data_inventory: {e}')
        return []
def total_jobs():
    try:
        api_endpoint = 'jobs'
        url = f'{api_url}' + f'/{api_endpoint}' + '/'
        payload = {}
        response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)
        # Parse JSON response
        json_data = response.json()
        # Total Jobs calculations
        successful_jobs_count = sum(1 for result in json_data.get('results', []) if result.get("status") == "successful")
        failed_jobs_count = sum(1 for result in json_data.get('results', []) if result.get("status") == "failed")
        total_jobs_num = successful_jobs_count + failed_jobs_count

        # Total Execution Time Average calculation
        elapsed_times = [result.get("elapsed", 0) for result in json_data.get('results', [])]
        total_jobs_count = len(elapsed_times)

        if total_jobs_count > 0:
            total_elapsed_time = sum(elapsed_times)
            avg_execution_time = total_elapsed_time / total_jobs_count
            print(f'Total Execution Time Average: {avg_execution_time} seconds')
        else:
            avg_execution_time = 0
            print('No jobs available.')
        return {
            "total_successful_jobs": successful_jobs_count,
            "total_failed_jobs": failed_jobs_count,
            "total_jobs_num": total_jobs_num,
            "total_execution_time_avg": avg_execution_time
        }
    except Exception as e:
        logging.error(f'Error in total_jobs: {e}')
        return {
            "total_successful_jobs": 0,
            "total_failed_jobs": 0,
            "total_jobs_num": 0,
            "total_execution_time_avg": 0
        }

if __name__ == "__main__":
    # Example usage
    jobs_data = get_data_jobs()
    teams_data = get_data_teams()
    inventory_data = get_data_inventory()
    total_jobs_data = total_jobs()
