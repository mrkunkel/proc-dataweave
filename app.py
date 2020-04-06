import os
import subprocess
import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def run_transform():
   payload_url = request.args.get("payload_url")
   r = requests.get(payload_url, allow_redirects=True)
   open('payload.json', 'wb').write(r.content)

   transform_dw = request.get_data()
   open('transform.dw', 'wb').write(transform_dw)

   dataweave = subprocess.run(["/root/.dw/dw", "-i", "payload", "payload.json", "-f", "transform.dw"], stdout=subprocess.PIPE, text=True)
   return dataweave.stdout

if __name__ == "__main__":
   app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))
