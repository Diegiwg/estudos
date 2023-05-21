def menu(*options: list[tuple[str, callable]]):
    m_options = {index: data for index, data in enumerate(options)}
    print("\n".join(f"{index + 1} - {data[0]}" for index, data in m_options.items()))

    while True:
        user_option = input("> ")
        if not user_option.isdigit():
            print("Opção inválida")
            continue

        m_index = int(user_option) - 1
        if m_index not in m_options:
            print("Opção inválida")
            continue

        m_options[m_index][1]()


def view_home():
    print("Home")
    menu(("Listar Pessoas", view_person), ("Sair", lambda: exit(0)))


def view_person():
    print("Pessoas")
    menu(("Voltar", view_home), ("Sair", lambda: exit(0)))


def main():
    view_home()


if __name__ == "__main__":
    main()
