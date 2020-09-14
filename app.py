from flask import Flask, render_template, redirect, url_for, request, json
import requests

app = Flask(__name__)

NETPALM_SERVER_IP = "10.0.2.15"
NETPALM_SERVER_PORT = 9000
NETPALM_API_KEY = "2a84465a-cf38-46b2-9d86-b84Q7d57f288"

@app.route("/")
def hello_world_form_index():
    return render_template("hello-world-template.html")


@app.route("/result/<posted_data>")
def hello_world_result(posted_data):
    task_id = json.loads(posted_data)["data"]["task_id"]
    r = requests.get(f"http://{NETPALM_SERVER_IP}:{NETPALM_SERVER_PORT}/task/{task_id}",
                        headers={"Content-type": "application/json", "x-api-key": NETPALM_API_KEY}, timeout=10)    
    return render_template("result.html", posted_data=r.json())


@app.route("/execute_job", methods=["POST"])
def hello_world_execute():
    post_data = {
        "library": "netmiko",
        "connection_args": {
            "device_type": "cisco_ios",
            "host": request.form["ipaddr"],
            "username": request.form["username"],
            "password": request.form["pwd"],
            "timeout": 5
        },
        "command": request.form["command"],
        "queue_strategy": "pinned"
    }
    r = requests.post(f"http://{NETPALM_SERVER_IP}:{NETPALM_SERVER_PORT}/getconfig",
                    headers={"Content-type": "application/json", "x-api-key": NETPALM_API_KEY}, json=post_data, timeout=10)
    return redirect(url_for(".hello_world_result", posted_data=r.text))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10001)
