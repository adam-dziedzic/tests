from enum import Enum


class EnumWithNames(Enum):
    @classmethod
    def get_names(cls):
        return [enum_value.name for enum_value in cls]

    @staticmethod
    def get_names_static():
        return [enum_value.name for enum_value in EnumWithNames]


class Model(EnumWithNames):
    RESNET = 0
    DENSENET = 1
    ALEXNET = 2


def run():
    print("model names: ", Model.get_names())


if __name__ == "__main__":
    run()