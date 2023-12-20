dic={
    122:"saif",
    211:"alex",
    311:"jhon",
    411:"rush"
}
print(dic)
print(len(dic))
for l in dic.keys():
    print(l)
    info={
        'name':"saif",
        'age':23,
        'eligible':True,
    }
    print(info.items())
    for key,value in info.items():
        print(value)