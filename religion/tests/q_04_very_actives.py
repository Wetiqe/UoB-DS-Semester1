test = {
  'name': 'Question 04_very_actives',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'very_actives'
          >>> 'very_actives' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'very_actives'
          >>> # from its initial state (of ...)
          >>> very_actives is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(very_actives) == 1000
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(very_actives >= 0)
          True
          >>> np.all(very_actives <= 74)
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
