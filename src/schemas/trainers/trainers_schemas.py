from marshmallow import Schema, fields,validate

class TrainerSchema(Schema):
    id = fields.Str(required = True, validate = validate.Length(min = 5, max = 20) )
    name = fields.Str(required = True, validate = validate.Length(min = 3, max = 20) )
    region = fields.Str(required = True, validate = validate.Length(min = 4, max = 15))