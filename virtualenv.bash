rm -rf venv
virtualenv venv
cd venv
source bin/activate
cd ..
curl https://bootstrap.pypa.io/get-pip.py | python
pip install flask
