# capone
#
# Setup
### Install python 2.7
If you have not have python 2.7, download it at https://www.python.org/downloads/release/python-2713/


### Install pip
If you have not have pip, download it at https://bootstrap.pypa.io/get-pip.py.
```
python get-pip.py
```

### Create a virtual environment
Virtual environment lets you have different dependencies in multiple projects

Install virtualenv if you haven't:
```
sudo pip install virtualenv
```

If virtualenv is not found, add /usr/local/bin to your path in ~/.bashrc
```
export PATH=$PATH:/usr/local/bin
```

Create virtualenv
```
cd capone
virtualenv env
source env/bin/activate
```
Install requirements
```
pip install -r requirements.txt
```

### Run the program
You can simply start running it by:
```
python bookkeeper.py
```
For additional options:
```
python bookkeeper.py -h
```
