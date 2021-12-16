test = {
  'name': 'Question fake_ediffs',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'fake_ediffs'
          >>> 'fake_ediffs' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'fake_ediffs'
          >>> # from its initial state (of ...)
          >>> fake_ediffs is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(fake_ediffs)
          1000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.all(np.logical_and(fake_ediffs > -1, fake_ediffs < 1))
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
