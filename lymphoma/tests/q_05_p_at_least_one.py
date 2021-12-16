test = {
  'name': 'Question 05_p_at_least_one',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'p_at_least_one'
          >>> 'p_at_least_one' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'p_at_least_one'
          >>> # from its initial state (of ...)
          >>> p_at_least_one is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Proportion should be between 0 and 1
          >>> 0 <= p_at_least_one <= 1
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
