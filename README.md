Imagination Entry Test
=======================
The brief was to construct a command line script that returns the arithmetic mean of the rank of male child names within the top 1000 results from the US social security database over a given period of time.

Requirements
----------------------
No third party libraries were permitted during development, so only interpreter internal libraries have been used. The script was written for python 2.7 but care has been taken so that it _should_ work under python 3 too.

Running
----------------------
Running the script is pretty simple really, it has a shebang line which uses env to find an interpreter so should run fine on any POSIX compliant system without the need to specify the interpreter binary path.

```
imagination-test:develop$ ./popular_names.py -h
usage: popular_names.py [-h] name [start_year] [end_year]

Gives the mean of rank of a male name within the top 1000 results over a given
period of time.

positional arguments:
  name        The name to look up
  start_year  The start year
  end_year    The end year

optional arguments:
  -h, --help  show this help message and exit
```

start_year if not specified is defaulted to 1900.

end_year if not specified is defaulted to 2014.

Return codes
-------------
POSIX return codes are employed in the app.

Anything greater than 0 for a return code indicates an error, a table of which can be found below

| Return Code 	| Reason                                                      	|
|-------------	|-------------------------------------------------------------	|
| 1           	| HTTP Error encountered before connecting to the web service 	|
| 2           	| Invalid URL for web service                                 	|
| 3           	| HTTP Error encountered after connecting to the web service  	|
| 4           	| Generic 'Pokemon' exception handler - any other error                                                             	|

Installing
-----------
I don't really see why you'd want to, but should you wish to install this systemwide, a setup.py has been provided,
this will install the script into your python environment and can be called as: popular-names

```
python setup.py install
```

Author
------
```
Nick Pack <nick@nickpack.com>
```

Licence
--------
Copyright (c) 2015 Nick Pack
Licensed under the MIT license.