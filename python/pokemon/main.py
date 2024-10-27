from name_service import NameService
from pokemon import Pokemon
from player import Player
from pikachu import Pikachu


def test_interface():
    print("=== NameServiceインターフェースのインスタンス化テスト ===")
    try:
        name_service = NameService()
        print("エラー: NameServiceのインスタンス化が成功しました")
    except TypeError as e:
        print("期待通りのエラー:")
        print(f"TypeError: {e}")
        print()


def test_abstract_class():
    print("=== Pokemon抽象クラスのインスタンス化テスト ===")
    try:
        pokemon = Pokemon("ピカチュウ", "でんき", None, 100)
        print("エラー: Pokemon抽象クラスのインスタンス化が成功してしまいました")
    except TypeError as e:
        print("期待通りのエラー:")
        print(f"TypeError: {e}")
        print()


def test_player():
    print("=== Playerのテスト ===")
    player = Player("さとし")
    print(f"現在の名前: {player.name}")

    print("不適切な名前に変更を試みる...")
    player.name = "うんこ"
    print(f"変更後の名前: {player.name}")

    print("適切な名前に変更...")
    player.name = "レッド"
    print(f"変更後の名前: {player.name}")
    print()


def test_pikachu():
    print("=== Pikachuのテスト ===")
    pikachu = Pikachu("ピカチュウ", "でんき", None, 100)
    print(f"現在の名前: {pikachu.name}")

    print("不適切な名前に変更を試みる...")
    pikachu.name = "うんこ"
    print(f"変更後の名前: {pikachu.name}")

    print("攻撃の実行...")
    pikachu.attack()
    print()


def test_inheritance():
    print("=== 継承関係のテスト ===")
    player = Player("さとし")
    pikachu = Pikachu("ピカチュウ", "でんき", None, 100)

    print("クラスの継承関係チェック:")
    print(f"- Playerは、NameServiceのサブクラス: {issubclass(Player, NameService)}")
    print(f"- Pikachuは、Pokemonのサブクラス: {issubclass(Pikachu, Pokemon)}")
    print(f"- Pokemonは、NameServiceのサブクラス: {issubclass(Pokemon, NameService)}")

    print("\nインスタンスの型チェック:")
    print(f"- playerはNameServiceのインスタンス: {isinstance(player, NameService)}")
    print(f"- pikachuはPokemonのインスタンス: {isinstance(pikachu, Pokemon)}")
    print()


def main():
    test_interface()
    test_abstract_class()
    test_player()
    test_pikachu()
    test_inheritance()


if __name__ == "__main__":
    main()
