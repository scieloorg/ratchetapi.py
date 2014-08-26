.. _quickstart:

Quickstart
==========

When a `ratchetapi.Client` instance is initialized, the process automaticaly 
instrospects the API server in order to make available only the endpoints part 
of the specified API version. The API version may be passed as keyword argument 
`version` when creating the `ratchetapi.Client` instance. If ommited, the highest 
version is used.

::

    >>> client = ratchetapi.Client('some.user', 'some.api_key') 
    

Listing available endpoints::

    >>> client.endpoints
    [u'journals', u'issues', u'articles']
    >>>

Listing all items of an endpoint::

    >>> for journal in client.query('journals').all(): print journal['code'], journal['total']
    ...
    0100-4670 1809
    0103-5053 1023
    0074-0276 990
    0100-879X 869
    1516-1439 782
    0104-1169 742
    >>> 


Getting a specific item::

    >>> journal = client.query('journals').get('0100-4670')
    >>> journal['total']
    1809
    >>>

