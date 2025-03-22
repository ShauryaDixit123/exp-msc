
"""cxzczxczxc

"""

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
    {"label": "PIA - Payment in Advance", "value": "PIA"},
    {"label": "CIA - Cash in Advance", "value": "CIA"},
    {"label": "COD - Cash on Delivery", "value": "COD"},
    {"label": "EOM - End of Month", "value": "EOM"},
    {"label": "CBS - Cash Before Shipment", "value": "CBS"},
    {"label": "50% Upfront - 50% Payment Upfront", "value": "50%UP"},
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
        (f"{{quantity}} {{qtype}} of {{code}} (delivery by {{date}})", 0.6),
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
                    tags[i + j] = 'I-REJECT_REASON' if len(reject_parts) > 1 else 'O'
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

import pandas as pd
import numpy as np
import torch

torch.cuda.is_available()

data = pd.read_csv("/content/ner_dataset2.csv")

data.head()

data["tags"].iloc[0]

# list of all tags in dataset
tags = []
for tag in data["tags"].values:
    for i in tag.split():
        if i not in tags:
            tags.append(i)
idxToTag = {i:j for i,j in enumerate(tags)}
tagToIdx = {j:i for i,j in enumerate(tags)}
tags
# import numpy as np

# Extract all tags (flatten nested lists and ignore `-100`)
# all_tags = []
# for tag_sequence in data["tags"]:
#     all_tags.extend([t for t in tag_sequence if t != -100])

# Get unique tags (sorted for consistency)
tags = sorted(list(set(tags)))

print("Unique tags:", tags)
print("Number of classes:", len(tags))

# creating a idx list of tags
df = data.copy()
tags_idx = data["tags"].apply(lambda x: x.split())
idxed_senteces = []
for tag in tags_idx.values:
    idx = []
    for i in tag:
        idx.append(tagToIdx[i])
    idxed_senteces.append(idx)
df["tags_ids"] = idxed_senteces

df.head()

# !pip install -U transformers
# !pip install -U accelerate

from transformers import  AutoTokenizer


model_checkpoint = "dslim/bert-base-NER"
tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)

df["tokens"] = df['tokens'].apply(lambda x: x.split(" "))

inputs = df['tokens'][0]
print(inputs)
inputs = tokenizer(list(inputs), is_split_into_words=True, return_offsets_mapping=True, padding="max_length", truncation=True)
print(inputs.tokens(),inputs.word_ids(), inputs.input_ids)

print(inputs.tokens())
print(inputs.word_ids())

def align_labels_with_tokens(labels, word_ids):
  new_labels = []
  current_word=None
  for word_id in word_ids:
    if word_id != current_word:
      current_word = word_id
      label = -100 if word_id is None else labels[word_id]
      new_labels.append(label)

    elif word_id is None:
      new_labels.append(-100)

    else:
      label = labels[word_id]
      if label%2==1:
        label = label + 1
      new_labels.append(label)

  return new_labels

# import torch
# from transformers import DataCollatorForTokenClassification
# # # labels = df["tags_ids"][0]
# # # align_labels_with_tokens(labels, inputs.word_ids())
# # def tokenize_and_align(examples):
# #   # print(examples)
# #   inputs = list(examples['tokens'])
# #   # inputs = tokenizer(inputs, truncation=True, is_split_into_words=True)
# #   inputs = tokenizer(inputs, is_split_into_words=True, return_offsets_mapping=True, padding="max_length", truncation=True)
# #   labels = examples['tags_ids']
# #   new_labels = []
# #   for idx, label in enumerate([labels]):
# #     word_ids = inputs.word_ids(batch_index=idx)
# #     new_labels.append(align_labels_with_tokens(label, word_ids))

# #   inputs['labels'] = new_labels
# #   # print(inputs.attention_mask)
# #   return inputs
# # tokenized_datasets = df.apply(tokenize_and_align,axis=1)

# def tokenize_and_align(examples):
#     inputs = tokenizer(
#         examples['tokens'],
#         is_split_into_words=True,
#         padding='max_length',
#         truncation=True,
#         return_tensors='pt'  # Return PyTorch tensors directly
#     )

#     # Convert tag IDs to tensor
#     labels = torch.tensor(examples['tags_ids'], dtype=torch.long)

#     # Create word mappings and align labels
#     word_ids = inputs.word_ids()
#     aligned_labels = align_labels_with_tokens(labels, word_ids)

#     # Add labels to inputs dict
#     inputs['labels'] = aligned_labels

#     # Convert offset mapping to tensor
#     # inputs['offset_mapping'] = torch.tensor(inputs['offset_mapping'], dtype=torch.long)

#     return {k: v for k, v in inputs.items()}  # Remove batch dimension

# # Apply to dataframe
# tokenized_datasets = df.apply(tokenize_and_align, axis=1, result_type='expand')

# # Convert to list of dicts
# final_dataset = [dict(row) for _, row in tokenized_datasets.iterrows()]

