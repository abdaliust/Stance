import os
import pandas as pd


class DatasetReader:

    def __init__(self):
        self.paths = {
            "vast": {
                "train": "datasets/VAST/vast_train.csv",
                "val": "datasets/VAST/vast_dev.csv",
                "test": "datasets/VAST/vast_test.csv"
            },
            "semeval2016": {
                "train": "datasets/SemEval2016 Task 6/SemEval-2016-Train.xlsx",
                "test": "datasets/SemEval2016 Task 6/SemEval-2016-Test-TaskA.xlsx"
            },
            "pstance": {
                "train": [
                    "datasets/P-Stance/raw_train_bernie.csv",
                    "datasets/P-Stance/raw_train_biden.csv",
                    "datasets/P-Stance/raw_train_trump.csv"
                ],
                "val": [
                    "datasets/P-Stance/raw_val_bernie.csv",
                    "datasets/P-Stance/raw_val_biden.csv",
                    "datasets/P-Stance/raw_val_trump.csv"
                ],
                "test": [
                    "datasets/P-Stance/raw_test_bernie.csv",
                    "datasets/P-Stance/raw_test_biden.csv",
                    "datasets/P-Stance/raw_test_trump.csv"
                ]
            }
        }

    def read_vast(self, data_type):
        path = self.paths["vast"].get(data_type)
        if not path:
            return []

        try:
            file = pd.read_csv(path)
        except ValueError:
            return []

        result = []
        for _, row in file.iterrows():
            result.append({
                "text": row["post"],
                "target": row["new_topic"],
                "stance": "favor" if row["label"] == 1 else "against" if row["label"] == 0 else "none"
            })

        return result

    def read_semeval2016(self, data_type):
        path = self.paths["semeval2016"].get(data_type)
        if not path:
            return []

        try:
            file = pd.read_excel(path)
        except ValueError:
            return []

        result = []
        for _, row in file.iterrows():
            result.append({
                "text": row["Tweet"],
                "target": row["Target"],
                "stance": row["Stance"].lower()
            })

        return result

    def read_pstance(self, data_type):
        paths = self.paths["pstance"].get(data_type, [])
        if not paths:
            return []

        result = []
        for path in paths:
            try:
                file = pd.read_csv(path)
            except ValueError:
                continue

            for _, row in file.iterrows():
                result.append({
                    "text": row["Tweet"],
                    "target": row["Target"],
                    "stance": row["Stance"].lower()
                })

        return result
