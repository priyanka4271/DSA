from tkinter.font import names

Employee ={1:{"name":"harleeen","age":20,"Roll no":2323443,"gmail":"harleen@gmail.com"},
          2: {"name":"Hari",    "age":22, "Roll no":2323463,"gmail":"hari@gmail.com"},
          3: {"name":"harsh",   "age":29, "Roll no":2323743,"gmail":"harsh@gmail.com"},
           4:{"name":"heena",    "age":25,"Roll no":2329443,"gmail":"heena@gmail.com"}}
print(Employee)
for i in Employee.items():
    print(i)
print("hello")
print(Employee.pop(1))
print(Employee.get("name"))
