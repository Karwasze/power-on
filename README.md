# Power on!
## How to run it?

1. Clone the repository
2. Activate the venv: ```. venv/bin/activate```
2. Install (```npm install -g localtunnel```) and run (
```lt --port 5000```) **localtunnel**, save the address it returns.
3. Run the app using
```FLASK_APP=power-on MAC_ADDRESS=<your MAC address> flask run```
4. Access the web app using the address provided in 2.