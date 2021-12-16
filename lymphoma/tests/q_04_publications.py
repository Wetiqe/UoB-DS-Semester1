test = {
  'name': 'Question 04_publications',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'publications'
          >>> 'publications' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'publications'
          >>> # from its initial state (of ...)
          >>> publications is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Publication counts should be between 0 and 4
          >>> np.all(publications >= 0)
          True
          >>> np.all(publications <= 4)
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
