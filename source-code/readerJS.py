import requests
import json
from datetime import datetime, timedelta
from collections import OrderedDict
token = 'tDO8VWrhvpCwdtwUQtBNVefvvtBqxF'
headers = {'Authorization': 'Bearer ' + token}

def get_data_jobs(token, headers):
    api_endpoint = 'jobs'
    url = f'https://aap-aap.apps.cluster-grwtc.grwtc.sandbox60.opentlc.com/api/v2/{api_endpoint}/'
    payload = {}

    # makes request to controller user endpoint
    response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)

    # Parse JSON response
    json_data = response.json()
    
    cutoff_time = datetime.utcnow() - timedelta(hours=24)
    

    # Extract desired fields for each object under "results"
    desired_data = []
    for result in json_data.get('results', []):
        created_time = datetime.strptime(result.get("created"), "%Y-%m-%dT%H:%M:%S.%fZ")

        # Check if the job was created within the last 24 hours
        if created_time > cutoff_time:
            desired_item = {
                "name": result.get("name"),
                "created": result.get("created"),
                "modified": result.get("modified"),
                "launch_type": result.get("launch_type"),
                "status": result.get("status"),
                "started": result.get("started"),
                "finished": result.get("finished"),
                "canceled_on": result.get("canceled_on"),
                "elapsed": result.get("elapsed"),
                "controller_node": result.get("controller_node"),
                "playbook": result.get("playbook"),
                "job_template": {
                    "id": result["summary_fields"]["job_template"]["id"],
                    "name": result["summary_fields"]["job_template"]["name"],
                    "description": result["summary_fields"]["job_template"]["description"],
                },
                "organization": {
                    "id": result["summary_fields"]["organization"]["id"],
                    "name": result["summary_fields"]["organization"]["name"],
                    "description": result["summary_fields"]["organization"]["description"],
                },
                "inventory": {
                    "id": result["summary_fields"]["inventory"]["id"],
                    "name": result["summary_fields"]["inventory"]["name"],
                    "description": result["summary_fields"]["inventory"]["description"],
                },
                "execution_environment": {
                    "id": result["summary_fields"]["execution_environment"]["id"],
                    "name": result["summary_fields"]["execution_environment"]["name"],
                    "description": result["summary_fields"]["execution_environment"]["description"],
                    "image": result["summary_fields"]["execution_environment"]["image"],
                },
                "project": {
                    "id": result["summary_fields"]["project"]["id"],
                    "name": result["summary_fields"]["project"]["name"],
                    "description": result["summary_fields"]["project"]["description"],
                    "status": result["summary_fields"]["project"]["status"],
                    "scm_type": result["summary_fields"]["project"]["scm_type"],
                    "allow_override": result["summary_fields"]["project"]["allow_override"],
                },
            }
            desired_data.append(desired_item)

    ####### OLD VERSION #######
    # Print the desired data
    #print(json.dumps(desired_data, indent=4, sort_keys=True))

    # Save the data to a JSON file
    #with open(f'{api_endpoint}.json', 'w') as json_file:
    #    json.dump(desired_data, json_file, indent=4)

def get_data_teams(token, headers):
    api_endpoint = 'teams'
    url = f'https://aap-aap.apps.cluster-grwtc.grwtc.sandbox60.opentlc.com/api/v2/{api_endpoint}/'
    payload = {}

    # makes request to controller user endpoint
    response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)

    # Parse JSON response
    json_data = response.json()

    # Extract desired fields for each object under "results"
    desired_data = []
    for result in json_data.get('results', []):
        desired_item = {
            # Add the desired fields for teams
            "name": result.get("name"),
            "id": result.get("id"),
            "type": result.get("type"),
            "url": result.get("url"),
            "created": result.get("created"),
            "modified": result.get("modified"),
            "description": result.get("description"),
            "organization": {
                "id": result["summary_fields"]["organization"]["id"],
                "name": result["summary_fields"]["organization"]["name"],
                "description": result["summary_fields"]["organization"]["description"],
            },
            "created_by": {
                    "id": result["summary_fields"]["created_by"]["id"],
                    "username": result["summary_fields"]["created_by"]["username"],
                    "first_name": result["summary_fields"]["created_by"]["first_name"],
                    "last_name": result["summary_fields"]["created_by"]["last_name"],
            },  
        }
        desired_data.append(desired_item)
    ####### OLD VERSION #######
    # Print the desired data
    #print(json.dumps(desired_data, indent=4, sort_keys=True))

    # Save the data to a JSON file
    #with open(f'{api_endpoint}.json', 'w') as json_file:
    #    json.dump(desired_data, json_file, indent=4)

def get_data_inventory(token, headers):
    api_endpoint = 'inventories'
    url = f'https://aap-aap.apps.cluster-grwtc.grwtc.sandbox60.opentlc.com/api/v2/{api_endpoint}/'
    payload = {}

    # makes request to controller user endpoint
    response = requests.request('GET', url, headers=headers, data=payload, allow_redirects=False, verify=False)

    # Parse JSON response
    json_data = response.json()

    # Extract desired fields for each object under "results"
    desired_data = []
    for result in json_data.get('results', []):
        desired_item = {
            # Add the desired fields for teams
            "name": result.get("name"),
            "id": result.get("id"),
            "created": result.get("created"),
            "modified": result.get("modified"),
            "description": result.get("description"),
            ### I was HERE!!!@!@
            "organization": {
                "id": result["summary_fields"]["organization"]["id"],
                "name": result["summary_fields"]["organization"]["name"],
                "description": result["summary_fields"]["organization"]["description"],
            },
            "created_by": {
                    "id": result["summary_fields"]["created_by"]["id"],
                    "username": result["summary_fields"]["created_by"]["username"],
                    "first_name": result["summary_fields"]["created_by"]["first_name"],
                    "last_name": result["summary_fields"]["created_by"]["last_name"],
            },  
        }
        desired_data.append(desired_item)
    ####### OLD VERSION #######
    # Print the desired data
    #print(json.dumps(desired_data, indent=4, sort_keys=True))

    # Save the data to a JSON file
    #with open(f'{api_endpoint}.json', 'w') as json_file:
    #    json.dump(desired_data, json_file, indent=4)

def total_jobs(token, headers):
    api_endpoint = 'jobs'
    url = f'https://aap-aap.apps.cluster-grwtc.grwtc.sandbox60.opentlc.com/api/v2/{api_endpoint}/'
    payload = {}

    # makes request to controller user endpoint
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

    # Print and save the data
    total_jobs_data = {
        "total_successful_jobs": successful_jobs_count,
        "total_failed_jobs": failed_jobs_count,
        "total_jobs_num": total_jobs_num,
        "total_execution_time_avg": avg_execution_time
    }

    ####### OLD VERSION #######
    #print(json.dumps(total_jobs_data, indent=4, sort_keys=True))

    #with open('total_jobs.json', 'w') as json_file:
    #    json.dump(total_jobs_data, json_file, indent=4)


# Example usage for /jobs endpoint
jobs_data = get_data_jobs(token, headers)
print(json.dumps(jobs_data, indent=4, sort_keys=True))

# Example usage for /teams endpoint
teams_data = get_data_teams(token, headers)
print(json.dumps(teams_data, indent=4, sort_keys=True))

# Example usage for total_jobs endpoint
total_jobs_data = total_jobs(token, headers)
print(json.dumps(total_jobs_data, indent=4, sort_keys=True))

# Example usage for /inventories endpoint
inventory_data = get_data_inventory(token, headers)
print(json.dumps(inventory_data, indent=4, sort_keys=True))
