def order(menu, *ops, **kwops):
    print(f"메뉴: {menu}")
    print(f"옵션: {ops}")
    print(f"정보: {kwops}")

order("아메리카노", "얼음 적게", "샷추가", size="Tall", takeout=True)