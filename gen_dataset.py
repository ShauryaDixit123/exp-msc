import csv
import random
from datetime import datetime
import uuid

# Configuration data
buyer_names = [
    "Alice", "John", "Michael", "Robert", "David", "Emily", "Sophia", "James", "William", "Olivia",
    "Emma", "Daniel", "Benjamin", "Mia", "Charlotte", "Liam", "Noah", "Ava", "Isabella", "Ethan",
    "Alexander", "Sebastian", "Grace", "Chloe", "Lucas", "Mason", "Ella", "Harper", "Abigail", "Jackson",
    "Aiden", "Samuel", "Henry", "Scarlett", "Lily", "Zoe", "Matthew", "Joseph", "Levi", "Victoria",
    "Hannah", "David", "Andrew", "Christopher", "Joshua", "Natalie", "Madison", "Evelyn", "Logan", "Ryan"
]

items_list = [
    "SteelBeam-X", "AluSheet-Y", "CopperWire-Z", "GlassPanel-A", "PlasticPipe-B", "IronRod-C", "BrassPlate-D",
    "TitaniumBar-E", "CarbonFiber-F", "AluminumTubing-G", "StainlessSteel-H", "PVCSheet-I", "RubberGasket-J",
    "CeramicTile-K", "NylonBushing-L", "FiberglassMat-M", "CopperTubing-N", "BronzeFitting-O", "Polycarbonate-P",
    "AcrylicSheet-Q", "GalvanizedSteel-R", "NickelAlloy-S", "ZincCoating-T", "LeadSheet-U", "TinPlate-V",
    "MagnesiumBar-W", "TungstenRod-X", "SiliconWafer-Y", "GraphiteBlock-Z", "Polypropylene-AA", "Polyethylene-BB",
    "EpoxyResin-CC", "SiliconeSealant-DD", "AdhesiveTape-EE", "InsulationFoam-FF", "ConcreteMix-GG", "Mortar-HH",
    "Brick-II", "Cement-JJ", "Sandpaper-KK", "WoodPlank-LL", "Plywood-MM", "ParticleBoard-NN", "MDFBoard-OO",
    "Hardwood-PP", "Softwood-QQ", "Laminate-RR", "VinylFlooring-SS", "CarpetTile-TT"
]

quant_types = [
    "units", "pieces", "kilos", "liters", "boxes", "packs", "bundles", "rolls", "sheets", "pallets",
    "crates", "bags", "barrels", "cartons", "containers", "drums", "cans", "jars", "bottles", "tubes",
    "sacks", "cases", "trays", "racks", "bins", "totes", "cylinders", "spools", "reels", "blocks",
    "slabs", "panels", "strands", "coils", "strips", "rods", "beams", "planks", "tiles", "pipes",
    "wires", "cables", "hoses", "tanks", "vats", "buckets", "pails", "jugs", "flasks", "vials"
]

date_formats = [
    "%d %B %Y", "%B %d, %Y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y", "%m-%d-%Y",
    "%Y-%b-%d", "%b %d, %Y", "%d %b %Y", "%Y %b %d", "%d/%b/%Y", "%b/%d/%Y", "%Y/%b/%d", "%d-%b-%Y",
    "%b-%d-%Y", "%Y-%b-%d", "%d %B, %Y", "%B %d %Y", "%Y %B %d", "%d/%B/%Y", "%B/%d/%Y", "%Y/%B/%d",
    "%d-%B-%Y", "%B-%d-%Y", "%Y-%B-%d", "%d %b, %Y", "%b %d %Y", "%Y %b %d", "%d/%b/%Y", "%b/%d/%Y",
    "%Y/%b/%d", "%d-%b-%Y", "%b-%d-%Y", "%Y-%b-%d", "%d %B %Y", "%B %d, %Y", "%Y-%m-%d", "%d/%m/%Y",
    "%m/%d/%Y", "%Y/%m/%d", "%d-%m-%Y", "%m-%d-%Y", "%Y-%b-%d", "%b %d, %Y", "%d %b %Y", "%Y %b %d"
]

