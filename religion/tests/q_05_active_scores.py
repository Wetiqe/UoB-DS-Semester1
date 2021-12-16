test = {
  'name': 'Question 05_active_scores',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'active_scores'
          >>> 'active_scores' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'active_scores'
          >>> # from its initial state (of ...)
          >>> active_scores is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(active_scores) == 48
          True
          >>> list(np.unique(active_scores))
          [0, 1, 2, 3]
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
