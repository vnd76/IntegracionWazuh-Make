#!/usr/bin/env python3

import sys
import requests
import json

"""
ossec.conf configuration structure
 <integration>
     <name>custom-make</name>
     <hook_url>https://hook.eu1.make.com/XXXXXXXXXXXX</hook_url>
     <alert_format>json</alert_format>
 </integration>
"""

# read configuration
alert_file = sys.argv[1]
user = sys.argv[2].split(":")[0]
hook_url = sys.argv[3]

# read alert file
with open(alert_file) as f:
    alert_json = json.loads(f.read())

# extract alert fields
alert_level = alert_json["rule"]["level"]
rule_id = alert_json["rule"]["id"]
description = alert_json["rule"]["description"]

# agent details
if "agentless" in alert_json:
    agent_ = "agentless"
else:
    agent_ = alert_json["agent"]["name"]

# construir payload compatible con Make
payload = {
    "rule_id": rule_id,
    "level": alert_level,
    "description": description,
    "agent": agent_,
    "full_log": alert_json  # opcional: envía todo el evento
}

# enviar a webhook de Make
response = requests.post(
    hook_url,
    json=payload,  # <- IMPORTANTE: usar json= en lugar de data=
    headers={"Content-Type": "application/json"}
)

# opcional: debug
print(f"Status: {response.status_code}")
print(response.text)

sys.exit(0)