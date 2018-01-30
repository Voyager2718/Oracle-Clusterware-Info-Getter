# Oracle-Clusterware-Info-Getter
Get cluster information and store them into a file.

# Usage
```
python cinfo.py [OPTION]
  -o, --output <output location>    by default, will write to file /var/opt/info.
  -h                                get help information.
```

# Extend
Create another **py** file, put it into the root directory, implement `run()` in your **py** file. Then finally put your file name into `INSTALLED_APPS` in **settings.py**

## extract.py
This module helps your to extract information and handle exceptions.

Just import extract, call `extract.extractInfomation(command, regex, path, failedToExtractCallBack, successCallBack, envs)`. It will returns the information that you needs.
```python
'''
@command:                 <string> Command that you want to run and extract information from.
@regex:                   <string> The regex that extracts information.
@path:                    [Optional] <string> You may need to pass ORACLE_HOME if you didn't export it.
@failedToExtractCallBack  [Optional] <function> If this is set, will call this function. Unless it will exit with an error message.
@successCallBack          [Optional] <function> If this is set, will call this function and return the return value of this function.
@envs                     [Optional] <string> You may need to export some envs to run the command, then put them here or set them in settings.ENVIROMENTS.
'''
extract.extractInfomation(command, regex, path, failedToExtractCallBack, successCallBack, envs)
```
