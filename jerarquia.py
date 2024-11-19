from abc import ABC, abstractmethod

class Vehiculo(ABC):
    def __init__(self, marca, modelo, año, color):
        self.__marca = marca
        self.__modelo = modelo
        self.__año = año
        self.__color = color

    # Métodos getter y setter para encapsular los atributos
    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, valor):
        self.__marca = valor

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, valor):
        self.__modelo = valor

    @property
    def año(self):
        return self.__año

    @año.setter
    def año(self, valor):
        self.__año = valor

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, valor):
        self.__color = valor

    # Método abstracto para obtener el tipo de vehículo (se implementará en las subclases)
    @abstractmethod
    def tipo_vehiculo(self):
        pass

    def __str__(self):
        return f"{self.marca} {self.modelo}, {self.año}, {self.color}"
    

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, año, color, tipo_automovil):
        super().__init__(marca, modelo, año, color)
        self.__tipo_automovil = tipo_automovil  # SUV o Sedan

    @property
    def tipo_automovil(self):
        return self.__tipo_automovil

    @tipo_automovil.setter
    def tipo_automovil(self, valor):
        self.__tipo_automovil = valor

    def tipo_vehiculo(self):
        return f"Automóvil tipo {self.tipo_automovil}"

    def __str__(self):
        return f"{super().__str__()} ({self.tipo_vehiculo()})"



class SUV(Automovil):
    def __init__(self, marca, modelo, año, color, tipo_automovil, capacidad_carga):
        super().__init__(marca, modelo, año, color, tipo_automovil)
        self.__capacidad_carga = capacidad_carga  # Capacidad de carga en kg

    @property
    def capacidad_carga(self):
        return self.__capacidad_carga

    @capacidad_carga.setter
    def capacidad_carga(self, valor):
        self.__capacidad_carga = valor

    def tipo_vehiculo(self):
        return f"SUV, capacidad de carga: {self.capacidad_carga} kg"

    def __str__(self):
        return f"{super().__str__()} ({self.tipo_vehiculo()})"


class Sedan(Automovil):
    def __init__(self, marca, modelo, año, color, tipo_automovil, numero_puertas):
        super().__init__(marca, modelo, año, color, tipo_automovil)
        self.__numero_puertas = numero_puertas  # Número de puertas

    @property
    def numero_puertas(self):
        return self.__numero_puertas

    @numero_puertas.setter
    def numero_puertas(self, valor):
        self.__numero_puertas = valor

    def tipo_vehiculo(self):
        return f"Sedán, número de puertas: {self.numero_puertas}"

    def __str__(self):
        return f"{super().__str__()} ({self.tipo_vehiculo()})"



class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, color, carga_maxima):
        super().__init__(marca, modelo, año, color)
        self.__carga_maxima = carga_maxima  # Carga máxima en kg

    @property
    def carga_maxima(self):
        return self.__carga_maxima

    @carga_maxima.setter
    def carga_maxima(self, valor):
        self.__carga_maxima = valor

    def tipo_vehiculo(self):
        return f"Camión, carga máxima: {self.carga_maxima} kg"

    def __str__(self):
        return f"{super().__str__()} ({self.tipo_vehiculo()})"
    



class Motocicleta(Vehiculo):
    def __init__(self, marca, modelo, año, color, cilindrada):
        super().__init__(marca, modelo, año, color)
        self.__cilindrada = cilindrada  # Cilindrada en cc

    @property
    def cilindrada(self):
        return self.__cilindrada

    @cilindrada.setter
    def cilindrada(self, valor):
        self.__cilindrada = valor

    def tipo_vehiculo(self):
        return f"Motocicleta, cilindrada: {self.cilindrada} cc"

    def __str__(self):
        return f"{super().__str__()} ({self.tipo_vehiculo()})"

