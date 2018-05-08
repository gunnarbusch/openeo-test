from marshmallow import Schema, fields

class UserSchema(Schema):
    username    = fields.Str(required=True)
    email       = fields.Str(required=True)
    project     = fields.Str(required=True)
