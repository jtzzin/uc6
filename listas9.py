r1_mobile = ["oi oi", "ai ai", "ui ui"]
item_removido = [1]

if r1_mobile in item_removido:
    r1_mobile.remove("corinthians")
else:
    print("\n" + "o produto CORINTHIANS não consta no estoque.")

print("\n" + "os modelos atuais são:", r1_mobile, "\n")