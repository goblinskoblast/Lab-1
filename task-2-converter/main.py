UNITS_TO_METERS = {
    "км": 1000.0,
    "м": 1.0,
    "см": 0.01,
    "мм": 0.001,
    "mi": 1609.344,
    "yd": 0.9144,
}


def read_unit(prompt: str) -> str:
    unit = input(prompt).strip().lower()
    while unit not in UNITS_TO_METERS:
        print("Неизвестная единица. Допустимо: км, м, см, мм, mi, yd.")
        unit = input(prompt).strip().lower()
    return unit


source_unit = read_unit("Исходная единица: ")
target_unit = read_unit("Целевая единица: ")
value = float(input("Значение: ").replace(",", "."))

result = value * UNITS_TO_METERS[source_unit] / UNITS_TO_METERS[target_unit]
print(f"Результат: {value:g} {source_unit} = {result:.2f} {target_unit}")
