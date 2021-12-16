test = {
  'name': 'Question calc_ld_sd_ediff',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to define the function 'calc_ld_sd_ediff'
          >>> 'calc_ld_sd_ediff' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # calc_ld_sd_ediff should be a function.
          >>> callable(calc_ld_sd_ediff)
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
          >>> # Oops, have you deleted 'vax_eff_diff'?
          >>> 'vax_eff_diff' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> calc_ld_sd_ediff(ox_vax) == vax_eff_diff
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
