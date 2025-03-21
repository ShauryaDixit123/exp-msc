from extract_model import model_encoding_mapping, extract_model
from handlers.external.crud import crud_executor
from datetime import datetime

def get_model_by_name(name):
    model_zip = [i for i in model_encoding_mapping if model_encoding_mapping[i]["name"] == name][0]
    return extract_model(model_zip)

def use_model(text):
    model_ner_bert = get_model_by_name("ner_bert")
    model_bert_clf = get_model_by_name("bert_clf")
    return {
        "action" : model_bert_clf.predict(text),
        "bert_response" : model_ner_bert.predict(text),
    }

class process():
    def __init__(self, text):
        self.model_response = use_model(text)
        self.top_level = {}
        self.items = {}
        self.backend_payload = {}
        self.action = self.model_response["action"][0]['label']
    def call_backend(self, *args, **kwds):
        response = self.process_entities(self.model_response["bert_response"])
        print(response,"payload") # changes in payload here!
        return crud_executor(self.action, response).exec()
    def process_entities(self, entities):
        for entity in entities:
            group = entity['entity_group']
            word = entity['word']
            if group.startswith('ITEM'):
                parts = group.split('_', 1)
                if len(parts) < 2:
                    continue
                item_num, field = parts
                if item_num not in self.items:
                    self.items[item_num] = {}
                if field not in self.items[item_num]:
                    self.items[item_num][field] = []
                self.items[item_num][field].append(word)
            else:
                if group not in self.top_level:
                    self.top_level[group] = []
                self.top_level[group].append(word)
        drop_location = ' '.join([w.replace('##', '') for w in self.top_level.get('DROP', [])])
        pickup_location = ' '.join([w.replace('##', '') for w in self.top_level.get('PICKUP', [])])
        incoterms = ''.join([w.replace('##', '') for w in self.top_level.get('INCO_TERM', [])])
        paymentterm = ''.join([w.replace('##', '') for w in self.top_level.get('PAYMENT_TERM', [])])
        item_list = []
        for item_key in sorted(self.items.keys()):
            item = self.items[item_key]
            item_code = ''.join([w.replace('##', '') for w in item.get('CODE', [])])
            quant = ''.join([w.replace('##', '') for w in item.get('QUANT', [])])
            quantity = int(quant) if quant.isdigit() else 0
            qtype = ' '.join([w.replace('##', '') for w in item.get('QTYPE', [])])
            date = ''.join([w.replace('##', '') for w in item.get('DATE', [])])
            print(date)
            item_dict = {
                "title": "",
                "item_code": item_code,
                "description": "",
                "store_id": "",
                "quantity": quantity,
                "quantity_unit": qtype,
                "expected_delivery_date" : datetime.now().strftime('%Y-%m-%d'),
                # "expected_delivery_date": datetime.strptime(date, '%d%b%Y').strftime('%Y-%m-%d') if date != '' else '',
            }
            item_list.append(item_dict)

        # Construct final result
        result = {
            "buyer_id": "",
            "buyer_email_id" : "alice@example.com",
            "supplier_email_id" : "frank@example.com",
            "supplier_id": "",
            "inco_terms": incoterms,
            "pickup_location": pickup_location,
            "drop_location": drop_location,
            "payment_terms": paymentterm,
            "active": True,
            "due_date": datetime.now().strftime('%Y-%m-%d'),
            "status": "",
            "terms_and_conditions": "",
            "created_by": "",
            "notes": "",
            "items": item_list
        }
        return result


resp = process(
    # "RFQ to be created under terms as Free Carrier and payment terms as Payment in Advance, for 809 bags of BrassPlate-D needed by 2024/Sep/17, 454 bags - Cement-JJ needed by 02-April-2024 and 557 bins of IronRod-C delivery by 14-Jul-2024  delivery at 123 Main Street, Apt 101, MG Road, Mumbai , Maharashtra"
     "I am reaching out to request a quote for a shipment under Ex works terms , The goods will be picked up from 249 Maple Ave, Room 645, Silver Area, Kolkata, Odisha, 491239, India and delivered to 239 Maple St, Flat 691, Blue Area, Delhi, Punjab, 804751, India. I would like to proceed with PIA payment terms, and the due date for this transaction is 2025-11-21. Kindly share the quote at your earliest convenience."
)

print(resp.action, resp.call_backend().json())

# print(use_model("Request for quote with following items,24 racks of blam1 needed by 02/19/2025 310 tubes of blanketsABC to be delivery by 2025 Jul 28 to be delivered at Wire and Fabric Warehouse"))
# print(use_model("Request for quote accepted by buyer on 2022/06/22 for id 08d00e26-e7ae-48b4-8a34-93e00d3def54"))


