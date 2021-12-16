test = {
  'name': 'Question 1_2',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> by_nei.iloc[1, :3]
          Date        2010-01-01
          NEI            10.9054
          NEI-PTER       12.7311
          Name: 64, dtype: object
          >>> by_nei_pter.iloc[1, :3]
          Date        2009-07-01
          NEI            10.8089
          NEI-PTER       12.7404
          Name: 62, dtype: object
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
