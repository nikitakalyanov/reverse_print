
def reverse_print(some_list):
    if some_list['next'] is not None:
        reverse_print(some_list['next'])
    print(some_list['value'])

'''
# example
# uncomment to execute
some_list = {
  'value': 1,
  'next': {
    'value': 2,
    'next': {
      'value': 3,
      'next': {
        'value': 4,
        'next': None,
      },
    },
  },
}

reverse_print(some_list)
'''
