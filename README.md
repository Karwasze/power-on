# Power on!
## How to run it?

1. Clone the repository
2. Activate the venv: ```. venv/bin/activate```
3. Install etherwake (e.g. ```sudo apt install etherwake```)
4. Install (```npm install -g localtunnel```) and run (
```lt --port 5000```) **localtunnel**, save the address it returns.
5. Run the app using
```FLASK_APP=power-on MAC_ADDRESS=<your MAC address> flask run```
6. Access the web app using the address provided in 4.