locations = [
    "Warehouse A", "Factory B", "Dock C", "Storage D", "Plant E", "Distribution Center F", "Logistics Hub G",
    "Manufacturing Unit H", "Shipping Yard I", "Cold Storage J", "Assembly Line K", "Production Facility L",
    "Loading Bay M", "Unloading Zone N", "Inventory Room O", "Dispatch Center P", "Receiving Area Q",
    "Packaging Station R", "Quality Control S", "Maintenance Depot T", "Tool Room U", "Workshop V",
    "Research Lab W", "Testing Facility X", "Training Center Y", "Office Z", "Headquarters AA", "Branch BB",
    "Regional Office CC", "Field Office DD", "Site EE", "Project Site FF", "Construction Yard GG", "Mining Site HH",
    "Quarry II", "Oil Rig JJ", "Refinery KK", "Power Plant LL", "Wind Farm MM", "Solar Park NN", "Hydro Station OO",
    "Nuclear Plant PP", "Data Center QQ", "Server Room RR", "Cloud Facility SS", "Network Hub TT", "Telecom Center UU",
    "Broadcasting Station VV", "Media House WW", "Studio XX"
]

reject_reasons = [
    "pricing issues", "delivery delays", "quality concerns", "insufficient stock", "specification mismatch",
    "incorrect documentation", "missing paperwork", "expired certification", "damaged goods", "wrong quantity",
    "incorrect labeling", "packaging defects", "transportation issues", "customs clearance problems",
    "regulatory non-compliance", "safety violations", "environmental concerns", "technical failures",
    "performance issues", "unmet standards", "late submission", "incomplete order", "wrong product",
    "unsuitable material", "color mismatch", "size discrepancy", "weight variation", "dimension errors",
    "expired product", "defective parts", "missing components", "incorrect assembly", "poor workmanship",
    "unapproved changes", "unauthorized substitution", "inadequate testing", "failed inspection",
    "non-functional item", "unsafe for use", "outdated technology", "incompatible with system",
    "lack of spare parts", "excessive lead time", "unreliable supplier", "communication breakdown",
    "contract disputes", "payment issues", "budget constraints", "project cancellation"
]

# INCO Terms and Payment Terms
INCO_TERMS = [
    {"label": "Ex Works", "value": "EXW"},
    {"label": "Free Carrier", "value": "FCA"},
    {"label": "Carriage Paid to", "value": "CPT"},
    {"label": "Carriage and Insurance Paid To", "value": "CIP"},
    {"label": "Delivered at Place", "value": "DAP"},
    {"label": "Delivered at Place Unloaded", "value": "DPU"},
    {"label": "Delivered Duty Paid", "value": "DDP"},
    {"label": "Free Alongside Ship", "value": "FAS"},
    {"label": "Free on Board", "value": "FOB"},
    {"label": "Cost and Freight", "value": "CFR"},
    {"label": "Cost Insurance and Freight", "value": "CIF"},
]

PAYMENT_TERMS = [
  { "label": "Payment in Advance", "value": "PIA" },
  { "label": "Cash in Advance", "value": "CIA" },
  { "label": "Cash on Delivery", "value": "COD" },
  { "label": "End of Month", "value": "EOM" },
  { "label": "Cash Before Shipment", "value": "CBS" },
  { "label": "50% Payment Upfront", "value": "50%UP" },
]

# NER Tag Structure
BASE_TAGS = {
    'BUYER': 'B-BUYER',
    'RFQ_ID': 'B-RFQ_ID',
    'QUOTE_ID': 'B-QUOTE_ID',
    'ITEM_QUANT': 'B-ITEM{}_QUANT',
    'ITEM_QTYPE': 'B-ITEM{}_QTYPE',
    'ITEM_CODE': 'B-ITEM{}_CODE',
    'ITEM_DATE': 'B-ITEM{}_DATE',
    'ITEM_RATE': 'B-ITEM{}_RATE',
    'PICKUP': 'B-PICKUP',
    'DROP': 'B-DROP',
    'STATUS': 'B-STATUS',
    'REJECT_REASON': 'B-REJECT_REASON',
    'ACTION': 'B-ACTION',
    'INCO_TERM': 'B-INCO_TERM',
    'PAYMENT_TERM': 'B-PAYMENT_TERM'
}

