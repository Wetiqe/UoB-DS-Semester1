test = {
  'name': 'Question calc_efficiency',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to define the function 'calc_efficiency'
          >>> 'calc_efficiency' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # calc_efficiency should be a function.
          >>> callable(calc_efficiency)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Oops, have you deleted 'ox_vax'?
          >>> 'ox_vax' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Oops, have you deleted 'vax_eff'?
          >>> 'vax_eff' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> calc_efficiency(ox_vax) == vax_eff
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
