test = {
  'name': 'Question 02_top_religion',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'top_religion'
          >>> 'top_religion' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'top_religion'
          >>> # from its initial state (of ...)
          >>> top_religion is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you drop the last row in the table?
          >>> len(top_religion) == 4
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Did you set the index from the 'level' column?
          >>> 'level' not in top_religion
          True
          >>> list(top_religion.index)
          ['Very', 'Somewhat', 'Not very', 'Not at all']
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
