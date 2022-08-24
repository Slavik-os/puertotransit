# ------------------------------------------------------------------------
# Puerto transit odoo :  1.0v
# File Description    :  Create folder for Dedouane
#
# ------------------------------------------------------------------------
from odoo import api,fields,models,tools,_
from odoo.exceptions import ValidationError

class FolderManagment(models.Model):
    _name ="folder.managment"
    _inherit = ['mail.thread','mail.activity.mixin']
    _description = "Folder managment for puerto transit"
    _rec_name = "n_serie"
    created_date = fields.Date(string='Created Date',
                              default=lambda self:fields.Date.context_today(self).replace(day=8,month=5,year=2022),readonly=True)
    folder_type = fields.Selection([('proviesior','Provisionnelle'),
                                    ('difinitive','Definitive')],default='proviesior',
                                   string="Type de dossier",tracking=True)

    #Priority
    priority = fields.Selection([
        ('0','Normal'),
        ('1','Low'),
        ('2', 'High'),
        ('3', 'Very High')],string="Priority",default='0',
        help="Set the priority status of the appointment"
    )
    #Status Bar
    state = fields.Selection([
        ('draft', 'Draft'),
        ('in_consultation', 'In consultaion'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')],default='draft',required=True, string="Status",
        help="Set the sate status of the appointment"
    )

    #Overide the delete function :
    def unlink(self):
        for folder in self:
            # delete if difinitive
            if folder.folder_type !='difinitive':
                super(FolderManagment, folder).unlink()
            else:
                super(FolderManagment, folder).unlink()
                raise ValidationError(_("Cant delete when permanent"))
                pass

    #Overide the edite function :
    def write(self,vals):
        # write not difinitive
        if self.folder_type != 'difinitive':
            res = super(FolderManagment, self).write(vals)
            print("Can delete !!!!!")
        else :
            res = super(FolderManagment, self).write(vals)
            raise ValidationError(_("Cant Edit !"))
        return res

    # Dum
    _n_dum = fields.Many2one('dum.number', string="N °Dum",tracking=True)
    n_dum  = fields.Selection(related="_n_dum.ndum",readonly=False,tracking=True)
    dum_start_date = fields.Date(string="Date Dum",tracking=True)
    dum_end_date = fields.Date(string="Date Fin",tracking=True)

    # Expiditeur
    _expiditeur = fields.Many2one('expiditeur.select', string="Expiditeur",tracking=True)
    destinataire = fields.Selection(related="_expiditeur.name",
                                  string="Déstinataire",readonly=False,tracking=True)


    # Serie number
    n_serie = fields.Char(string="N°Serie",tracking=True)

    # Bureaux dedouan
    _bureax_dedouane = fields.Many2one('bureaux.dedouan',tracking=True)
    bureax_dedouane = fields.Selection(related='_bureax_dedouane.bureaux_dedouan',
                                       string='Bureau de dédouanement',readonly=False,tracking=True)

    # Arrondissement
    arrondissement = fields.Selection(
        [('411 - TANGER MED', '411 - TANGER MED'),
         ('411001 - MAED MARCOTRAN MAROC', '411001 - MAED MARCOTRAN MAROC'),
         ('411002 - TANGER MED IMPORT', '411002 - TANGER MED IMPORT'),
         ('411003 - TANGER MED EXPORT', '411003 - TANGER MED EXPORT'),
         ('411005 -ZF TAC', '411005 -ZF TAC'),
         ('411006 -ZF TANGER MED (MEDHUB)', '411006 -ZF TANGER MED (MEDHUB)'),
         ('411007 -ZF MELLOUSSA RENAULT', '411007 -ZF MELLOUSSA RENAULT')
         ], string="arrondissement",tracking=True
    )

    # Regime
    regime = fields.Selection(
        [
            ("000 - MAIN LEVEE", "000 - MAIN LEVEE"),
            ("001 - ETAT DE CHARGEMENT", "001 - ETAT DE CHARGEMENT"),
            ("002 - RETOUR", "002 - RETOUR"),
            ("003- TRANSIT INTERIEURE MARITIME", "003- TRANSIT INTERIEURE MARITIME"),
            ("007 - CONSIGNATION TRANSPORT EXPORT", "007 - CONSIGNATION TRANSPORT EXPORT"),
            ("052 - RIEMPORTATION EN SUITE ET", "052 - RIEMPORTATION EN SUITE ET"),
            ("060 - EXPORTATION SIMPLE", "060 - EXPORTATION SIMPLE"),
            ("061 - EXPORTATION DANS LE CADRE DU SGP", "061 - EXPORTATION DANS LE CADRE DU SGP"),
            ("70 - EXPORT EN SUITE D'ATPA AVEC P", "70 - EXPORT EN SUITE D'ATPA AVEC P"),
            ("72- EXPORT EN SUITE D'ATPA SANS PA", "72- EXPORT EN SUITE D'ATPA SANS PA"),
            ("74 - EXPORT EN SUITE D'AT", "74 - EXPORT EN SUITE D'AT"),
            ("75- EXPORT EN SUIT DE OPP", "75- EXPORT EN SUIT DE OPP"),
            ("77-ETPP", "77-ETPP"),
            ("78-EXPORTATION TEMPORAIRE", "78-EXPORTATION TEMPORAIRE"),
            ("111 - PROV", "111 - PROV"),
            ("231- ATPA SANS PAIEMENT A PARTIR ZF", "231- ATPA SANS PAIEMENT A PARTIR ZF"),
            ("680-EXPORT DEFINITIVE EN REGULARISATION D ETP", "680-EXPORT DEFINITIVE EN REGULARISATION D ETP"),
            ("681-EXPORTATION DIFINITIVE EN REGU", "681-EXPORTATION DIFINITIVE EN REGU"),
            ("682-EXPORTATION VERS L'ETRANGER EN SUITE D'D", "682-EXPORTATION VERS L'ETRANGER EN SUITE D'D"),
            ("751 - EXPORT SUITE EIF", "751 - EXPORT SUITE EIF"),
            ("761 - EXPORT SIMPLE VERS ZONE FRANCH", "761 - EXPORT SIMPLE VERS ZONE FRANCH"),
            ("762-EXPORT SUITE D'ATPA VERS ZONE", "762-EXPORT SUITE D'ATPA VERS ZONE"),
            ("763-EXPORTATION EN SUIT DAT VERS LES ZONES FF", "763-EXPORTATION EN SUIT DAT VERS LES ZONES FF"),
            ("763- EXPORTATION EN SUITE AT VERS FZ", "763- EXPORTATION EN SUITE AT VERS FZ"),
            ("764 - EXPORT SUITE EPP VERS LA ZONE", "764 - EXPORT SUITE EPP VERS LA ZONE"),
            ("765- EXPORT TEMP VERS ZONE FRANCHE", "765- EXPORT TEMP VERS ZONE FRANCHE"),
            ("766 - ETPP VERS ZF", "766 - ETPP VERS ZF"),
            ("768 - Exportation suite EIF vets les", "768 - Exportation suite EIF vets les"),
            ("769 - EXPORTATION VERS LES ZONES FRANCHES LOG", "769 - EXPORTATION VERS LES ZONES FRANCHES LOG"),
            ("856 - TRANSIT ENTRE ZONE FRANCHE", "856 - TRANSIT ENTRE ZONE FRANCHE"),
            ("866 - EXPORT PARTIR DE ZF", "866 - EXPORT PARTIR DE ZF")
        ], string="Régime" ,tracking=True)

    # Bureaux destinatair  burea_destinataire
    bureaux_destinataire = fields.Selection(related='_bureax_dedouane.burea_destinataire'
                                            ,readonly=False ,tracking=True)

    # Lieu stockage
    lieu_stockage = fields.Selection([('', '')], string="lieu Stokage",tracking=True)

    # Folder number
    n_dossier = fields.Char(string="N°Dossier",tracking=True)

    # Reception Dates
    repection_datetime = fields.Datetime(string="Date de Récepetion pré-alerte",tracking=True)

    # Declaration

    declaration = fields.Selection([('normal','Normal'),
                                    ('provisionelle','Provisionelle'),
                                    ('Nouvelle Provisionelle', 'Nouvelle Provisionelle')
                                    ], string="Declaration", tracking=True)

    # Tr
    tr = fields.Selection([('oui','Oui'),('non','Non')],string="TR",tracking=True)

    # Ref Tr , placehoder for now
    referance_tr = fields.Char(string="Ref.Tr",readonly=True,tracking=True)


    # Origine
    _origin = fields.Many2one("origin.select",string="origin")
    origine = fields.Selection(related="_origin.origine_contries",
                               readonly=False,tracking=True)

    # Provenenace
    provenance = fields.Selection([
        ('CADIZ', 'CADIZ'),
        ('PEDROLA','PEDLORA'),
        ('PAMPLONA', 'PAMPLONA'),
        ('ZARAGOZA', 'ZARAROGA'),
        ('PAMPLONA&CADIZ', 'PAMPLONA&CADIZ')
    ], string="Provenance",tracking=True)

    # Mode transport
    _mode_transport = fields.Many2one('transport.control')
    mode_transport = fields.Selection(related='_mode_transport.mode_transport',readonly=False,tracking=True)

    # Type de transport
    type_transport_route = fields.Selection(related='_mode_transport.type_route',
                                            readonly=False,tracking=True)
    type_transport_route_martime = fields.Selection(related='_mode_transport.type_transport_route_martime',
                                                    readonly=False,tracking=True)
    type_transport_plain = fields.Selection(related='_mode_transport.type_transport_plain',
                                            readonly=False,tracking=True)

    # Martricule / Ref T.C
    matricule = fields.Char(string='Matricule',tracking=True)
    ref_tc = fields.Char(string='Ref.Tr',tracking=True)

    # Plain transport type
    ref_depot = fields.Char(string="Réf Dépôt")
    HAWB_LTA = fields.Char(string="HAWB/LTA")
    ref_lta = fields.Char(string="Réf LTA")
    bateau = fields.Char(string="Bateau")

    # Tye DS
    type_ds = fields.Selection([
        ("01 : Declaration sommaire", "01 : Declaration sommaire"),
        ("03: DS MEAD", "03: DS MEAD"),
        ("04 : EPCST", "04 : EPCST"),
        ("05 : Bat de Dopotage", "05 : Bat de Dopotage"),
        ("06 : Eclatement titre de transport", "06 : Eclatement titre de transport"),
        ("07 : PEC de camel TIR", "07 : PEC de camel TIR")],string="Type Ds",tracking=True)

    # Compagine
    _compagine= fields.Many2one("compagine",string="Compagine")
    compagine = fields.Selection(related="_compagine.compagine_list",
                                 string="Compagine",readonly=False,tracking=True)


    # Ref compagine
    ref_compagine = fields.Char(string="Ref.Compagine",tracking=True)

    #Date of travel
    datetime_travel = fields.Datetime(string="Date de voyage",tracking=True)

    #Transporter
    _transporteur = fields.Many2one('transporter')
    transporteur = fields.Selection(related="_transporteur.transporter_list",
                                    string="Transporteur",readonly=False,tracking=True)

    #Ref client
    ref_client= fields.Char(string="Ref.Client",readonly=True)

    #N° Connaissement
    connaissement_number = fields.Char(string="N°Connaissement",tracking=True)

    #Transitaire
    _transitaire = fields.Many2one("transitaire")
    transitaire = fields.Selection(related="_transitaire.transitaire",
                                   string="Transitaire",readonly=False,tracking=True)
    #Ref transitaire
    ref_transitaire = fields.Char(string="Ref.Transitaire",tracking=True)

    #Poids Brut
    proids_brut = fields.Float(string="Poids Brut",tracking=True)

    #Nbr Colis
    number_colis = fields.Integer(string="Numbre Colis",tracking=True)


    #Designation Marchandise
    designation_marchandise = fields.Char(string="Designation Marchandise",tracking=True)

    #Expiditeur
    expiditeur = fields.Selection(related="_expiditeur.name",
                                   readonly=False, tracking=True)

    #Observation
    observation = fields.Text(string="observation",tracking=True,trim=True)



    #N Scelle Douane

    active_scelle_douane = fields.Boolean(default=False,string="",tracking=True)
    N_scelle_douane = fields.Char(string="N°Scelle Douane",tracking=True)

    #N Scelle Client
    active_scelle_client = fields.Boolean(default=False,string="",tracking=True)
    N_scelle_client = fields.Char(string="N°Scelle Client",tracking=True)

    #N Chasse
    n_chasse = fields.Char(string="N°CHASSE",tracking=True)

    #CADNA
    cadna = fields.Char(string="CADNA",tracking=True)

    #Demand Traction
    active_demond_traction = fields.Boolean(default=False,string="",tracking=True)
    demond_traction = fields.Datetime(string="Demande Traction",tracking=True)

    #Motif de traction
    motif_traction = fields.Char(string="Motif de traction",tracking=True)



    #Upload (attach une piece)
    upload_files_ids = fields.One2many('pieceattach.control','n_serie_id',string="Attacher une piece",tracking=True)

class PieceAttachControll(models.Model):
    _name ="pieceattach.control"
    _description =  "Attach des peice managment "
    upload = fields.Binary(string="attach une piece")
    file_name_upload = fields.Char(string="File name")
    n_serie_id = fields.Many2one("folder.managment",string="Numero serie")
    comment = fields.Text(string="Commentaire")














