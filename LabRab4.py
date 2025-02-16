from typing import Optional


class Aircraft:
    """
    Базовый класс для всех самолетов.
    """

    def __init__(self, model: str, manufacturer: str, year: int, max_speed: float):
        """
        Конструктор класса Aircraft.

        :param model: Модель самолета (строка).
        :param manufacturer: Производитель самолета (строка).
        :param year: Год выпуска самолета (целое число).
        :param max_speed: Максимальная скорость самолета в км/ч (число с плавающей точкой).
        """
        self._model = model  # Защищенный атрибут, чтобы предотвратить случайное изменение извне.
        self._manufacturer = manufacturer  # Защищенный атрибут, чтобы предотвратить случайное изменение извне.
        self.year = year  # Публичный атрибут, так как год выпуска может быть легко изменен.
        self.max_speed = max_speed  # Публичный атрибут, так как максимальная скорость может меняться при модификации.

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.

        :return: Строковое представление самолета.
        """
        return f"{self._manufacturer} {self._model} ({self.year})"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для разработчиков.

        :return: Формальное строковое представление самолета.
        """
        return f"Aircraft(model={self._model}, manufacturer={self._manufacturer}, year={self.year}, max_speed={self.max_speed})"

    def take_off(self) -> None:
        """
        Метод для имитации взлета самолета.
        """
        print(f"{self._manufacturer} {self._model} выполняет взлет.")


class PassengerAircraft(Aircraft):
    """
    Дочерний класс для пассажирских самолетов.
    """

    def __init__(self, model: str, manufacturer: str, year: int, max_speed: float, seating_capacity: int):
        """
        Конструктор класса PassengerAircraft. Расширяет базовый класс дополнительным атрибутом seating_capacity.

        :param seating_capacity: Количество мест в самолете (целое число).
        """
        super().__init__(model, manufacturer, year, max_speed)
        self.seating_capacity = seating_capacity  # Публичный атрибут, так как количество мест может меняться.

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для добавления информации о вместимости.

        :return: Строковое представление пассажирского самолета.
        """
        return f"{super().__str__()} - Вместимость: {self.seating_capacity} человек"

    def take_off(self) -> None:
        """
        Переопределение метода take_off для учета особенностей пассажирских самолетов.
        Например, проверка наличия пассажиров перед взлетом.

        :return: Сообщение о взлете или предупреждение об отсутствии пассажиров.
        """
        if self.seating_capacity > 0:
            super().take_off()
        else:
            print("Ошибка: Недостаточно пассажиров для выполнения рейса.")

    def calculate_fuel_consumption(self, distance: float) -> float:
        """
        Вычисляет расход топлива на заданное расстояние.

        :param distance: Расстояние в километрах.
        :return: Расход топлива в литрах.
        """
        average_consumption = 5  # Средний расход топлива на 100 км для пассажирских самолетов (пример).
        return distance * (average_consumption / 100)


class CargoAircraft(Aircraft):
    """
    Дочерний класс для грузовых самолетов.
    """

    def __init__(self, model: str, manufacturer: str, year: int, max_speed: float, load_capacity: float):
        """
        Конструктор класса CargoAircraft. Расширяет базовый класс дополнительным атрибутом load_capacity.

        :param load_capacity: Грузоподъемность самолета в тоннах (число с плавающей точкой).
        """
        super().__init__(model, manufacturer, year, max_speed)
        self.load_capacity = load_capacity  # Публичный атрибут, так как грузоподъемность может меняться.

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для добавления информации о грузоподъемности.

        :return: Строковое представление грузового самолета.
        """
        return f"{super().__str__()} - Грузоподъемность: {self.load_capacity} тонн"

    def take_off(self) -> None:
        """
        Переопределение метода take_off для учета особенностей грузовых самолетов.
        Например, проверка загруженности перед взлетом.

        :return: Сообщение о взлете или предупреждение о недостаточной загрузке.
        """
        if self.load_capacity > 0:
            super().take_off()
        else:
            print("Ошибка: Самолет не загружен. Взлет невозможен.")

    def calculate_payload(self, weight: float) -> bool:
        """
        Проверяет, можно ли загрузить самолет заданным весом.

        :param weight: Вес груза в тоннах.
        :return: True, если груз помещается, иначе False.
        """
        return weight <= self.load_capacity


if __name__ == "__main__":
    # Пример использования классов
    passenger_plane = PassengerAircraft(
        model="Superjet 100",
        manufacturer="Sukhoi",
        year=2022,
        max_speed=830,
        seating_capacity=98
    )

    cargo_plane = CargoAircraft(
        model="747-400F",
        manufacturer="Boeing",
        year=2018,
        max_speed=905,
        load_capacity=112  # Грузоподъемность Boeing 747-400F составляет до 112 тонн
    )

    print(passenger_plane)  # Выводит информацию о пассажирском самолете
    print(cargo_plane)  # Выводит информацию о грузовом самолете

    passenger_plane.take_off()  # Взлет пассажирского самолета
    cargo_plane.take_off()  # Взлет грузового самолета

    print(passenger_plane.calculate_fuel_consumption(2000))  # Расчет расхода топлива для пассажирского самолета
    print(cargo_plane.calculate_payload(100))  # Проверка возможности загрузки грузового самолета