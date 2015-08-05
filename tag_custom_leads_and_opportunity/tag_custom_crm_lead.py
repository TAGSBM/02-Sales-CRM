from openerp.osv import fields, osv

class tag_custom_opportunity(osv.osv):

  _inherit = "crm.lead"

  _columns = {
    'firstname':fields.char('First Name', size=50),
    'lastname':fields.char('Last Name', size=50),
    'refer' : fields.many2one('res.partner', 'Refferal Partners', select=True),
    'industry': fields.many2one('industry', 'Industry', select=True),
	'namecom': fields.many2many('marketing.campaign','campaign_compagn_reli','crm_lead_id','marketing_campaign_id','Campaign'),
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
    'TagCustL1Label': fields.char('List Name 1', size=1),
    'TagCustAL1': fields.float('List Opt 1'),
    'TagCustAL2': fields.float('List Opt 2'), 
    'TagCustAL3': fields.float('List Opt 3'), 
    'TagCustAL4': fields.float('List Opt 4'), 
    'TagCustAL5': fields.float('List Opt 5'),
    'TagCustAL6': fields.float('List Opt 6'),
    'TagCustAL7': fields.float('List Opt 7'), 
    'TagCustAL8': fields.float('List Opt 8'),
    'TagCustAL9': fields.float('List Opt 9'), 
    'TagCustAL9a': fields.float('List Opt 9a'),
    'TagCustAL9b': fields.float('List Opt 9b'),
    'TagCustAL9c': fields.float('List Opt 9c'),
    'TagCustAL9d': fields.float('List Opt 9d'),
    'TagCustAL10': fields.float('List Opt 10'),
    'TagCustAL11': fields.float('List Opt 11'),
    'TagCustAL12': fields.float('List Opt 12'), 
    'TagCustAL13': fields.float('List Opt 13'), 
    'TagCustAL14': fields.float('List Opt 14'), 
    'TagCustAL15': fields.float('List Opt 15'),
    'TagCustAL16': fields.float('List Opt 16'),
    'TagCustL1Label2': fields.char('List Label 1', size=1),
    'TagCustAL21': fields.float('List Opt 21'),
    'TagCustAL22': fields.float('List Opt 22'), 
    'TagCustAL23': fields.float('List Opt 23'), 
    'TagCustAL24': fields.float('List Opt 24'), 
    'TagCustAL25': fields.float('List Opt 25'),
    'TagCustAL26': fields.float('List Opt 26'),
    'TagCustAL27': fields.float('List Opt 27'), 
    'TagCustAL28': fields.float('List Opt 28'),
    'TagCustAL29': fields.float('List Opt 29'), 
    'TagCustAL30': fields.float('List Opt 30'),
    'TagCustAL31': fields.float('List Opt 31'),
    'TagCustAL32': fields.float('List Opt 32'), 
    'TagCustAL33': fields.float('List Opt 33'), 
    'TagCustAL34': fields.float('List Opt 34'), 
    'TagCustAL35': fields.float('List Opt 35'),
    'TagCustAL36': fields.float('List Opt 36'),
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
    'TagCustList02':fields.one2many('crm.lead.tag_cust_list_2', 'tag_list2_id', 'TagListA02'),
    'TagCustList03':fields.one2many('crm.lead.tag_cust_list_3', 'tag_list3_id', 'TagListA03'),
    'TagCustList04':fields.one2many('crm.lead.tag_cust_list_4', 'tag_list4_id', 'TagListA04'),
    'TagCustList05':fields.one2many('crm.lead.tag_cust_list_5', 'tag_list5_id', 'TagListA05')
  }
  
class tag_cust_list_1(osv.osv):

    _name = "crm.lead.tag_cust_list_1"
    
    _columns = {
        'tag_list1_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList101': fields.char('L1 Choice 1'),
        'TagList102': fields.char('L1 Choice 4'),
        'TagList103': fields.char('L1 Choice 3'),
        'TagList104': fields.char('L1 Choice 4'),
        'TagList105': fields.char('L1 Choice 5', size=20),
        'TagList106': fields.text('L1 Choice 6', size=150)
    }
    
class tag_cust_list_2(osv.osv):

    _name = "crm.lead.tag_cust_list_2"
    
    _columns = {
        'tag_list2_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
		'TagList201': fields.date('L2 Choice 1'),
        'TagList202': fields.char('L2 Choice 2'),
        'TagList203': fields.char('L2 Choice 3'),
        'TagList204': fields.char('L2 Choice 4'),
        'TagList205': fields.char('L2 Choice 5'),
        'TagList206': fields.float('L2 Choice 6')
    }

class tag_cust_list_3(osv.osv):

    _name = "crm.lead.tag_cust_list_3"
    
    _columns = {
        'tag_list3_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList301': fields.char('L3 Choice 1'),
        'TagList302': fields.char('L3 Choice 2'),
        'TagList303': fields.char('L3 Choice 3'),
        'TagList304': fields.char('L3 Choice 4'),
        'TagList305': fields.char('L3 Choice 5'),
        'TagList306': fields.char('L3 Choice 6'),
        'TagList307': fields.char('L3 Choice 7')
    }
    

class tag_cust_list_4(osv.osv):

    _name = "crm.lead.tag_cust_list_4"
    
    _columns = {
        'tag_list4_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList401': fields.char('L4 Choice 1'),
        'TagList402': fields.char('L4 Choice 2'),
        'TagList403': fields.char('L4 Choice 3'),
        'TagList404': fields.char('L4 Choice 4'),
        'TagList405': fields.text('L4 Choice 5'),
        'TagList406': fields.char('L4 Choice 6'),
        'TagList407': fields.float('L4 Choice 7')
    }
    
class tag_cust_list_5(osv.osv):

    _name = "crm.lead.tag_cust_list_5"
    
    _columns = {
        'tag_list5_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList501': fields.char('L5 Choice 1'),
        'TagList502': fields.char('L5 Choice 2'),
        'TagList503': fields.char('L5 Choice 3'),
        'TagList504': fields.char('L5 Choice 4'),
        'TagList505': fields.char('L5 Choice 5'),
        'TagList506': fields.char('L5 Choice 6'),
        'TagList507': fields.char('L5 Choice 7')
    }
