from odoo import api,fields,models,tools,_

class Transport(models.Model):
    _name = 'transport.control'
    _description = 'transport selection'

    mode_transport = fields.Selection([
            ('Routière\Maritime', 'Routière\Maritime'),
            ('Routière', 'Routière'),
            ('Aérrienne', 'Aérrienne')
        ], string="Mode de Transport")

    # Routière
    type_route = fields.Selection([
            ('Camion.', 'Camion'),
            ('Remorque', 'Remorque'),
            ('Remorque caisse mobile', 'Remorque caisse mobile'),
            ('Ensemble Routière', 'Ensemble Routière'),
            ('Ensemble Routière mobile', 'Ensemble Routière mobile'),
            ('Contenair', 'Contenair'),
            ('Semi Contenair', 'Semi Contenair'),
        ], string="type de transport")

    # Routière\Maritime
    type_transport_route_martime = fields.Selection([
        ('Camion.', 'Camion'),
        ('Remorque', 'Remorque'),
        ('Remorque caisse mobile', 'Remorque caisse mobile'),
        ('Ensemble Routière', 'Ensemble Routière'),
        ('Ensemble Routière mobile', 'Ensemble Routière mobile'),
        ('Contenair', 'Contenair'),
        ('Semi Contenair', 'Semi Contenair'),
    ], string="type de transport")

    # Aérrienne
    type_transport_plain = fields.Selection([
        ('H.C.', 'H.C.'),
        ('R.freight', 'R.freight'),
        ('Charter', 'Charter'),
    ], string="type de transport")


