my_dict = {'Alexander': 1991, 'Anna': 1992, 'Denis': 2013}
print('Dict:', my_dict)
print('Existing value:', my_dict['Anna'])
print('Not existing value:', my_dict.get('Roman'))
my_dict.update({'Yura': 1986,
                'Pavel': 1990})
print('Modified dictionary:', my_dict)
my_dict.pop('Alexander')
print('Deleted Alexander:', my_dict)


my_set = {2, 4, 6, 2, 2, 4, 6, 'Banana', 'Mango'}
print(my_set)
my_set.update([1, 'Kiwi'])
my_set.discard('Banana')
print(my_set)
