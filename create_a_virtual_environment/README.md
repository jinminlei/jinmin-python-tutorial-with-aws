# Introduction
In this section, I introduce two methods for creating the python virtual environment. The code has been ran in powershell/windows 10. 

# Method 1 - venv (native to python3)
* Create the working directory

    ```mkdir create_a_virtual_environment_1```

    ```cd create_a_virtual_environment_1```

* [Create a virtual environment](https://docs.python.org/3/library/venv.html#creating-virtual-environments) in the current folder
```python -m venv .```

* [Activate the virtual environment](https://docs.python.org/3/library/venv.html)
```.\scripts\activate```

* install packages to virtual environment
```pip install -r requirements.txt```

* run main.py
```python main.py```

* test main.py
```python test_main.py```

* Exit from virtual environment
```deactivate```

# Method 2 - pipenv
* [Install pipenv](https://pypi.org/project/pipenv/)
```https://pypi.org/project/pipenv/```

* Create the working directory
 ```mkdir create_a_virtual_environment_2``` 
    
 ```cd create_a_virtual_environment_2```
    
* Install boto3 and create the virtual environment
```pipenv install boto3```

* run main.py
Replace the argument 'jinmin' with the value that makes sense to you
```pipenv run python test_main.py jinmin```

* run test_main.py (unit test)
```pipenv run python test_main.py```

* Enter virtual environment
```pipenv shell```

* Exit from virtual environment
```exit```

* Check the path of your virtual environment
```pipenv --venv```

* [More to read about pipenv](https://pipenv-fork.readthedocs.io/en/latest/advanced.html)
