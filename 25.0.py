'''

尴尬 忘记了字符串split方法 虽然脑子想到split了 下次要多想想
推测 (mydict['id'], mydict['name']) 等号右边的项
'''
data = '1000,xiaojiayu,male'
mydict = {}
(mydict['id'], mydict['name'], mydict['sex']) = data.split(',')

print('id:' + mydict['id']) #用+拼接
print('name: ' + mydict['name'])
print('sex: ' + mydict['sex'])
