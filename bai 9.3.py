cannang=float(input("cân nặng là:"))
chieucao=float(input("chiều cao là"))
BMI= cannang /(chieucao*chieucao)
if BMI<18.5:
    print("gầy")
elif BMI>=25:
    print("béo")
else:
    print("bình thường") 