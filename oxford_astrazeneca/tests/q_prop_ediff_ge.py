test = {
  'name': 'Question prop_ediff_ge',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'prop_ediff_ge'
          >>> 'prop_ediff_ge' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'prop_ediff_ge'
          >>> # from its initial state (of ...)
          >>> prop_ediff_ge is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 0 < prop_ediff_ge < 0.5
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
