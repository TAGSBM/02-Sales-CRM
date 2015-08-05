from openerp.osv import fields, osv
from openerp.addons.crm import crm

class tag_customer_tabs(osv.osv):

    _inherit = "res.partner"
    


    _columns = {

        'user_id_n': fields.many2one('res.users', 'Salesperson', select=True, track_visibility='always'),
        'industry': fields.many2one('industry', 'Industry', select=True),
		'firstname': fields.char('Contact Name', size=64, select=True, track_visibility='always'),
        'parent_id': fields.many2one('res.partner', 'Related Company', select=True, track_visibility='always'),
        'contact_name': fields.char('Contact Name', size=64, select=True, track_visibility='always'),
		'lastname': fields.char('Last Name', size=64, select=True, track_visibility='always'),
        'street_n': fields.char('Street', select=True, track_visibility='always'),
        'street2_n': fields.char('Street2', select=True, track_visibility='always'),
        'zip_n': fields.char('Zip', size=24, change_default=True, select=True, track_visibility='always'),
        'city_n': fields.char('City', select=True, track_visibility='always'),
        'state_id_n': fields.many2one("res.country.state", 'State', ondelete='restrict', select=True, track_visibility='always'),
        'country_id_n': fields.many2one('res.country', 'Country', ondelete='restrict', select=True, track_visibility='always'),
        'email_form': fields.char('Email', select=True, track_visibility='always'),
        'phone_num': fields.char('Phone', select=True, track_visibility='always'),
        'fax_num': fields.char('Fax', select=True, track_visibility='always'),
        'mobile_num': fields.char('Mobile', select=True, track_visibility='always'),
        'vehicle_name_n': fields.char('Vehicle', size=64, select=True, track_visibility='always'),
        'date_deadline': fields.date('Expected Closing', help="Estimate of the date on which the opportunity will be won.", select=True, track_visibility='always'),
        'date_action': fields.date('Next Action Date', select=True, track_visibility='always'),
        'priority': fields.selection(crm.AVAILABLE_PRIORITIES, 'Priority', select=True, track_visibility='always'),
        'categ_ids': fields.many2many('crm.case.categ', 'res_partner_category_rel', 'partner_id', 'category_id', 'Tags', \
            domain="['|', ('section_id', '=', section_id), ('section_id', '=', False), ('object_id.model', '=', 'crm.lead')]", select=True, track_visibility='always'),
        'title_action': fields.char('Next Action', select=True, track_visibility='always'),
        'company_currency': fields.related('company_id', 'currency_id', type='many2one', string='Currency', readonly=True, relation="res.currency"),
        'planned_revenue': fields.float('Expected Revenue', select=True, track_visibility='always'),
        'probability': fields.float('Success Rate (%)', group_operator="avg"),
        'Option1': fields.char('Data Upload ID', size=15),
		'Option2': fields.char('Option 2', size=25), 
		'Option3': fields.text('Option 3', size=50),
		'Option4': fields.text('Option 4', size=100), 
		'Option5': fields.text('Option 5', size=100), 
		'Option6': fields.text('Option 6', size=100), 
		'Option7': fields.char('ACN', size=25), 
		'Option8': fields.char('ABN', size=25),
		'Option9': fields.text('Option 9', size=100), 
		'Option10': fields.text('Option 10', size=50), 
		'Option11': fields.char('Option 11', size=100), 
		'Option12': fields.char('Website', size=50),
		'Option13': fields.char('Other 13', size=25),
		'Option14': fields.date(' Option 14'), 
		'Option15': fields.float('Option 15'), 
		'Option16': fields.char('Option 16',size=25), 
		'Option17': fields.char('Option 17', size=25), 
		'Option18': fields.char('Option 18', size=5),
		'Option19': fields.char('Option 19', size=25), 
		'Option20': fields.char('Option 20', size=25),
		'Option21': fields.char('Option 21', size=25),
		'Option22': fields.char('Option 22', size=25), 
		'Option23': fields.char('Option 23', size=25), 
		'Option24': fields.selection([('1','Choice 1'), ('2','Choice 2'), ('3','Choice 3'),('4','Choice 4')],'Option 24'),
		'Option25': fields.selection([('1','Choice 1'), ('2','Choice 2')], 'Option 25'),
		'Option26': fields.selection([('1','Choice 1'), ('2','Choice 2'),('3','Choice 3')], 'Option 26'),
		'Option27': fields.char('Option 27', size=25), 
		'Option28': fields.text('Option 28', size=200), 
		'Option29': fields.char('Option 29', size=25), 
		'Option30': fields.char('Option 30', size=25),
		'Option31': fields.char('Option 31', size=25),
		'Option32': fields.char('Option 32', size=25), 
		'Option33': fields.char('Option 33', size=25),
		'Option34': fields.char('Option 34', size=30), 
		'Option35': fields.char('Option 35', size=30),
		'Option36': fields.char('Option 36', size=25),
		'Option37': fields.char('Option 37', size=25), 
		'Option38': fields.char('Option 38', size=25), 
		'Option39': fields.char('Option 39', size=25), 
		'Option40': fields.char('Option 40', size=25), 
		'Option41': fields.char('Option 41', size=25),
		'Option42': fields.selection([('1','Choice 1'), ('2','Choice 2'), ('3','Choice 3'),('4','Choice 4')],'Option 42'), 
		'Option43': fields.selection([('1','Choice 1'), ('2','Choice 2')], 'Option 43'), 
		'Option44': fields.selection([('1','Choice 1'), ('2','Choice 2'),('3','Choice 3')], 'Option 44'), 
		'Option45': fields.char('Option 45', size=25),
		'Option46': fields.text('Option 46', size=100),
		'Option47': fields.char('Option 47', size=30), 
		'Option48': fields.char('EOption 48', size=30),
		'Option49': fields.char('Other 49', size=25), 
		'Option50': fields.char('Other 50', size=25),

	    'TagCustL1Label': fields.char('Assetts', size=1),
	    'TagCustAL1': fields.float('Cash at Bank'),
        'TagCustAL2': fields.float('Residential Property'), 
        'TagCustAL3': fields.float('Property 1'), 
        'TagCustAL4': fields.float('Property 2'), 
        'TagCustAL5': fields.float('Property 3'),
        'TagCustAL6': fields.float('Other Investments'),
	    'TagCustAL7': fields.float('Fixtures & Fittings'), 
	    'TagCustAL8': fields.float('Furniture'),
	    'TagCustAL9': fields.float('Superannuation'), 
	    'TagCustAL10': fields.float('Shares'),
	    'TagCustAL11': fields.float('Plant & Equip'),
        'TagCustAL12': fields.float('Motor Vehicle'), 
        'TagCustAL13': fields.float('Bike/Van/Boat'), 
        'TagCustAL14': fields.float('Valuables'), 
        'TagCustAL15': fields.float('Business Val'),
        'TagCustAL16': fields.float('Total Assetts'),
	    'TagCustL1Label2': fields.char('Liabilities', size=1),
	    'TagCustAL21': fields.float('Overdraught'),
        'TagCustAL22': fields.float('Residential Property'), 
        'TagCustAL23': fields.float('Property 1'), 
        'TagCustAL24': fields.float('Property 2'), 
        'TagCustAL25': fields.float('Property 3'),
        'TagCustAL26': fields.float('Other Investments'),
	    'TagCustAL27': fields.float('Fixtures & Fittings'), 
	    'TagCustAL28': fields.float('Furniture'),
	    'TagCustAL29': fields.float('Superannuation'), 
	    'TagCustAL30': fields.float('Shares'),
	    'TagCustAL31': fields.float('Plant & Equip'),
        'TagCustAL32': fields.float('Motor Vehicle'), 
        'TagCustAL33': fields.float('Bike/Van/Boat'), 
        'TagCustAL34': fields.float('Valuables'), 
        'TagCustAL35': fields.float('Business Val'),
        'TagCustAL36': fields.float('Total Liabilities'),
	    'TagDevNotesFT1':fields.text('DFT1 Notes'),
	    'TagDevNotesFT1H':fields.char('Help'),
	    'TagDevNotesFT2':fields.text('FT2 Added for comments re development of this tab area'),
	    'TagDevNotesFT3':fields.text('FT3 Added for comments re development of this tab area'),
	    'TagDevNotesFT4':fields.text('FT4 Added for comments re development of this tab area'),
	    'TagDevNotesFT5':fields.text('FT5 Added for comments re development of this tab area'),
	    'TagDevNotesLT1':fields.text('LT1 Added for comments re development of this tab area'),
	    'TagDevNotesLT2':fields.text('LT2 Added for comments re development of this tab area'),
	    'TagDevNotesLT3':fields.text('LT3 Added for comments re development of this tab area'),
	    'TagDevNotesLT4':fields.text('LT4 Added for comments re development of this tab area'),
	    'TagDevNotesLT5':fields.text('LT5 Added for comments re development of this tab area'),
	    'TagCustList01':fields.one2many('crm.lead.tag_cust_list_1', 'tag_list1_id', 'TagListA01'),
	    'TagCustList02': fields.one2many('crm.lead.tag_cust_list_2', 'tag_list2_id', 'TagListA02'),
	    'TagCustList03': fields.one2many('crm.lead.tag_cust_list_3', 'tag_list3_id', 'TagListA03'),
	    'TagCustList04': fields.one2many('crm.lead.tag_cust_list_4', 'tag_list4_id', 'TagListA04'),
	    'TagCustList05': fields.one2many('crm.lead.tag_cust_list_5', 'tag_list5_id', 'TagListA05')
    }

    _defaults = {
        'user_id': lambda s, cr, uid, c: uid,
       # 'stage_id': lambda s, cr, uid, c: s._get_default_stage_id(cr, uid, c),
       # 'section_id': lambda s, cr, uid, c: s._get_default_section_id(cr, uid, context=c),
        'priority': lambda *a: crm.AVAILABLE_PRIORITIES[2][0],
      
    }

    
