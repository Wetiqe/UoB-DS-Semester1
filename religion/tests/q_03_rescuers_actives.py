test = {
  'name': 'Question 03_rescuers_actives',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'rescuers_actives'
          >>> 'rescuers_actives' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'rescuers_actives'
          >>> # from its initial state (of ...)
          >>> rescuers_actives is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(rescuers_actives)
          ['rescuers', 'actives']
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
