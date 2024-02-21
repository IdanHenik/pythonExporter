
# Ansible Automation Platform Python Exporter

This repository contains a Python exporter for the Ansible Automation Platform. The exporter is designed to retrieve data from the Ansible Automation Platform API, parse it, and generate metrics for the Platform as a Service (PaaS) team's usage.

## Contents

- [Ansible Automation Platform Python Exporter](#ansible-automation-platform-python-exporter)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Architecture](#architecture)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Functions:](#functions)
    - [`get_labels_from_job_total(json_data)`](#get_labels_from_job_totaljson_data)
    - [`get_labels_from_job(json_data)`](#get_labels_from_jobjson_data)
    - [`get_labels_from_teams(json_data)`](#get_labels_from_teamsjson_data)
    - [`get_labels_from_inventory(json_data)`](#get_labels_from_inventoryjson_data)
    - [`create_prometheus_metrics(data, metrics)`](#create_prometheus_metricsdata-metrics)
  - [Adding New Metric:](#adding-new-metric)
  - [Example of Adding a New Metric:](#example-of-adding-a-new-metric)

## Introduction

The Ansible Automation Platform Python Exporter consists of two Python code files:

1. **readerJS**: This file is responsible for making requests to the Ansible Automation Platform API, retrieving the necessary data, and parsing it.
2. **HUBexporter**: This file utilizes the parsed data obtained from `readerJS` to generate metrics tailored for the usage of the Platform as a Service team.

## Architecture

![architecture](/img/pythonExporter-diagrm.png)

## Installation

To install and use the Ansible Automation Platform Python Exporter, follow these steps:

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/ihenik/pythonExporter.git
    ```

2. Navigate to the cloned directory:

    ```bash
    cd pythonExporter/source-code
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

Before using the exporter, make sure you have the necessary credentials and permissions to access the Ansible Automation Platform API.

1. Open the `readerJS.py` file and configure the API endpoint, authentication credentials, and any other necessary parameters.
2. Run the `readerJS.py` file to retrieve and parse the data from the Ansible Automation Platform API.
3. Open the `HUBexporter.py` file and customize the metrics generation according to the requirements of 

```bash
    python3 HUBexporter.py

    curl localhost:8000
    ```
```
![screenshot](/img/screenshot.png)


## Functions:

### `get_labels_from_job_total(json_data)`
- **Purpose**: Generates labels for total job metrics.
- **Parameters**: `json_data` - JSON data representing total job metrics.
- **Returns**: Dictionary containing labels for total job metrics.

### `get_labels_from_job(json_data)`
- **Purpose**: Generates labels for individual job metrics.
- **Parameters**: `json_data` - JSON data representing an individual job.
- **Returns**: Dictionary containing labels for individual job metrics.

### `get_labels_from_teams(json_data)`
- **Purpose**: Generates labels for team metrics.
- **Parameters**: `json_data` - JSON data representing a team.
- **Returns**: Dictionary containing labels for team metrics.

### `get_labels_from_inventory(json_data)`
- **Purpose**: Generates labels for inventory metrics.
- **Parameters**: `json_data` - JSON data representing an inventory.
- **Returns**: Dictionary containing labels for inventory metrics.

### `create_prometheus_metrics(data, metrics)`
- **Purpose**: Creates Prometheus metrics based on the provided data.
- **Parameters**:
  - `data`: Dictionary containing data retrieved from various sources.
  - `metrics`: Dictionary containing initialized Prometheus gauge objects.
- **Returns**: None
- **Process**: Iterates through the provided data, extracting relevant information and setting gauge values for each metric using appropriate labels.

## Adding New Metric:
To add a new metric, follow these steps:

1. **Define a Gauge**: Initialize a new Prometheus gauge object with appropriate labels in the script's main section.
2. **Create Labels Function**: Define a function to generate labels for the new metric based on the data structure it represents.
3. **Modify Metric Creation**: Update the `create_prometheus_metrics` function to include logic for the new metric. Extract necessary data from the `data` dictionary and set gauge values using the new labels function.
4. **Add Metric to Loop**: Ensure the new metric is added to the `metrics` dictionary in the main section.
5. **Run the Script**: Run the `HUBexporter.py` script to start collecting and exposing the new metric.

## Example of Adding a New Metric:
Let's say we want to add a metric for tracking the average execution time of teams. Here's how we would do it:

1. **Define a Gauge**:
   ```python
   team_execution_time = Gauge('team_execution_time', 'Average execution time of teams', labelnames=['team_name', 'team_org'])
    ```

2. **Create a Label Function**:
 ```python
 def get_labels_from_team_execution_time(json_data):
    return {
        'team_name': json_data.get('name', ''),
        'team_org': json_data.get('organization', {}).get('name', '')
    }
```

3. **Modify Metric Creation**:
   ```python
   if 'teams_data' in subdata:
    for team in data['teams_data']:
        labels = get_labels_from_teams(team)
        print (f'Labels generated for teams {labels}')
        metrics['aap_find_teams'].labels(**labels).set(team['id'])
        
        # New metric for team execution time
        team_execution_time.labels(**labels).set(team['execution_time'])
    ```
4. **Add Metrics to Loop**:
   ```python
   metrics = {
    'get_jobs': get_jobs,
    'aap_find_teams': aap_find_teams,
    'aap_find_inventories': aap_find_inventories,
    'team_execution_time': team_execution_time  # Add the new metric here
    }
    ```



