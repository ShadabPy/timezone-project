# Table of content
 * Introduction
 * Requirements
 * Configuration
 
# Introduction:-
- It is the time zone based task. `action_package`
is a main project directory.
- There is one datetime module .It is used to calculate datetime logic
- `main_file` is used to execute the project.
It is take 5 and 6 argument from terminal.
- `logger_file` is used to log the code statement and errors.
- `util` is used make some constant.

# Requirements:-
- Only setup the python 2.7. no need to install any other packages.
# Configuration:-
- `main_file` is used to run the project.
---
* `**Input**` 
- a)- argument1 = `task_type`
- b)- argument2 = `user`
- c)- argument3 = `country`
- d)- argument4 = `start_time`
- e)- argument5 = `end_time`
- f)- argument6 = `day`

- NOTE1:- `argument6` is optional.If we need to 
execute on a particular day. we can add day with `,` string.
It is case-insensitive.
- NOTE2:- `Country` value should be `india` or `usa` .
 it is case-insensitive.Other values ​may not be acceptable.
---
- Ex:-   
- a)- argument1 = `email`
- b)- argument2 = `u1`
- c)- argument3 = `india`
- d)- argument4 = `12:00:00`
- e)- argument5 = `20:00:00`
- f)- argument6 = `sunday,wednesday`
---
- **Command to run project**:-
- Below command is used to run the main_file.
- Main file pah:-
```bash
$ cd timezone_based_project/action_package/
```
- The action will only be executed between the specified time period

``` python
 python main_file.py email u1 india 12:00:00 20:00:00
```
- if we need to use specific day feature, we can use below command
``` python
 python main_file.py email u1 india 12:00:00 20:00:00 sunday,wednesday

```

- **logger_file**
- Need to make a directory.Please follow below command.
```bash
$ cd /var/log/
$ sudo mkdir assignment
```
- The log-file will be automatically created in the name of timezone_project.log