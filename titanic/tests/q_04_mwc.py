test = {
  'name': 'Question 04_mwc',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'mwc'
          >>> 'mwc' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'mwc'
          >>> # from its initial state (of ...)
          >>> mwc is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(mwc, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(mwc) == len(titanic)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(np.unique(mwc) == ['child', 'female', 'male'])
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
