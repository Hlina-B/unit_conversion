from enum import Enum, unique
from decimal import Decimal

@unique
class SIPrefix(Enum):
    YOTTA = pow(10, 24)
    ZETTA = pow(10, 21)
    EXA = pow(10, 18)
    PETA = pow(10, 15)
    TERA = pow(10, 12)
    GIGA = pow(10, 9)
    MEGA = pow(10, 6)
    KILO = pow(10, 3)
    HECTO = pow(10, 2)
    DECA = 10
    UNIT = 1
    DECI = pow(10, -1)
    CENTI = pow(10, -2)
    MILLI = pow(10, -3)
    MICRO = pow(10, -6)
    NANO = pow(10, -9)
    PICO = pow(10, -12)
    FEMTO = pow(10, -15)
    ATTO = pow(10, -18)
    ZEPTO = pow(10, -21)
    YOCTO = pow(10, -24)

@unique
class Length(Enum):
    KILOMETER = (Decimal(1/SIPrefix.KILO.value), "km")
    METER = (Decimal(SIPrefix.UNIT.value), "m")
    CENTIMETER = (Decimal(1/SIPrefix.CENTI.value), "cm")
    MILLIMETER = (Decimal(1/SIPrefix.MILLI.value), "mm")
    MICROMETER = (Decimal(1/SIPrefix.MICRO.value), "um")
    NANOMETER = (Decimal(1/SIPrefix.NANO.value), "nm")
    MILE = (Decimal(0.000621371), "mi")
    YARD = (Decimal(1.09361), "yd")
    FOOT = (Decimal(3.28084), "ft")
    INCH = (Decimal(39.3701), "ft")
    NAUTICALEMILE = (Decimal(0.000539957), "nmi")

@unique
class Area(Enum):
    SQUAREKILOMETER = (Decimal(1/SIPrefix.MEGA.value), "km^2")
    SQUAREMETER = (Decimal(SIPrefix.UNIT.value), "m^2")
    SQUAREMILE = (Decimal((3.861) * pow(10, -7)), "mi^2")
    SQUAREYARD = (Decimal(1.19599), "yd^2")
    SQUAREFOOT = (Decimal(10.7639), "ft^2")
    SQUAREINCH = (Decimal(1550), "in^2")
    HECTARE = (Decimal(pow(10, -4)), "ha")
    ACRE = (Decimal(0.000247105), "ac")

@unique
class DataTransferRate(Enum):
    BITPERSECOND = (Decimal(SIPrefix.UNIT.value), "bps")
    KILOBITPERSECOND = (Decimal(0.001), "kbps")
    KILOBYTEPERSECOND = (Decimal(0.000125), "KBps")
    # KIBIBITEPERSECOND = 7812.5 -> kibps
    MEGABITPERSECOND = (Decimal(1/SIPrefix.MEGA.value), "Mbps")
    MEGABYTEPERSECOND = (Decimal((1.25 * pow(10, -7))), "MBps")
    # MEBIBITPERSECOND = ""->  Mibps
    GIGABITPERSECOND = (Decimal(1/SIPrefix.GIGA.value), "GBps")
    GIGABYTEPERSECOND = (Decimal(1/(1.25*pow(10, -10))), "GBps")
    # GIBIBITPERSECOND = ""-> Gibps
    TERABITPERSECOND = (Decimal(1/SIPrefix.TERA.value), "Tbps")
    TERABYTEPERSECOND = (Decimal(1.25 * pow(10, -13)), "TBps")
    # TEBIBITPERSECOND = ""-> Tibps

