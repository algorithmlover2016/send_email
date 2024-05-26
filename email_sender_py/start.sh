# for run only once
python3.11 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -r requirements.txt

# need rerun the server if updated any codes
python3 app.py