class tag_cust_list_1(osv.osv):

    _name = "crm.lead.tag_cust_list_1"
    
    _columns = {
        'tag_list1_id': fields.many2one('crm.lead','Member Block Reference', required=True, readonly=True),
		'tag_list2_id': fields.many2one('crm.lead','Member Block Reference', required=True, readonly=True),
		'tag_list3_id': fields.many2one('crm.lead','Member Block Reference', required=True, readonly=True),
		'tag_list4_id': fields.many2one('crm.lead','Member Block Reference', required=True, readonly=True),
		'tag_list5_id': fields.many2one('crm.lead','Member Block Reference', required=True, readonly=True),
        'TagList101': fields.char('Name'),
        'TagList102': fields.char('Address'),
		'TagList103': fields.char('Phone'),
		'TagList104': fields.char('D.O.B'),
		'TagList105': fields.char('Lic No', size=20),
		'TagList106': fields.text('Note', size=150),
		'TagList201': fields.char('Service Date'),
        'TagList202': fields.char('Kms'),
		'TagList203': fields.char('L203'),
		'TagList204': fields.char('L204'),
		'TagList205': fields.char('L205'),
		'TagList206': fields.float('L206'),
		'TagList301': fields.char('Name'),
        'TagList302': fields.char('Address'),
		'TagList303': fields.char('Contact'),
		'TagList304': fields.char('Phone'),
		'TagList305': fields.char('Details'),
		'TagList306': fields.float('Price'),
		'TagList401': fields.char('Name'),
        'TagList402': fields.char('Address'),
		'TagList403': fields.char('Contact'),
		'TagList404': fields.char('Phone'),
		'TagList405': fields.text('Notes'),
		'TagList406': fields.float('Price'),
		'TagList501': fields.char('Ref No'),
        'TagList502': fields.char('Term'),
		'TagList503': fields.char('Rate %'),
		'TagList504': fields.char('Broker'),
		'TagList505': fields.char('Trident Fee'),
		'TagList506': fields.char('Doc Fee')


    }


