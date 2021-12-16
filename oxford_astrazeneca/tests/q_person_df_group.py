test = {
  'name': 'Question person_df_group',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'person_df'
          >>> 'person_df' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # person_df should be a data frame
          >>> isinstance(person_df, pd.DataFrame)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # person_df should have the same number of rows as the total
          >>> # of 'N' in "ox_vax".
          >>> len(person_df) == ox_vax['N'].sum()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The first two columns of person_df should have names
          >>> # "Dose" and "Group"
          >>> list(person_df)[:2]
          ['Dose', 'Group']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The "Group" column should only have the labels "Control"
          >>> # and "Covax".
          >>> set(person_df['Group']) == {'Control', 'Covax'}
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
