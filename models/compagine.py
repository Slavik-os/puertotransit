from odoo import api,fields,models,tools,_


class Compagine(models.Model):
    _name='compagine'
    _rec_name = 'compagine_list'
    compagine_list = fields.Selection([
        ("AGTT", "AGTT"),
        ("Pi Arabia Maroc", "Pi Arabia Maroc"),
        ("ATLAS BLUE", "ATLAS BLUE"),
        ("AUTRE", "AUTRE"),
        ("BDP INTERNATIONAL", "BDP INTERNATIONAL"),
        ("CHRONOPOST", "CHRONOPOST"),
        ("DHL", "DHL"),
        ("EASY JET", "EASY JET"),
        ("EMIRATES", "EMIRATES"),
        ("EMIRATES SKY CARGO", "EMIRATES SKY CARGO"),
        ("ETIHAD", "ETIHAD"),
        ("EXPRESSWORLD", "EXPRESSWORLD"),
        ("GARLAND", "GARLAND"),
        ("HITEK LOGISTICS", "HITEK LOGISTICS"),
        ("IBERIA", "IBERIA"),
        ("MYCS", "MYCS"),
        ("PESCHAUD", "PESCHAUD"),
        ("QATAR AIRWAYS", "QATAR AIRWAYS"),
        ("RAYNAIR", "RAYNAIR"),
        ("ROYAL AIR MAROC", "ROYAL AIR MAROC"),
        ("SAUDI ARABIAN", "SAUDI ARABIAN"),
        ("SLINE", "SLINE"),
        ("SWIFTAIR", "SWIFTAIR"),
        ("TURKISH AIRLINES", "TURKISH AIRLINES"),
    ],string="Compagine")