class tag_cust_list_2(osv.osv):

    _name = "crm.lead.tag_cust_list_2"
    
    _columns = {
        'tag_list2_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList201': fields.char('Service Date'),
        'TagList202': fields.char('Kms'),
        'TagList203': fields.char('L203'),
        'TagList204': fields.char('L204'),
        'TagList205': fields.char('L205'),
        'TagList206': fields.float('L206')
    }

class tag_cust_list_3(osv.osv):

    _name = "crm.lead.tag_cust_list_3"
    
    _columns = {
        'tag_list3_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList301': fields.char('Name'),
        'TagList302': fields.char('Address'),
        'TagList303': fields.char('Contact'),
        'TagList304': fields.char('Phone'),
        'TagList305': fields.char('Details'),
        'TagList305a': fields.char('Spotters'),
        'TagList306': fields.float('Price')
    }
    

class tag_cust_list_4(osv.osv):

    _name = "crm.lead.tag_cust_list_4"
    
    _columns = {
        'tag_list4_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList401': fields.char('Name'),
        'TagList402': fields.char('Address'),
        'TagList403': fields.char('Contact'),
        'TagList404': fields.char('Phone'),
        'TagList405': fields.text('Notes'),
        'TagList406': fields.char('Email'),
        'TagList407': fields.float('Price')
    }
    
class tag_cust_list_5(osv.osv):

    _name = "crm.lead.tag_cust_list_5"
    
    _columns = {
        'tag_list5_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList501': fields.char('Ref No'),
        'TagList502': fields.char('Term'),
        'TagList503': fields.char('Rate %'),
        'TagList504': fields.char('Broker'),
        'TagList505': fields.char('Trident Fee'),
        'TagList506': fields.char('Doc Fee'),
        'TagList507': fields.char('Lender Name')
    }

class res_partner(osv.osv):

    _inherit = "res.partner"

    _columns = {

        'vehicle_name':fields.char('Vehicle',size=64),

    }
class industry(osv.osv):
    _name = "industry"
    

    _columns = {

        'name':fields.char('industry',size=64),

    }
tag_customer_tabs()
