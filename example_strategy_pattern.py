from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Context():
    """
    Der Kontext definiert das Interface für Clients.
    """

    strategy: Strategy


    def __init__(self, strategy: Strategy) -> None:
        """
        Konstruktor akzeptiert Strategie die der Kontext am anfang benutzt
        """

        self.strategy = strategy

    def setStrategy(self, strategy: Strategy) -> None:
        """
        Setter Methode um die Strategie währen der Laufzeit zu ändern.
        """

        self.strategy = strategy

    def sortList(self) -> None:
        """
        Der Kontext gibt arbeit an die Strategien weiter anstatt mehrere Versionen 
        des ähnlichen Algorithmus selbst zu implementieren.

        Er weiß dabei nicht welche Strategie bnutzt wird.
        """

        # ...

        print("Context: Sortiert Daten in dem es die Strategien nutzt.")
        result = self.strategy.execute_sort(["d", "e", "a", "c", "b"])
        print(",".join(result))

        # ...


class Strategy(ABC):
    """
    Das Strategy Interface (hier: Abstrakte Klasse) deklariert Operationen die alle
    Algorithmen gemeinsam haben.

    Der Context nutzt dieses Interface um die Algortihmen aufzurufen.
    """

    @abstractmethod
    def execute_sort(self, data: List):
        pass


"""
Die Konkreten Strategien implementieren die Algorithmen, während sie der Basis
Strategie folgen. Das Interface macht alle Strategien austauschbar.
"""


class normalSort(Strategy):
    def execute_sort(self, data: List) -> List:
        return sorted(data)


class reverseSort(Strategy):
    def execute_sort(self, data: List) -> List:
        return reversed(sorted(data))

def main():
    """
    Der Client wählt die konkrete Strategie und übergibt sie dem Kontext. 
    Der Client sollte dem Unterschied zwischen den Strategien kennen, um
    den richtigen Algorithmus zu wählen.
    """
    context = Context(normalSort())
    print("Client: Strategy is set to normal sorting.")
    context.sortList()
    print()

    print("Client: Strategy is set to reverse sorting.")
    context.setStrategy(reverseSort())
    context.sortList()


if __name__ == "__main__":
    main()