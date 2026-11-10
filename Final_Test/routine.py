"""
De cada Routine se guardara un title, su duration y la cantidad de exercises.
"""


class Routine:
    def __init__(self, title: str, duration: int, exercises: int) -> None:
        self.__title = title
        self.__duration = duration
        self.__exercises = exercises

    def getTitle(self):
        return self.__title

    def getDuration(self):
        return self.__duration

    def getExercises(self):
        return self.__exercises

    def setTitle(self, newValue):
        self.__title = newValue

    def setDuration(self, newValue):
        self.__duration = newValue

    def setExercises(self, newValue):
        self.__exercises = newValue

    # toString()
    def __str__(self) -> str:
        return f"Rutina {self.__title} duracion de {self.__duration} minutos y {self.__exercises} ejercicios "
