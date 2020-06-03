# [Install Packages](https://packaging.python.org/tutorials/installing-packages/#id14)
````shell script
mkdir /py/jorge

python3 -m venv jorge_venv  # virtualenv jorge_venv
source jorge_venv/bin/activate

python3.7 -m pip install --upgrade pip setuptools wheel
pip install --upgrade pip
pip3 install -r requirements.txt
````