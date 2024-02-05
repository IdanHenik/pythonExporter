import json
import time
from prometheus_client import Gauge, start_http_server


start_http_server(8000)

def get_labels_from_job_total(json_data):
    return {}

def get_labels_from_job(json_data):
    organization = json_data.get('organization', {})
    return {
        'custom_job_name': json_data.get('name', ''),
        'custom_job_status': json_data.get('status', ''),
        'custom_job_type': json_data.get('launch_type', ''),
        'custom_job_playbook': json_data.get('playbook', ''),
        'custom_job_org': organization.get ('name','')
    }

def get_labels_from_teams(json_data):
    organization = json_data.get('organization', {})
    created_by = json_data.get('created_by',{})
    return {
        'team_name': json_data.get('name', ''),
        #'team_id': str(json_data.get('id', '')),
        'team_creation_timestamp': json_data.get('created', ''),
        'team_org': organization.get('name',''),
        'created_by': created_by.get('username','')
    }

def get_labels_from_inventory(json_data):
    organization = json_data.get('organization', {})
    created_by = json_data.get('created_by',{})
    return {
        'inv_name': json_data.get('name', ''),
        'inv_creation_timestamp': json_data.get('created', ''),
        'inv_org': organization.get('name',''),
        'created_by': created_by.get('username','')
    }

def create_prometheus_metrics(json_file_path, metrics):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)

    if json_file_path == 'total_jobs.json':
        labels = get_labels_from_job_total(data)
        metrics['total_successful_jobs_metric'].set(data['total_successful_jobs'])
        metrics['total_failed_jobs_metric'].set(data['total_failed_jobs'])
        metrics['total_jobs_num_metric'].set(data['total_jobs_num'])
        metrics['total_execution_time_avg_metric'].set(data['total_execution_time_avg'])
    elif json_file_path == 'jobs.json':
        for job in data:
            labels = get_labels_from_job(job)
            metrics['get_jobs'].labels(**labels).set(job['elapsed'])  # Example with labels
    elif json_file_path == 'teams.json':
        for team in data:
            labels = get_labels_from_teams(team)
            metrics['aap_find_teams'].labels(**labels).set(team['id'])
            # Add code to handle metrics for teams if needed
    elif json_file_path == 'inventories.json':
        for inventory in data:
            labels = get_labels_from_inventory(inventory)
            print(labels)
            metrics['aap_find_inventories'].labels(**labels).set(inventory['id'])
            # Add code to handle metrics for inventories if needed
            
if __name__ == "__main__":
    json_files = ['total_jobs.json', 'jobs.json', 'teams.json','inventories.json']

    total_successful_jobs_metric = Gauge('total_successful_jobs', 'Total number of successful jobs')
    total_failed_jobs_metric = Gauge('total_failed_jobs', 'Total number of failed jobs')
    total_jobs_num_metric = Gauge('total_jobs_num', 'Total number of jobs')
    total_execution_time_avg_metric = Gauge('total_execution_time_avg', 'Average execution time of jobs')
    #job_execution_time = Gauge('job_execution_time_seconds', 'Execution time of jobs', labelnames=['custom_job_name', 'custom_job_status', 'custom_job_type', 'custom_job_playbook', 'custom_execution_time'])
    get_jobs = Gauge('get_jobs', 'Execution time of jobs', labelnames=['custom_job_name', 'custom_job_org','custom_job_status', 'custom_job_type', 'custom_job_playbook'])
    aap_find_teams = Gauge('aap_find_teams', 'AAP Teams', labelnames=['team_name','team_creation_timestamp','team_org','created_by'])
    aap_find_inventories = Gauge('aap_find_inventories', 'AAP Inventories', labelnames=['inv_name','inv_creation_timestamp','inv_org','created_by'])

    metrics = {
        'total_successful_jobs_metric': total_successful_jobs_metric,
        'total_failed_jobs_metric': total_failed_jobs_metric,
        'total_jobs_num_metric': total_jobs_num_metric,
        'total_execution_time_avg_metric': total_execution_time_avg_metric,
       # 'job_execution_time': job_execution_time,
        'get_jobs': get_jobs,
        'aap_find_teams': aap_find_teams,
        'aap_find_inventories': aap_find_inventories
        
    }

    for json_file in json_files:
        create_prometheus_metrics(json_file, metrics)

    while True:
        time.sleep(300)
