# zabbix-auto-provisioning

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Zabbix](https://img.shields.io/badge/Zabbix-D40000?style=for-the-badge&logo=zabbix&logoColor=white)
![YAML](https://img.shields.io/badge/yaml-%23ffffff.svg?style=for-the-badge&logo=yaml&logoColor=151515)
![JSON](https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

## Overview
This tool automates the process of mass onboarding new devices (hosts, switches, cameras) into Zabbix.
Instead of manual UI configuration, it reads a YAML inventory file and communicates with Zabbix API to provision hosts with specific templates, groups, and interfaces.

## Features
- **Mass Provisioning:** Creates multiple hosts in seconds.
- **Defensive Programming:** Validates YAML inputs before execution to prevent pipeline failures.
- **Security:** API tokens and credentials are kept out of the code using Environment Variables.
- **Observability:** Built-in standard logging (info/warnings/errors).
- **Idempotency:** Detects if a host already exists and safely skips it.

## Tech Stack
- Python 3.x
- Zabbix JSON-RPC
- YAML (PyYAML)
- Requests (API communication), Argparse (CLI), Logging, OS (Env Vars)

## Usage
1. **Install dependencies:** `pip install -r requirements.txt`
2. **Prepare inventory file:** `cp hosts_example.yaml hosts-RO.yaml` (and edit it with your data).
3. **Export token:** `export ZABBIX_TOKEN="your_api_token_here"`
4. **Run the script:** `python zabbix_onboarder.py`