# # Now use with data collator
# data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)
# batch = data_collator(final_dataset[:2])

# batch

from transformers import DataCollatorForTokenClassification
import torch

def align_labels_with_tokens(labels, word_ids):
    """
    Aligns labels with tokenized word pieces.
    Assigns -100 to special tokens and subword tokens.
    """
    aligned_labels = []
    previous_word_idx = None

    for word_idx in word_ids:
        if word_idx is None:
            aligned_labels.append(-100)  # Special tokens
        elif word_idx != previous_word_idx:
            aligned_labels.append(labels[word_idx].item())  # Use first subword label
        else:
            aligned_labels.append(-100)  # Ignore subword tokens

        previous_word_idx = word_idx

    return torch.tensor(aligned_labels, dtype=torch.long)

def tokenize_and_align(example):
    inputs = tokenizer(
        example['tokens'],
        is_split_into_words=True,
        padding='max_length',
        truncation=True,
        return_tensors='pt'
    )

    labels = torch.tensor(example['tags_ids'], dtype=torch.long)

    # Align labels
    word_ids = inputs.word_ids()
    aligned_labels = align_labels_with_tokens(labels, word_ids)

    # Add labels to inputs
    inputs['labels'] = aligned_labels.unsqueeze(0)  # Ensure batch dim consistency

    return {k: v.squeeze(0) for k, v in inputs.items()}  # Remove batch dim

# Apply function row-wise
tokenized_datasets = df.apply(tokenize_and_align, axis=1)

# Convert to list of dicts
final_dataset = list(tokenized_datasets)

# Use DataCollatorForTokenClassification
data_collator = DataCollatorForTokenClassification(tokenizer=tokenizer)
batch = data_collator(final_dataset[:2])

# Check batch structure
print(batch)

# !pip install seqeval
# !pip install evaluate
# !pip install sympy
# !pip install requests

import evaluate
metric = evaluate.load('seqeval')

# ner_feature = df.features['ner_tags']
label_names = tags
# print(ner_feature,label_names)

import numpy as np

def compute_metrics(eval_preds):
  logits, labels = eval_preds

  predictions = np.argmax(logits, axis=-1)

  true_labels = [[label_names[l] for l in label if l!=-100] for label in labels]

  true_predictions = [[label_names[p] for p,l in zip(prediction, label) if l!=-100]
                      for prediction, label in zip(predictions, labels)]

  all_metrics = metric.compute(predictions=true_predictions, references=true_labels)

  return {"precision": all_metrics['overall_precision'],
          "recall": all_metrics['overall_recall'],
          "f1": all_metrics['overall_f1'],
          "accuracy": all_metrics['overall_accuracy']}

from transformers import AutoModelForTokenClassification
model = AutoModelForTokenClassification.from_pretrained(
                                                    model_checkpoint,
                                                    id2label=idxToTag,
                                                    label2id=tagToIdx,
                                                    ignore_mismatched_sizes=True,
                                                    )

model.config.num_labels

from transformers import TrainingArguments

args = TrainingArguments(model_checkpoint,
                         evaluation_strategy = "epoch",
                         save_strategy="epoch",
                         learning_rate = 2e-5,
                         num_train_epochs=3,
                         weight_decay=0.01)

# import torch

# # Example: Fixing a single item in the dataset
# def fix_labels(item):
#     # Ensure labels is a 1D tensor
#     if item['labels'].ndim == 2:
#         item['labels'] = item['labels'].squeeze(0)
#      # Remove the batch dimension
#     if item['input_ids'].ndim == 2:
#         item['input_ids'] = item['input_ids'].squeeze(0)
#     if item['attention_mask'].ndim == 2:
#         item['attention_mask'] = item['attention_mask'].squeeze(0)
#     return item

# # Apply to the entire dataset
# final_dataset = [fix_labels(item) for item in final_dataset]



from sklearn.model_selection import train_test_split
import torch
device = torch.device("cuda")
model = model.to(device)
# Split the dataset into train and test sets (e.g., 80% train, 20% test)
train_dataset, test_dataset = train_test_split(final_dataset, test_size=0.2, random_state=42)
from transformers import Trainer
trainer = Trainer(model=model,
                  args=args,
                  train_dataset = train_dataset,
                  eval_dataset = test_dataset,
                  data_collator=data_collator,
                  compute_metrics=compute_metrics,
                  tokenizer=tokenizer)

trainer.train()



# unique_labels = set()
# for item in final_dataset:
#     unique_labels.update(item['labels'].tolist())

# print("Unique labels:", unique_labels)

from transformers import pipeline

checkpoint = f"/content/{model_checkpoint}/checkpoint-3000"
token_classifier = pipeline(
    "token-classification", model=checkpoint, aggregation_strategy="simple"
)

token_classifier("this is a request for quote with items: 24 racks of blam1 needed by 02/19/2025, 310 tubes of blanketsABC to be delivery by 2025 Jul 28 to be delivered at Wire and Fabric Warehouse")

import os
import zipfile

