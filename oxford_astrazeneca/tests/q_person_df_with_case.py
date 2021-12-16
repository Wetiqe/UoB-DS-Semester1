test = {
  'name': 'Question person_df_case',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # The columns of person_df should have names
          >>> # "Dose", "Group" and "Case"
          >>> list(person_df)
          ['Dose', 'Group', 'Case']
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The "Case" column should only have True and False values.
          >>> set(person_df['Case']) == {True, False}
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The "Case" column have the same number of True values as
          >>> # "Cases" in the original table.
          >>> np.count_nonzero(person_df['Case']) == ox_vax['Cases'].sum()
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
