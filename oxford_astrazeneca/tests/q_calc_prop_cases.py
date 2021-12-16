test = {
  'name': 'Question calc_prop_cases',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to define the function 'calc_prop_cases'
          >>> 'calc_prop_cases' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # calc_prop_cases should be a function.
          >>> callable(calc_prop_cases)
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
          >>> # Oops, have you deleted 'prop_covid'?
          >>> 'prop_covid' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Wait - did you use "ox_vax" inside the function, instead of
          >>> # the data frame *like* "ox_vax" (called "df")?
          >>> my_df = pd.DataFrame()
          >>> my_df['N'] = [10, 20, 30, 40]
          >>> my_df['Cases'] = [2, 3, 4, 5]
          >>> calc_prop_cases(my_df) == prop_covid
          False
          >>> calc_prop_cases(my_df) == 14 / 100
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> calc_prop_cases(ox_vax) == prop_covid
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Wait - did you use "ox_vax" inside the function, instead of
          >>> # the data frame *like* "ox_vax" (called "df")?
          >>> my_df = pd.DataFrame()
          >>> my_df['N'] = [10, 20, 30, 40]
          >>> my_df['Cases'] = [2, 3, 4, 5]
          >>> calc_prop_cases(my_df) == prop_covid
          False
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