def generate_delivery_date():
    year = random.choice([2024, 2025])
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    date_obj = datetime(year, month, day)
    return date_obj.strftime(random.choice(date_formats))

def generate_items(num_items, include_rates=False):
    items = []
    for _ in range(num_items):
        item = {
            'quantity': random.randint(1, 1000),
            'qtype': random.choice(quant_types),
            'code': random.choice(items_list),
            'date': generate_delivery_date()
        }
        if include_rates:
            item['rate'] = round(random.uniform(10.0, 1000.0), 2)
        items.append(item)
    return items

def build_item_string(item, index, include_rates=False):
    templates = [
        (f"{{quantity}} {{qtype}} of {{code}} delivery by {{date}}", 0.6),
        (f"{{quantity}} {{qtype}} - {{code}} needed by {{date}}", 0.3),
        (f"{{code}} x{{quantity}} to arrive before {{date}}", 0.1)
    ]
    template = random.choices([t[0] for t in templates], weights=[t[1] for t in templates])[0]
    if include_rates:
        template += f" at a rate of {{rate}} per {{qtype}}"
    return template.format(**item)

def generate_sentence():
    buyer = random.choice(buyer_names)
    action = random.choice(['rfq_accept', 'rfq_reject', 'quote_accept', 'quote_reject', 'create_rfq', 'create_quote'])
    num_items = random.randint(1, 4)
    include_rates = action == 'create_quote'
    items = generate_items(num_items, include_rates)

    # Include pickup and drop only for create_rfq and create_quote
    if action in ['create_rfq', 'create_quote']:
        pickup = random.choice(locations)
        drop = random.choice([loc for loc in locations if loc != pickup])
    else:
        pickup = None
        drop = None

    # Include INCO and Payment Terms
    inco_term = random.choice(INCO_TERMS)['label']
    payment_term = random.choice(PAYMENT_TERMS)['label']

    # Build items string
    item_strings = [build_item_string(item, i+1, include_rates) for i, item in enumerate(items)]
    items_text = ", ".join(item_strings[:-1]) + (" and " if num_items > 1 else "") + item_strings[-1]

    # Generate IDs
    if action in ['rfq_accept', 'rfq_reject', 'create_rfq']:
        entity_id = str(uuid.uuid4())
        id_type = 'rfq_id'
    else:
        entity_id = str(uuid.uuid4())
        id_type = 'quote_id'

    # Ensure RFQ_ID is present for quote creation
    if action == 'create_quote':
        rfq_id = str(uuid.uuid4())
        entities = {
            'buyer': buyer,
            'rfq_id': rfq_id,
            'quote_id': entity_id,
            'items': items,
            'pickup': pickup,
            'drop': drop,
            'inco_term': inco_term,
            'payment_term': payment_term
        }
    else:
        entities = {
            'buyer': buyer,
            id_type: entity_id,
            'items': items,
            'pickup': pickup,
            'drop': drop,
            'inco_term': inco_term,
            'payment_term': payment_term
        }

    if action in ['rfq_accept', 'rfq_reject', 'quote_accept', 'quote_reject']:
        if action == 'rfq_accept':
            templates = [
                {
                    'sentence': f"Approved request for quote with id {{id}}.",
                    'status_verb': 'approved',
                    'status_root': 'approve',
                    'action_words': ['Approved']
                },
                {
                    'sentence': f"RFQ for id {{id}} has been approved.",
                    'status_verb': 'approved',
                    'status_root': 'approve',
                    'action_words': ['approved']
                },
                {
                    'sentence': f"Approval confirmation for RFQ id {{id}}.",
                    'status_verb': 'Approval',
                    'status_root': 'approve',
                    'action_words': ['Approval']
                }
            ]
        elif action == 'rfq_reject':
            reject_reason = random.choice(reject_reasons)
            templates = [
                {
                    'sentence': f"Rejected RFQ with id {{id}} due to {reject_reason}.",
                    'status_verb': 'rejected',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['Rejected']
                },
                {
                    'sentence': f"Request for quote with id {{id}} was declined by {buyer} because of {reject_reason}.",
                    'status_verb': 'declined',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['declined']
                },
                {
                    'sentence': f"Rejection of RFQ {{id}} due to {reject_reason}.",
                    'status_verb': 'Rejection',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['Rejection']
                }
            ]
        elif action == 'quote_accept':
            templates = [
                {
                    'sentence': f"Accepted quote for id {{id}}.",
                    'status_verb': 'accepted',
                    'status_root': 'accept',
                    'action_words': ['Accepted']
                },
                {
                    'sentence': f"Quote {{id}} was accepted.",
                    'status_verb': 'accepted',
                    'status_root': 'accept',
                    'action_words': ['accepted']
                },
                {
                    'sentence': f"Acceptance of quote {{id}} done.",
                    'status_verb': 'Acceptance',
                    'status_root': 'accept',
                    'action_words': ['Acceptance']
                }
            ]
        elif action == 'quote_reject':
            reject_reason = random.choice(reject_reasons)
            templates = [
                {
                    'sentence': f"Rejected quote with id {{id}} due to {reject_reason}",
                    'status_verb': 'rejected',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['Rejected']
                },
                {
                    'sentence': f"Quote with id {{id}} was declined because of {reject_reason}",
                    'status_verb': 'declined',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['declined']
                },
                {
                    'sentence': f"Rejection of quote with id {{id}} due to {reject_reason}",
                    'status_verb': 'Rejection',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['Rejection']
                }
            ]
        selected_template = random.choice(templates)
        sentence = selected_template['sentence'].format(id=entity_id, inco_term=inco_term, payment_term=payment_term)
        entities['status_verb'] = selected_template['status_verb']
        entities['status_root'] = selected_template['status_root']
        if 'reject_reason' in selected_template:
            entities['reject_reason'] = selected_template['reject_reason']
        entities['action_words'] = selected_template['action_words']
    else:
        if action == 'create_rfq':
            templates = [
                {
                    'sentence': f"A new request for quote for {items_text} to be delivered at {drop} under {inco_term} for payment terms as {payment_term}",
                    'action_words': ['request', 'for', 'quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"New RFQ to be created for payment term as {payment_term} and for INCO terms as {inco_term} with requirements: {items_text} on location {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Request for quote on location {drop} on following items {items_text} for INCO terms as {inco_term} and payment terms as {payment_term}",
                    'action_words': ['Request', 'for', 'quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ created for items: {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"New RFQ for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Request for quote for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['Request', 'for', 'quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ generated for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"New RFQ for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ created for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Request for quote for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['Request', 'for', 'quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ generated for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"New RFQ for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ created for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Request for quote for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['Request', 'for', 'quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ generated for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"New RFQ for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ created for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Request for quote for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['Request', 'for', 'quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ generated for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"New RFQ for {items_text} under {inco_term} and {payment_term}, delivery at {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                }
            ]
            selected_template = random.choice(templates)
            sentence = selected_template['sentence'].format(inco_term=inco_term, payment_term=payment_term)
            entities['action_words'] = selected_template['action_words']
            entities['pickup'] =  selected_template['pickup']
            entities['drop'] =  selected_template['drop']
            entities['inco_terms'] =  selected_template['inco_terms']
            entities['payment_terms'] =  selected_template['payment_terms']
        else:  # create_quote
            templates = [
                {
                    'sentence': f"Quote for RFQ on id {{rfq_id}} under {inco_term} for payment terms as {payment_term} with the following items: {items_text} to be picked up from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote has been prepared on request for quote id: {{rfq_id}} for pickup location as {pickup} including {items_text} under {inco_term} and {payment_term}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"New quote to be created for payment term as {payment_term} and for INCO terms as {inco_term} for RFQ {{rfq_id}} with items: {items_text}, picked up from {pickup}",
                    'action_words': ['quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} has been quoted with {inco_term} and {payment_term} for items: {items_text}, to be picked up from {pickup}",
                    'action_words': ['quoted'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Prepared a quote for RFQ {{rfq_id}} under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['Prepared'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote generated for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['generated'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} quote prepared under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['prepared'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} quote created under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['created'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} quote finalized under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['finalized'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} quote submitted under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['submitted'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} quote approved under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['approved'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} quote processed under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['processed'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"RFQ {{rfq_id}} quote completed under {inco_term} and {payment_term} for items: {items_text}, pickup at {pickup}",
                    'action_words': ['completed'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                },
                {
                    'sentence': f"Quote for RFQ {{rfq_id}} with {inco_term} and {payment_term} for items: {items_text}, pickup from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop,
                    'inco_terms': inco_term,
                    'payment_terms': payment_term
                }
            ]
            selected_template = random.choice(templates)
            sentence = selected_template['sentence'].format(rfq_id=entities['rfq_id'], inco_term=inco_term, payment_term=payment_term)
            entities['action_words'] = selected_template['action_words']
            entities['pickup'] =  selected_template['pickup']
            entities['drop'] =  selected_template['drop']
            entities['inco_terms'] =  selected_template['inco_terms']
            entities['payment_terms'] =  selected_template['payment_terms']

    return sentence, entities

def tag_sentence(sentence, entities):
    # Tokenize into words (split on whitespace)
    tokens = []
    current_token = []
    for char in sentence:
        if char.isspace():
            if current_token:
                tokens.append(''.join(current_token))
                current_token = []
        else:
            current_token.append(char)
    if current_token:
        tokens.append(''.join(current_token))

    # Initialize all tags as 'O'
    tags = ['O'] * len(tokens)

    # Tag buyer
    buyer = entities['buyer']
    for i, token in enumerate(tokens):
        if token == buyer:
            tags[i] = BASE_TAGS['BUYER']
            break

    # Tag RFQ_ID if present
    if 'rfq_id' in entities:
        rfq_id = entities['rfq_id']
        for i, token in enumerate(tokens):
            if token == rfq_id:
                tags[i] = BASE_TAGS['RFQ_ID']
                break

    # Tag QUOTE_ID if present
    if 'quote_id' in entities:
        quote_id = entities['quote_id']
        for i, token in enumerate(tokens):
            if token == quote_id:
                tags[i] = BASE_TAGS['QUOTE_ID']
                break

    # Tag pickup and drop locations if present
    if 'pickup' in entities and entities['pickup']:
        pickup_tokens = entities['pickup'].split()
        for i in range(len(tokens) - len(pickup_tokens) + 1):
            if tokens[i:i+len(pickup_tokens)] == pickup_tokens:
                tags[i] = BASE_TAGS['PICKUP']
                for j in range(1, len(pickup_tokens)):
                    tags[i+j] = 'I-PICKUP'
                break

    if 'drop' in entities and entities['drop']:
        drop_tokens = entities['drop'].split()
        for i in range(len(tokens) - len(drop_tokens) + 1):
            if tokens[i:i+len(drop_tokens)] == drop_tokens:
                tags[i] = BASE_TAGS['DROP']
                for j in range(1, len(drop_tokens)):
                    tags[i+j] = 'I-DROP'
                break
    # inco_term = entities.get('inco_term')
    # if inco_term:
    #     for i, token in enumerate(tokens):
    #         if token == inco_term:
    #             tags[i] = BASE_TAGS['INCO_TERM']
    #             break
    if 'inco_terms' in entities and entities['inco_terms']:
        inco_term_token = entities['inco_terms'].split()
        for i in range(len(tokens) - len(inco_term_token) + 1):
            if tokens[i:i+len(inco_term_token)] == inco_term_token:
                tags[i] = BASE_TAGS['INCO_TERM']
                for j in range(1, len(inco_term_token)):
                    tags[i+j] = 'I-INCO_TERM'
                break

    # Tag Payment Term
    if 'payment_terms' in entities and entities['payment_terms']:
        inco_term_token = entities['payment_terms'].split()
        for i in range(len(tokens) - len(inco_term_token) + 1):
            if tokens[i:i+len(inco_term_token)] == inco_term_token:
                tags[i] = BASE_TAGS['PAYMENT_TERM']
                for j in range(1, len(inco_term_token)):
                    tags[i+j] = 'I-PAYMENT_TERM'
                break
    # Tag items
    current_item = 1
    for item in entities.get('items', []):
        components = [
            (str(item['quantity']), 'ITEM_QUANT'),
            (item['qtype'], 'ITEM_QTYPE'),
            (item['code'], 'ITEM_CODE'),
            (item['date'], 'ITEM_DATE')
        ]
        if 'rate' in item:
            components.append((f"{item['rate']}", 'ITEM_RATE'))

        for value, tag_type in components:
            for i in range(len(tokens)):
                if tokens[i] == value:
                    formatted_tag = BASE_TAGS[tag_type].format(current_item)
                    tags[i] = formatted_tag
                    # Handle multi-word dates or rates
                    if tag_type in ['ITEM_DATE', 'ITEM_RATE'] and ' ' in value:
                        value_parts = value.split()
                        for j in range(1, len(value_parts)):
                            if i+j < len(tokens) and tokens[i+j] == value_parts[j]:
                                tags[i+j] = f'I-ITEM{current_item}_{tag_type.split("_")[1]}'
                    break
        current_item += 1

    # Tag status verb if present
    status_verb = entities.get('status_verb')
    if status_verb:
        status_parts = status_verb.split()
        for i in range(len(tokens) - len(status_parts) + 1):
            if tokens[i:i+len(status_parts)] == status_parts:
                tags[i] = BASE_TAGS['STATUS']
                for j in range(1, len(status_parts)):
                    tags[i + j] = 'I-STATUS' if len(status_parts) > 1 else 'O'
                break

    # Tag reject reason if present
    reject_reason = entities.get('reject_reason')
    if reject_reason:
        reject_parts = reject_reason.split()
        for i in range(len(tokens) - len(reject_parts) + 1):
            if tokens[i:i+len(reject_parts)] == reject_parts:
                tags[i] = BASE_TAGS['REJECT_REASON']
                for j in range(1, len(reject_parts)):
                    tags[i + j] = 'I-REJECT_REASON' 
                    # if len(reject_parts) > 1 else 'O'
                break

    # Tag action words if present
    if 'action_words' in entities:
        action_sequence = entities['action_words']
        for i in range(len(tokens) - len(action_sequence) + 1):
            if tokens[i:i + len(action_sequence)] == action_sequence:
                tags[i] = BASE_TAGS['ACTION']
                for j in range(1, len(action_sequence)):
                    if i + j < len(tags):
                        tags[i + j] = 'I-ACTION'
                break

    # Tag INCO Term


    return ' '.join(tokens), ' '.join(tags)

def generate_dataset(num_samples):
    dataset = []
    for _ in range(num_samples):
        sentence, entities = generate_sentence()
        tokens, tags = tag_sentence(sentence, entities)
        dataset.append((tokens, tags))
    return dataset

def save_to_csv(dataset, filename="ner_dataset2.csv"):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['tokens', 'tags'])
        for tokens, tags in dataset:
            writer.writerow([tokens, tags])

if __name__ == "__main__":
    num_samples = int(input("Enter number of samples to generate: "))
    dataset = generate_dataset(num_samples)
    save_to_csv(dataset)
    print(f"Generated {num_samples} samples in ner_dataset.csv")