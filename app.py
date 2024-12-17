from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def fetch_identity_token():
    try:
        # Target metadata URL
        audience = "https://vault-cluster-public-vault-b1e58017.a24ed26e.z1.hashicorp.cloud:8200"
        metadata_url = f"http://metadata.google.internal/computeMetadata/v1/instance/service-accounts/default/identity?audience={audience}"
        headers = {"Metadata-Flavor": "Google"}
        
        # Fetch identity token
        response = requests.get(metadata_url, headers=headers)
        response.raise_for_status()
        
        # Return the token in JSON response
        return jsonify({
            "identity_token": response.text
        })
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))