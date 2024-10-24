from juice import Juice
from suica import Suica
from vending_machine import VendingMachine


def handle_charge(suica, amount):
    try:
        suica.charge(amount)
    except ValueError as e:
        print(e)


def handle_buy(vending_machine, juice_name, suica):
    try:
        vending_machine.buy_with_suica(juice_name, suica)
    except ValueError as e:
        print(e)


def main():
    suica = Suica()
    print("Suicaの残高の初期値は500円です")
    print(f"現在のSuicaの残高は{suica.balance}円です")
    print("=" * 50)
    print("100円未満をチャージしようとすると例外が発生します")
    handle_charge(suica, 99)
    print("=" * 50)
    print("100円をチャージします")
    handle_charge(suica, 100)
    print(f"現在のSuicaの残高は{suica.balance}円です")
    print("=" * 50)

    vending_machine = VendingMachine()
    print("自動販売機はデフォルトでペプシ(150円)を5本持っています")
    default_juice = vending_machine.juice_stock
    for juice in default_juice:
        print(juice[0], ":", juice[1], "本")
    available_juice = vending_machine.available_juice
    for juice in available_juice:
        print(juice[0], ":", juice[1], "円")
    print("=" * 50)
    print("初期在庫にモンスター(230円) 5本、いろはす(120円) 5本を追加します")
    vending_machine.add_juice(Juice("モンスター", 230), 5)
    vending_machine.add_juice(Juice("いろはす", 120), 5)
    new_juice = vending_machine.juice_stock
    for juice in new_juice:
        print(juice[0], ":", juice[1], "本")
    print("-" * 50)
    new_available_juice = vending_machine.available_juice
    for juice in new_available_juice:
        print(juice[0], ":", juice[1], "円")
    print("=" * 50)
    print(f"現在のSuicaの残高は{suica.balance}円です")
    print("いろはすを5本(600円)購入します。")
    for _ in range(5):
        handle_buy(vending_machine, "いろはす", suica)
    print(f"現在のSuicaの残高は{suica.balance}円です")
    print("=" * 50)
    print("6本目のいろはすを購入しようとすると例外が発生します")
    handle_buy(vending_machine, "いろはす", suica)
    print("=" * 50)
    print(f"現在のSuicaの残高は{suica.balance}円です")
    print("この状態でモンスターを購入しようとすると例外が発生します")
    handle_buy(vending_machine, "モンスター", suica)
    default_juice = vending_machine.juice_stock
    print("=" * 50)
    print("現在の在庫は以下の通りです")
    for juice in default_juice:
        print(juice[0], ":", juice[1], "本")
    print("=" * 50)
    print("購入可能なリストは以下の通りです")
    available_juice = vending_machine.available_juice
    for juice in available_juice:
        print(juice[0], ":", juice[1], "円")
    print("=" * 50)
    print("自販機の現在の売上は以下の通りです")
    print(vending_machine.sales_amount)
    print("=" * 50)
    print("いろはすの在庫を5本追加します")
    irohasu = Juice("いろはす", 120)
    vending_machine.add_juice(irohasu, 5)
    print("=" * 50)
    print("現在の在庫は以下の通りです")
    default_juice = vending_machine.juice_stock
    for juice in default_juice:
        print(juice[0], ":", juice[1], "本")
    print("=" * 50)
    print("購入可能なリストは以下の通りです")
    available_juice = vending_machine.available_juice
    for juice in available_juice:
        print(juice[0], ":", juice[1], "円")


if __name__ == "__main__":
    main()
