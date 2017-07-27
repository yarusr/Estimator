from infi.clickhouse_orm import models, fields, engines

class Person(models.Model):

    first_name = fields.StringField()
    last_name = fields.StringField()
    birthday = fields.DateField()
    height = fields.Float32Field()

    engine = engines.MergeTree('birthday', ('first_name', 'last_name', 'birthday'))