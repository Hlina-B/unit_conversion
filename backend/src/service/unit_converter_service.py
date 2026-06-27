import math

from decimal import Decimal

from model.units import Temperature
from model.models import ConversionResponse

def convert(value: Decimal, from_unit: str, to_unit: str, measurement) -> ConversionResponse: 
    if from_unit.casefold() == to_unit.casefold():
        return ConversionResponse(value, from_unit, value, to_unit)
    
    t_val, t_unit = get_value_and_unit(to_unit, measurement)
    f_val, f_unit = get_value_and_unit(from_unit, measurement)

    if measurement == Temperature:
        return convert_temprature(value, to_unit, from_unit, t_unit, f_unit)

    normalize_unit = Decimal(t_val/f_val)
    converted_value = Decimal(value*normalize_unit)

    return ConversionResponse(format_sn(value), f_unit, format_sn(converted_value), t_unit)

def convert_temprature(value: Decimal, t_unit: str, f_unit: str, tunit, funit) -> ConversionResponse:
    to_dc = value
    dc, _ = Temperature.DEGREECELSIUS.value
    if f_unit.casefold() == Temperature.KELVIN.name.casefold() or f_unit.casefold() == Temperature.FAHRENHEIT.name.casefold():   
        to_dc = Decimal(value + dc) if f_unit.casefold() == Temperature.KELVIN.name.casefold() else Decimal((value - 32) * 5/9)
        if t_unit.casefold() == Temperature.DEGREECELSIUS.name.casefold():
            return ConversionResponse(format_sn(value), funit, format_sn(to_dc), tunit)
        
   
    converted_value = Decimal(to_dc - dc) if t_unit.casefold() == Temperature.KELVIN.name.casefold() else Decimal((to_dc * 9/5) + 32)
    return ConversionResponse(format_sn(value), funit, format_sn(converted_value), tunit)


def get_value_and_unit(unit: str, measurement):
    for val in measurement:
        if unit.casefold() == val.name.casefold():
            return val.value

def format_sn(value):
    if value == 0:
        return value
    return float(round(value, 8 - int(math.floor(math.log10(abs(value)))) - 1))