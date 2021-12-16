test = {
  'name': 'Question 1_5',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Did you add the column to the employment data frame?
          >>> 'PTER' in unemployment
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> by_pter.head(1)
                    Date      NEI  NEI-PTER    PTER
          62  2009-07-01  10.8089   12.7404  1.9315
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
