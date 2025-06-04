from flask import Flask
import requests
import time
import threading
import os


app = Flask(__name__)

def on_server_run():
    while True:
        try: 
            response = requests.get('https://attendance-registration-system.onrender.com/ping')
            print(response)
        except Exception as e:
            print("Error: ", e)
        time.sleep(5 * 60)

if __name__ == '__main__':
    thread = threading.Thread(target=on_server_run, daemon=True)
    thread.start()
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=port)