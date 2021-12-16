test = {
  'name': 'Question 01_counts',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'counts'
          >>> 'counts' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'counts'
          >>> # from its initial state (of ...)
          >>> counts is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Counts should all be from 0 through 17.
          >>> np.all(counts >= 0)
          True
          >>> np.all(counts <= 17)
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
