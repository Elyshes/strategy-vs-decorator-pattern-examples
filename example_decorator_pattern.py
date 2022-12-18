# base component interface that can be altered by decorators
class Beverage():
    def description(self) -> str:
        pass

    def price(self) -> float:
        pass


# concrete component provides default implementation
class Mochaccino(Beverage):
    def description(self) -> str:
        return "Moccachino"

    def price(self) -> float:
        return 2


# concrete component provides default implementation
class LatteMacchiato(Beverage):
    def description(self) -> str:
        return "Latte Machiato"

    def price(self) -> float:
        return 2.3


# concrete component provides default implementation
class CoffeeBlack(Beverage):
    def description(self) -> str:
        return "Coffee black"

    def price(self) -> float:
        return 1.9


# base decorator implements the same component interface and
# defines the wrapping interface for all concrete decorators
class IngredientDecorator(Beverage):
    _component: Beverage = None

    def __init__(self, component: Beverage) -> None:
        self._component = component

    def component(self) -> Beverage:
        return self._component

    def description(self) -> str:
        return self._component.description()

    def price(self) -> float:
        return self._component.price()


# concrete decorator
class ExtraMilk(IngredientDecorator):
    def description(self) -> str:
        return f"{super().description()}, extra milk"

    def price(self) -> float:
        return super().price() + .4


# concrete decorator
class ExtraSuggar(IngredientDecorator):
    def description(self) -> str:
        return f"{super().description()}, extra suggar"

    def price(self) -> float:
        return super().price() + .2


# concrete decorator
class ExtraChocolate(IngredientDecorator):
    def description(self) -> str:
        return f"{super().description()}, extra chocolate"

    def price(self) -> float:
        return super().price() + .5


def print_order(component: Beverage) -> None:
    print(
        f"\nYOUR ORDER: {component.description()}\nTOTAL COST: {component.price()} Euro\n")


def main():
    mochaccino = Mochaccino()
    mochaccino = ExtraMilk(mochaccino)
    print_order(mochaccino)

    coffee = CoffeeBlack()
    coffee = ExtraSuggar(coffee)
    coffee = ExtraMilk(coffee)
    print_order(coffee)


if __name__ == "__main__":
    main()
