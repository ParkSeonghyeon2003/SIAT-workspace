def show_profile(**kwargs):
    print(type(kwargs))
    print(kwargs)

show_profile(name="이철수", age=20)
show_profile(name="김영희", age=25, city="서울")