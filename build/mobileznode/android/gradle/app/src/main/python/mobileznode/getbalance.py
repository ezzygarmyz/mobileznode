import requests
import json
import os


def get_address_balance(config_path, selected_address):
    if os.path.exists(config_path):
        with open(config_path, "r") as config_file:
            config = json.load(config_file)
            rpc_user = config.get("rpcuser")
            rpc_password = config.get("rpcpassword")
            rpc_host = config.get("rpchost")
            rpc_port = config.get("rpcport")
            url = f"http://{rpc_host}:{rpc_port}"

            headers = {"content-type": "text/plain"}
            payload = {
                "jsonrpc": "1.0",
                "id": "curltest",
                "method": "z_getbalance",
                "params": [f"{selected_address}"],
            }
            response = requests.post(
                url,
                data=json.dumps(payload),
                headers=headers,
                auth=(rpc_user, rpc_password),
            )

            if response.status_code == 200:
                data = response.json()
                balance_t = float(data["result"])
                
                return balance_t
