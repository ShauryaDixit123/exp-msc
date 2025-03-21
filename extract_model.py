from transformers import pipeline

import zipfile
import os

zip_path_ner_distilbert = "model_nerbert.zip"
zip_path_ner_bert = "model_bert_new_1.zip"
zip_path_ner_bert_clf = "model_bert_clf.zip"
model_encoding_mapping = {
    zip_path_ner_bert : {
        "name" : "ner_bert",
        "encoding" : "token-classification"
    },
    zip_path_ner_distilbert : {
        "name" : "distil_bert",
        "encoding" : "token-classification"
    },
    zip_path_ner_bert_clf : {
        "name" : "bert_clf",
        "encoding" : "text-classification"
    }
}

class extract_model():
    def __init__(self, zip_path):
        self.zip_path = zip_path
        self.output_dir = f"model/{zip_path.split('.')[0]}"
        if not os.path.exists(self.output_dir):
            print("Extracting zip file")
            with zipfile.ZipFile(self.zip_path, 'r') as zip_ref:
                zip_ref.extractall(f"model/{self.zip_path.split('.')[0]}")
                print("Extracted")
        self.checkpoint = self.output_dir
    def predict(self, text):
        self.task = model_encoding_mapping[self.zip_path]["encoding"]
        pipeline_kwargs = {
            "model": self.checkpoint
        }
        if self.task != "text-classification":
            pipeline_kwargs["aggregation_strategy"] = "simple"
        token_classifier = pipeline(
            model_encoding_mapping[self.zip_path]["encoding"],**pipeline_kwargs
        )
        return token_classifier(text)


# model = extract_model(zip_path_ner_bert_clf)
# print(model.predict("Request for quote with following items,24 racks of blam1 needed by 02/19/2025 310 tubes of blanketsABC to be delivery by 2025 Jul 28 to be delivered at Wire and Fabric Warehouse"))
# print(model.predict("Request for quote accepted by buyer on 2022/06/22 for id 08d00e26-e7ae-48b4-8a34-93e00d3def54"))


