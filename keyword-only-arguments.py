def keyword_only_function(parameter, *, option1=False, option2=''):
    pass

In this example, option1, and option2 are only specifiable via the keyword argument syntax. The following is valid

keyword_only_function(3, option1=True, option2='Hello World!')
But this example will raise an error

keyword_only_function(3, True, 'Hello World!')




https://python-3-for-scientists.readthedocs.io/en/latest/python3_advanced.html