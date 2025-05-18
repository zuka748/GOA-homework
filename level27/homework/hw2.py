# 3. პაროლი
# მომხმარებელი შეიყვანს პაროლს. თუ პაროლი 8-ზე ნაკლები სიმბოლოა — დაბეჭდე "პაროლი ძალიან მოკლეა", თუ 8 ან მეტი — "პაროლი მიღებულია".


password = input("sheiyvane paroli: ")
if len(password) < 8:
    print("paroli dzalian moklea")
else:
    print("paroli migebulia")



