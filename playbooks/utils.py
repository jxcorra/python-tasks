def print_divider(section_name: str, separator_len: int = 15) -> None:
    print(f'{"#" * separator_len} {section_name.upper()} {"#" * separator_len}')


def setup_object_printer_with_globals(module_globals):
    __globals = module_globals

    def wrapper(obj):
        name = None
        for key, value in __globals.items():
            if obj == value:
                name = key
                break

        print_divider(name, 5)
        for attr_name, attr_value in obj.__dict__.items():
            if callable(attr_value):
                print(f'- {attr_name}: function {attr_value.__name__}')
            else:
                print(f'- {attr_name}: {attr_value}')

    return wrapper
