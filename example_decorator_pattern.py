class Component():
    def operation(self) -> str:
        pass


class ConcreteComponent(Component):
    def operation(self) -> str:
        return "ConcreteComponent"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    @property
    def component(self) -> Component:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self.component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self.component.operation()})"


def print_component(component: Component) -> None:
    print(f"RESULT: {component.operation()}")


def main():
    simple_component = ConcreteComponent()
    decorator1 = ConcreteDecoratorA(simple_component)
    decorator2 = ConcreteDecoratorB(decorator1)
    decorator3 = ConcreteDecoratorA(decorator2)

    print("\nClient: I've got a simple component:")
    print_component(simple_component)
    print()

    #print("Client: Now I've got a decorated component:")
    # print_component(decorator1)
    # print_component(decorator2)
    # print_component(decorator3)
    print()


if __name__ == "__main__":

    main()
