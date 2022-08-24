from odoo import api,fields,models,tools

class Bureaux(models.Model):
    _name = 'bureaux.dedouan'
    _rec_name = 'bureaux_dedouan'
    bureaux_dedouan = fields.Selection(
         [
            ('11  - TANGER MED','11  - TANGER MED'),
            ('100 - AGADIR','100 - AGADIR'),
            ('100 - AGADIR VILLE','100 - AGADIR VILLE'),
            ('101 - LAAYOUNE','101 - LAAYOUNE'),
            ('104 - DAKHLA','104 - DAKHLA'),
            ('200 - SAFI','200 - SAFI'),
            ('203 - OUARZAZATE','203 - OUARZAZATE'),
            ('300 - CASA EXTERIEUR','300 - CASA EXTERIEUR'),
            ('301 - CASA NOUASSER','301 - CASA NOUASSER'),
            ('302 - CASA MOHAMMADIA','302 - CASA MOHAMMADIA'),
            ('304 - CASA COLIS POSTAU','304 - CASA COLIS POSTAU'),
            ('305 - JORF LASFAR','305 - JORF LASFAR'),
            ('309 - CASA PORT','309 - CASA PORT'),
            ('400 - TANGER PORT','400 - TANGER PORT'),
            ('401 - TANGER VILLE','401 - TANGER VILLE'),
            ('403 - KENITRA ZONE FRANCHE','403 - KENITRA ZONE FRANCHE'),
            ('404 - RABAT AEROPORT','404 - RABAT AEROPORT'),
            ('407 - TETOUAN','407 - TETOUAN'),
            ('411 - TANGER IvIED','411 - TANGER IvIED'),
            ('412 - TANGER IBN BATOUTA','412 - TANGER IBN BATOUTA'),
            ('501 - EL HOUSSIEMA','501 - EL HOUSSIEMA'),
            ('602 - NADOR(602)','602 - NADOR(602)'),
            ('607 - NADOR PORT','607 - NADOR PORT')
         ],string="Bureau de dédouanement"
     )

    burea_destinataire = fields.Selection([
        ("100 - AGADIR", "100 - AGADIR"),
        ("100 - AGADIR VILLE", "100 - AGADIR VILLE"),
        ("101 - LAAYOUNE", "101 - LAAYOUNE"),
        ("104 - DAKHLA", "104 - DAKHLA"),
        ("200 - SAFI", "200 - SAFI"),
        ("203 - OUARZAZATE", "203 - OUARZAZATE"),
        ("300 - CASA EXTERIEUR", "300 - CASA EXTERIEUR"),
        ("301 - CASA NOUASSER", "301 - CASA NOUASSER"),
        ("302 - CASA MOHAMMADIA", "302 - CASA MOHAMMADIA"),
        ("304 - CASA COLIS POSTAU", "304 - CASA COLIS POSTAU"),
        ("305 -JORF LASFAR", "305 -JORF LASFAR"),
        ("309 - CASA PORT", "309 - CASA PORT"),
        ("400 - TANGER PORT", "400 - TANGER PORT"),
        ("401 - TANGER VILLE", "401 - TANGER VILLE"),
        ("403 - KENITRA ZONE FRANCHE", "403 - KENITRA ZONE FRANCHE"),
        ("404 - RABAT AEROPORT", "404 - RABAT AEROPORT"),
        ("407 - TETOUAN", "407 - TETOUAN"),
        ("411 - TANGER MED", "411 - TANGER MED"),
        ("412 - TANGER IBN BATOUTA", "412 - TANGER IBN BATOUTA"),
        ("501- EL HOUSSIEMA", "501- EL HOUSSIEMA"),
        ("602- NADOR(602)", "602- NADOR(602)"),
        ("607 - NADOR PORT", "607 - NADOR PORT")
    ], string="Bureau de Déstination"
    )