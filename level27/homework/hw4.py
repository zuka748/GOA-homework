# 5. რიცხვების ჯამი სიაში
# მომხმარებელს შემოატანინე 5 რიცხვი ერთის შემდეგ მეორე, შეინახე ისინი სიაში (list-ში) და ბოლოს დაბეჭდე მათი ჯამი.

def jami():
    res = []
    for i in range(5):
        num = int(input("sheiyvane ricxvi"))
        res.append(num)
    mtlianad = sum(res)
    print("ricxvebis jamia:", mtlianad)
jami()
