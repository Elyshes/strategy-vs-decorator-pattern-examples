# base component interface that can be altered by decorators
class Burger():
    def description(self) -> str:
        pass


# concrete component provides default implementation
class PlainBurger(Burger):
    def description(self) -> str:
        return "Burger with"


# base decorator implements the same component interface and
# defines the wrapping interface for all concrete decorators
class ToppingDecorator(Burger):
    _component: Burger = None

    def __init__(self, component: Burger) -> None:
        self._component = component

    def component(self) -> Burger:
        return self._component

    def description(self) -> str:
        return self._component.description()


# concrete decorator
class BeefPatty(ToppingDecorator):
    def description(self) -> str:
        return f"{super().description()}, beef patty"


# concrete decorator
class Salad(ToppingDecorator):
    def description(self) -> str:
        return f"{super().description()}, salad"


# concrete decorator
class Tomatoes(ToppingDecorator):
    def description(self) -> str:
        return f"{super().description()}, tomatoes"


# concrete decorator
class BarbecueSauce(ToppingDecorator):
    def description(self) -> str:
        return f"{super().description()}, barbecue sauce"


# concrete decorator
class Cheddar(ToppingDecorator):
    def description(self) -> str:
        return f"{super().description()}, cheddar"


# concrete decorator
class Bacon(ToppingDecorator):
    def description(self) -> str:
        return f"{super().description()}, bacon"


# concrete decorator
class Onions(ToppingDecorator):
    def description(self) -> str:
        return f"{super().description()}, onions"


def print_order(component: Burger) -> None:
    print(f"\nYOUR ORDER: {component.description()}\n")


def main():
    Burger = PlainBurger()
    Burger = BeefPatty(Burger)
    Burger = BarbecueSauce(Burger)
    Burger = Tomatoes(Burger)
    Burger = Salad(Burger)
    Burger = Bacon(Burger)
    Burger = Onions(Burger)
    Burger = Cheddar(Burger)

    print_order(Burger)


if __name__ == "__main__":
    main()
