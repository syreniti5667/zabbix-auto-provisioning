#!/usr/bin/env python3
"""
Zabbix Mass Host Onboarding via JSON-RPC API
Author: Kacper Jaworski
"""
import os
import sys
import yaml
import urllib3
import logging
import argparse
import requests

# Suppress insecure request warnings for internal self-signed certs
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configure standard logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration via Environment Variables
ZABBIX_URL = os.getenv("ZABBIX_URL", "https://zabbix.example.com/api_jsonrpc.php")
ZABBIX_TOKEN = os.getenv("ZABBIX_TOKEN")

GROUP_ID = "10"
TEMPLATE_ID = "10101"

def zabbix_api_call(method, params, token=None):
    payload = {
        "jsonrpc": "2.0",
        "method": method,
        "params": params,
        "id": 1
    }
    if token:
        payload["auth"] = token
    
    try:
        response = requests.post(ZABBIX_URL, json=payload, verify=False, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"API Connection failed: {e}")
        sys.exit(1)
    
def main():
    parser = argparse.ArgumentParser(description="Zabbix Auto-Provisioning Script")
    parser.add_argument("-f", "--file", default="hosts-RO.yaml", help="Path to YAML configuration file")
    args = parser.parse_args()
    
    if not ZABBIX_TOKEN:
        logger.error("ZABBIX_TOKEN environment variable is not set!")
        sys.exit(1)
        
    logger.info("Starting Host Import Process")
    
    try:
        with open(args.file, "r") as f:
            hosts = yaml.safe_load(f)
    except FileNotFoundError:
        logger.error(f"Configuration file '{args.file}' not found!")
        sys.exit(1)
        
    logger.info(f"Found {len(hosts)} hosts to process in {args.file}")

    for host in hosts:
    
        if not all(k in host for k in ("name", "ip", "port")):
            logger.error("Missing required fields (name/ip/port) in YAML. Skipping host.")
            continue
            
        logger.info(f"Processing: {host['name']} ({host['ip']})...")

        create_params = {
            "host": host['name'],
            "interfaces": [
                {
                    "type": 1,
                    "main": 1,
                    "useip": 1,
                    "ip": host['ip'],
                    "dns": "",
                    "port": str(host['port'])
                }
            ],
            "groups": [
                {"groupid": GROUP_ID}
            ],
            "templates": [
                {"templateid": TEMPLATE_ID}
            ]
        }

        result = zabbix_api_call("host.create", create_params, ZABBIX_TOKEN)

        if 'result' in result:
            logger.info(f"Success: Host created (HostID: {result['result']['hostids'][0]})")
        elif 'error' in result:
            err_msg = result['error']['data']
            if "already exists" in err_msg:
                logger.warning(f"Skipped: Host {host['name']} already exists.")
            else:
                logger.error(f"Failed to create {host['name']}: {err_msg}")
                
    logger.info("Import Process Completed")
  
if __name__ == "__main__":
    main()