@unique
class DigitalStorage(Enum):
    BIT = (Decimal(8), "b")
    KILOBIT = (Decimal(0.008), "kb")
    # KIBIBIT = "Kibibit"-> kib
    MEGABIT = (Decimal(8 * (1/SIPrefix.MEGA.value)), "Mb")
    # MEBIBIT = "Mebibit"-> Mib
    GIGABIT = (Decimal(8 * (1/SIPrefix.GIGA.value)), "Gb")
    # GIBIBIT = "Gibibit"-> Gib
    TERABIT = (Decimal(8 * (1/SIPrefix.TERA.value)), "Tb")
    # TEBIBIT = "Tebibit"-> Tib
    PETABIT = (Decimal(8 * (1/SIPrefix.PETA.value)), "Pb")
    BYTE = (Decimal(SIPrefix.UNIT.value), "B")
    # PEBIBIT = "Pebibit"-> Pib
    KILOBYTE = (Decimal(1/SIPrefix.KILO.value), "KB")
    # KIBIBYTE = "Kibibyte"-> KiB
    MEGABYTE = (Decimal(1/SIPrefix.MEGA.value), "MB")
    # MEBIBYTE = "Mebibyte"-> MiB
    GIGABYTE = (Decimal(1/SIPrefix.GIGA.value), "GB")
    # GIBIBYTE = "Gibibyte"-> GiB
    TERABYTE = (Decimal(1/SIPrefix.TERA.value), "TB")
    # TEBIBYTE = "Tebibyte"-> TiB
    PETABYTE = (Decimal(1/SIPrefix.PETA.value), "PB")
    # PEBIBYTE = "Pebibyte"-> PiB

@unique
class Energy(Enum):
    JOULE = (Decimal(SIPrefix.UNIT.value), "J")
    kILOJOULE = (Decimal(1/SIPrefix.KILO.value), "kJ")
    GRAMCALORIE = (Decimal(0.239006), "cal")
    KILOCALORIE = (Decimal(0.000239006), "kcal")
    WATTHOUR = (Decimal(0.000277778), "wh")
    KILOWATTHOUR = (Decimal(2.7778 * pow(10, -7)), "kWh")
    ELECTRONVOLT = (Decimal(6.242 * SIPrefix.EXA.value), "eV")
    BRITISHTHERMALUNIT = (Decimal(0.000947817), "BTU")
    USTHERM = (Decimal(9.4804 * SIPrefix.NANO.value), "Therm")
    FOOTPOUND = (Decimal(0.737562), "ft.lb")

@unique
class Frequency(Enum):
    HERTZ = (Decimal(SIPrefix.UNIT.value), "Hz")
    KILOHERTZ = (Decimal(1/SIPrefix.KILO.value), "kHz")
    MEGAHERTZ = (Decimal(1/SIPrefix.MEGA.value), "MHz")
    GIGAHERTZ = (Decimal(1/SIPrefix.GIGA.value), "GHz")

@unique
class FuelEconomy(Enum):
    MILESPERGALLON = (Decimal(2.35215), "mpg")
    MILESPERGALLONIMPERIAL = (Decimal(2.82481), "Imp")
    KILOMETERPERLITER = (Decimal(SIPrefix.UNIT.value), "km/L")
    LITERPERHUNDREDKILOMETER = (Decimal(100), "L/100km")

@unique
class Mass(Enum):
    METRICTON = (Decimal(0.001), "tonne")
    KILOGRAM = (Decimal(SIPrefix.UNIT.value), "kg")
    GRAM = (Decimal(1/SIPrefix.KILO.value), "g")
    MILLIGRAM = (Decimal(SIPrefix.KILO.value * (1/SIPrefix.MILLI.value)), "mg")
    MICROGRAM = (Decimal(SIPrefix.KILO.value * (1/SIPrefix.MICRO.value)), "mcg")
    IMPERIALTON = (Decimal(0.000984207), "ton")
    USTON = (Decimal(0.00110231), "short ton")
    STONE = (Decimal(0.157473), "st")
    POUND = (Decimal(2.20462), "lb")
    OUNCE = (Decimal(35.274), "oz")

@unique
class PlaneAngle(Enum):
    ARCSECOND = (Decimal(206265), "or\"")
    DEGREE = (Decimal(57.2958), "deg")
    GRADIAN = (Decimal(63.662), "grad")
    MILLIRADIAN = (Decimal(1/SIPrefix.MILLI.value), "mrad")
    MINUTEOFARC = (Decimal(3437.75), "or'")
    RADIAN = (Decimal(SIPrefix.UNIT.value), "rad")

