test = {
  'name': 'Question 03_gender_by_survived_p',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'gender_by_survived_p'
          >>> 'gender_by_survived_p' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'gender_by_survived_p'
          >>> # from its initial state (of ...)
          >>> gender_by_survived_p is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The values in the table should be proportions
          >>> # and sum to around 1 across the rows.
          >>> np.allclose(gender_by_survived_p.transpose().sum(), 1)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> isinstance(gender_by_survived, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> gender_by_survived.shape
          (2, 2)
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
