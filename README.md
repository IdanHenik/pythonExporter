
# Ansible Automation Platform Python Exporter

This repository contains a Python exporter for the Ansible Automation Platform. The exporter is designed to retrieve data from the Ansible Automation Platform API, parse it, and generate metrics for the Platform as a Service (PaaS) team's usage.

## Contents

- [Ansible Automation Platform Python Exporter](#ansible-automation-platform-python-exporter)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Architecture](#architecture)
  - [Installation](#installation)
  - [Usage](#usage)

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