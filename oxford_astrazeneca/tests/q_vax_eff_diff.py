test = {
  'name': 'Question vax_eff_diff',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'vax_eff_diff'
          >>> 'vax_eff_diff' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'vax_eff_diff'
          >>> # from its initial state (of ...)
          >>> vax_eff_diff is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0.1 < vax_eff_diff < 0.5
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
