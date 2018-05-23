# Setup virtual environment and dependencies
rm -rf venv
virtualenv venv
cd venv
source bin/activate
cd ..
curl https://bootstrap.pypa.io/get-pip.py | python
pip install flask
pip install wtforms

# Note you'll have to activate the venv again after running this script
# Just run `source bin/activate` in the /venv directory
