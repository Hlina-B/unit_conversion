from flask import Flask, Response, request, jsonify
from flask_cors import CORS

from decimal import Decimal
import re
from model.models import Parameters
from model.units import BaseUnits
from service.unit_converter_service import convert

app = Flask(__name__)
app.json.ensure_ascii = False
CORS(app)

@app.route('/convert', methods=['GET'])
def _convert():
    validated = extract_and_validate(request)
    if isinstance(validated, Response):
        return validated
    
    value, from_unit, to_unit, base_unit = validated
    result = convert(value, from_unit, to_unit, base_unit)
    return jsonify(result), 200

def extract_and_validate(req) -> tuple | Response:
        value = req.args.get(Parameters.VALUE.value)
        from_unit = req.args.get(Parameters.FROM_UNIT.value)
        to_unit = req.args.get(Parameters.TO_UNIT.value)
        base_unit = req.args.get(Parameters.BASE_UNIT.value)
        measurement = next((b_unit.value for b_unit in BaseUnits if base_unit.casefold() == b_unit.name.casefold()), None)
        NUMBER_PATTERN = re.compile(r"^-?\d+(\.\d+)?$")

        if measurement is None:
            return jsonify({"Message": "Provided 'base unit' is not valid."}, 400)

        if value is None or len(value.strip()) == 0 or not NUMBER_PATTERN.match(value.strip()):
            return jsonify({"Message": "Provided 'value' is not valid."}, 400)
        
        if not any((True for unit in measurement if from_unit.casefold() == unit.name.casefold())):
            return jsonify({"Message": "The unit to convert 'from' must be valid"}, 400)
        
        if not any((True for unit in measurement if to_unit.casefold() == unit.name.casefold())):
            return jsonify({"Message": "The unit to convert 'to' must be valid"}, 400)
        
        return Decimal(value), from_unit, to_unit, measurement