@unique
class Pressure(Enum):
    BAR = (Decimal(pow(10, -5)), "bar")
    PASCAL = (Decimal(SIPrefix.UNIT.value), "Pa")
    POUNDFORCEPERSQUAREINCH = (Decimal(0.000145038), "psi")
    STANDARDATMOSPHERE = (Decimal(9.8692 * SIPrefix.MICRO.value), "atm")
    TORR = (Decimal(0.00750062), "Torr")

@unique
class Speed(Enum):
    MILEPERHOUR = (Decimal(2.23694), "mps")
    FOOTPERHOUR = (Decimal(3.28084), "fph")
    METERPERSECOND = (Decimal(SIPrefix.UNIT.value), "m/s")
    KILOMETERPERHOUR = (Decimal(3.6), "km/h")
    KNOT = (Decimal(1.94384), "kn")

@unique
class Temperature(Enum):
    DEGREECELSIUS = (Decimal(-273.15), "°C")
    FAHRENHEIT = (Decimal(-459.67), "°F")
    KELVIN = (Decimal(0), "K")

@unique
class TimeM(Enum):
    NANOSECOND = (Decimal(1/SIPrefix.NANO.value), "ns")
    MICROSECOND = (Decimal(1/SIPrefix.MICRO.value), "us")
    SECOND = (Decimal(SIPrefix.UNIT.value), "sec")
    MINUTE = (Decimal(0.0166667), "min")
    HOUR = (Decimal(0.000277778), "h")
    DAY = (Decimal(1.1574 * pow(10, -5)), "d")
    WEEK = (Decimal(1.6534 * SIPrefix.MICRO.value), "wk")
    MONTH = (Decimal(3.8052 * pow(10,-7)), "mo")
    CALENDARYEAR = (Decimal(3.171 * pow(10, -8)), "cyr")
    DECADE = (Decimal(3.171 * SIPrefix.NANO.value), "d")
    CENTURY = (Decimal(3.171 * pow(10, -10)), "c")

@unique
class Volume(Enum):
    USLIQUIDGALLON = (Decimal(264.172), "gal")
    USLIQUIDQUART = (Decimal(1056.69), "qt")
    USLIQUIDPINT = (Decimal(2113.38), "pt")
    USLEGALCUP = (Decimal(4166.67), "c")
    USFLUIDOUNCE = (Decimal(33814), "fl oz")
    USTABLESPOON = (Decimal(67628), "tbsp")
    USTEASPOON = (Decimal(202884), "tsp")
    CUBICMETER = (Decimal(SIPrefix.UNIT.value), "m^3")
    LITER = (Decimal(SIPrefix.KILO.value), "l")
    MILLILITER = (Decimal(SIPrefix.MEGA.value), "ml")
    IMPERIALGALLON = (Decimal(219.969), "imp gal")
    IMPERIALQUART = (Decimal(879.877), "imp qt")
    IMPERIALPINT = (Decimal(1759.75), "imp pt")
    IMERIALCUP = (Decimal(3519.51), "imp c")
    IMPERIALFLUIDOUNCE = (Decimal(35195.1), "imp fl oz")
    IMPERIALTABLESPOON = (Decimal(56312.1), "imp tbsp")
    IMPERIALTEASPOON = (Decimal(168936), "impe tsp")
    CUBICFOOT = (Decimal(35.3147), "ft^3")
    CUBICINCH = (Decimal(61023.7), "in^3")

@unique
class BaseUnits(Enum):
    LENGTH = Length
    AREA = Area
    DATATRANSFERRATE = DataTransferRate
    DIGITALSTORAGE = DigitalStorage
    ENERGY = Energy
    FREQUENCE = Frequency
    FUELECONOMY = FuelEconomy
    MASS = Mass
    PLANEANGLE = PlaneAngle
    PRESSURE = Pressure
    SPEED = Speed
    TEMPERATURE = Temperature
    TIME = TimeM
    VOLUME = Volume
