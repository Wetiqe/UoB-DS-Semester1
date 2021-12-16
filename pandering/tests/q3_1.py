test = {
  'name': 'Question 3_1',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # complaints_per_product should be a Series
          >>> isinstance(complaints_per_product, pd.Series)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(complaints_per_product.sort_values().head(3).index)
          ['Other financial service', 'Prepaid card', 'Payday loan']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> list(complaints_per_product.sort_values().head(3))
          [16, 110, 119]
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