zf = zipfile.ZipFile("model_bert_new_1.zip", "w")
for dirname, subdirs, files in os.walk("/content/distilbert-finetuned-ner/checkpoint-3000"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()

"""generator edited"""

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
    'ACTION': 'B-ACTION'
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
        (f"{{quantity}} {{qtype}} of {{code}} (delivery by {{date}})", 0.6),
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
            'drop': drop
        }
    else:
        entities = {
            'buyer': buyer,
            id_type: entity_id,
            'items': items,
            'pickup': pickup,
            'drop': drop
        }

    if action in ['rfq_accept', 'rfq_reject', 'quote_accept', 'quote_reject']:
        if action == 'rfq_accept':
            templates = [
                {
                    'sentence': f"Approved Request for quote, Approved request for quote with id {{id}}",
                    'status_verb': 'approved',
                    'status_root': 'approve',
                    'action_words': ['Approved','Request','for', 'quote']
                },
                {
                    'sentence': f"Approved RFQ, RFQ for id {{id}} has been approved",
                    'status_verb': 'Approved',
                    'status_root': 'approve',
                    'action_words': ['Approved','RFQ']
                },
                {
                    'sentence': f"Request for quote approved, Approval confirmation for RFQ id {{id}}",
                    'status_verb': 'approved',
                    'status_root': 'approve',
                    'action_words': ['Request', 'for', 'quote' ,'approved']
                }
            ]
        elif action == 'rfq_reject':
            reject_reason = random.choice(reject_reasons)
            templates = [
                {
                    'sentence': f"Request for quote rejected, Rejected RFQ with id {{id}} due to {reject_reason}",
                    'status_verb': 'rejected',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['Request', 'for', 'quote' ,'rejected']
                },
                {
                    'sentence': f"RFQ rejected, Request for quote with id {{id}} was declined by {buyer} because of {reject_reason}",
                    'status_verb': 'declined',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['RFQ','rejected']
                },
                {
                    'sentence': f"Rejected RFQ, Rejection of RFQ {{id}} due to {reject_reason}",
                    'status_verb': 'Rejection',
                    'status_root': 'reject',
                    'reject_reason': reject_reason,
                    'action_words': ['Rejected', 'RFQ']
                }
            ]
        elif action == 'quote_accept':
            templates = [
                {
                    'sentence': f"Approved quote, Accepted quote for id {{id}}",
                    'status_verb': 'accepted',
                    'status_root': 'accept',
                    'action_words': ['Approved', 'quote']
                },
                {
                    'sentence': f"Quote approved, Quote {{id}} was accepted",
                    'status_verb': 'approved',
                    'status_root': 'approve',
                    'action_words': ['Quote','approved']
                },
                {
                    'sentence': f"Quote accepted, Acceptance of quote {{id}} done",
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
        sentence = selected_template['sentence'].format(id=entity_id)
        entities['status_verb'] = selected_template['status_verb']
        entities['status_root'] = selected_template['status_root']
        if 'reject_reason' in selected_template:
            entities['reject_reason'] = selected_template['reject_reason']
        entities['action_words'] = selected_template['action_words']
    else:
        if action == 'create_rfq':
            templates = [
                {
                    'sentence': f"A new request for quote for {items_text} to be delivered at {drop}",
                    'action_words': ['request','for',' quote'],
                    'pickup': pickup,
                    'drop': drop
                },
                {
                    'sentence': f"New RFQ with requirements: {items_text} on location {drop}",
                    'action_words': ['RFQ'],
                    'pickup': pickup,
                    'drop': drop
                },
                {
                    'sentence': f"Request for quote on location {drop} on following items {items_text}",
                    'action_words': ['Request', 'for', 'quote'],
                    'pickup': pickup,
                    'drop': drop
                }
            ]
            selected_template = random.choice(templates)
            sentence = selected_template['sentence']
            entities['action_words'] = selected_template['action_words']
            entities['pickup'] =  selected_template['pickup']
            entities['drop'] =  selected_template['drop']
        else:  # create_quote
            templates = [
                {
                    'sentence': f"Quote for RFQ on id {{rfq_id}} with the following items: {items_text} to be picked up from {pickup}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop
                },
                {
                    'sentence': f"Quote has been prepared on request for quote id: {{rfq_id}} for pickup location as {pickup} including {items_text}",
                    'action_words': ['Quote'],
                    'pickup': pickup,
                    'drop': drop
                },
                {
                    'sentence': f"New quote created for RFQ {{rfq_id}} with items: {items_text}, picked up from {pickup}",
                    'action_words': ['quote'],
                    'pickup': pickup,
                    'drop': drop
                }
            ]
            selected_template = random.choice(templates)
            sentence = selected_template['sentence'].format(rfq_id=entities['rfq_id'])
            entities['action_words'] = selected_template['action_words']
            entities['pickup'] =  selected_template['pickup']
            entities['drop'] =  selected_template['drop']

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
                    tags[i + j] = 'I-REJECT_REASON' if len(reject_parts) > 1 else 'O'
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