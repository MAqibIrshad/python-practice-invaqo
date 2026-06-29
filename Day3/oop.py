class Animal:
    def __init__(self, animals=None, name="", habitant="", color=""):
        self.animals = animals if animals is not None else []
        self.name = name
        self._habitant = habitant
        self.color = color

    @property
    def get_animal_info(self):
        return {
            "name": self.name,
            "habitant": self._habitant,
            "color": self.color,
        }

    @get_animal_info.setter
    def get_animal_info(self, values: dict):
        self.name = values.get("name", self.name)
        self._habitant = values.get("habitant", self._habitant)
        self.color = values.get("color", self.color)

    @property
    def get_animals(self):
        return self.animals

    @get_animals.setter
    def get_animals(self, animal_data: dict):
        self.animals.append(animal_data)


class Specie(Animal):
    def __init__(
        self,
        ancestor="",
        pred_not_pred=False,
        no_of_legs=0,
        animals=None,
        name="",
        habitant="",
        color="",
    ):
        super().__init__(animals, name, habitant, color)
        self.ancestor = ancestor
        self.pred_not_pred = pred_not_pred
        self.no_of_legs = no_of_legs

    @property
    def get_animal_info(self):
        info = super().get_animal_info
        info.update({
            "ancestor": self.ancestor,
            "pred_or_not": self.pred_not_pred,
            "no_of_legs": self.no_of_legs,
        })
        return info

    @get_animal_info.setter
    def get_animal_info(self, values: dict):
        super(Specie, self.__class__).get_animal_info.fset(self, values)

        self.ancestor = values.get("ancestor", self.ancestor)
        self.pred_not_pred = values.get(
            "pred_or_not", self.pred_not_pred
        )
        self.no_of_legs = values.get(
            "no_of_legs", self.no_of_legs
        )

