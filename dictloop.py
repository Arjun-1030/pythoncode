dictionary={}

dictionary['name']='Ram'
dictionary['age']=18
dictionary['subject']=['math','science','nepali']
dictionary['education']={'school':
    {
    'name':'Xavier school',
    'address':'kalopul, kathmandu'

    },
'High school':{
    'name':'DAV college',
    'address':'jawlakhel,lalitpur'
},
'Bachelor level':{
    'name':'xavier college',
    'address':'boudha,kathmandu'
  }
}
print(dictionary)
#for i in dictionary.keys():
 #   print(i)
#accessing element of nested dictionary from for loop
for i,j  in dictionary['education']['school'].items():
    print(i,"=",j)
#dict={key:{nestkey:{subnested:values}}
print(dictionary['education']['school']['name'])
