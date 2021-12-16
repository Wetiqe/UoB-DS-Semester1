test = {
  'name': 'Question 1_4',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The result should be a pandas Series.
          >>> # Recall that you can get the data from a column of a data frame
          >>> # as a Series with something like:
          >>> # unemployment['NEI']
          >>> isinstance(pter, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(pter)
          90
          >>> # It looks like you subtracted in the wrong order.
          >>> round(pter.iloc[6], 4) != -1.1282
          True
          >>> round(pter.iloc[6], 4)
          1.1282
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
