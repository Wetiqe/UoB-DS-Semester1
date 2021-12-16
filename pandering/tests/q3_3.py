test = {
  'name': 'Question 3_3',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # complaints_per_company should be a Series
          >>> isinstance(complaints_per_company, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(complaints_per_company.sort_values().tail(3).index)
          ['TransUnion Intermediate Holdings, Inc.', 'Experian', 'Equifax']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(complaints_per_company.sort_values().tail(3))
          [1034, 1240, 1440]
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
