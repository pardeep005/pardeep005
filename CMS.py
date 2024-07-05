id_list=[10,20,30,40]
name_list=["vijay","anuj","vikas","agrim"]
age_list=[22,45,43,54]
while(1):
    ch=input("enter your choice add/delete/search/:")
    if ch=="add":
        add_id=input("enter you id:")
        add_name=input("enter your name:")
        add_age=input("enter your age:")
        id_list.append(add_id)
        name_list.append(add_name)
        age_list.append(add_age)

    else:
        id=int(input("enter your id:"))
        if ch=="search":
                if id in id_list:
                   i=id_list.index(id)
                print(id_list[i])
                print(name_list[i])
                print(age_list[i])
        elif(ch=="delete"):
                if id in id_list:
                    i=id_list.index(id)
                    id_list.pop(i)
                    name_list.pop(i)
                age_list.pop(i)
        else:
                print("invalid choice")

    print(id_list)
    print(name_list)
    print(age_list)









