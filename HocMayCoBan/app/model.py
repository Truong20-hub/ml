from pathlib import Path
from typing import Dict, List

import pandas as pd

from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder


class MushroomNaiveBayes:
    def __init__(self):
        self.model = CategoricalNB()
        self.encoder = OrdinalEncoder()

        self.data = None
        self.feature_columns: List[str] = []
        self.target_column = None
        self.classes = []

        self.accuracy = 0.0
        self.is_trained = False

        self.dataset_path = (
            Path(__file__).resolve().parent / "data" / "mushrooms.csv"
        )

    def load_data(self):
        if not self.dataset_path.exists():
            raise FileNotFoundError(
                f"Không tìm thấy dataset tại: {self.dataset_path}"
            )

        self.data = pd.read_csv(self.dataset_path)

        if self.data.empty:
            raise ValueError("Dataset đang rỗng.")

        # Loại bỏ khoảng trắng ở tên cột
        self.data.columns = self.data.columns.str.strip()

        # Thay ký hiệu ? bằng giá trị missing
        self.data = self.data.replace("?", "missing")

        # Xóa các dòng bị trùng
        self.data = self.data.drop_duplicates()

        # Theo dataset Mushroom chuẩn, cột đầu tiên là nhãn class
        self.target_column = self.data.columns[0]

        self.feature_columns = [
            column
            for column in self.data.columns
            if column != self.target_column
        ]

        return self.data

    def train(self):
        self.load_data()

        X = self.data[self.feature_columns]
        y = self.data[self.target_column]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            random_state=42,
            stratify=y
        )

        # Mã hóa dữ liệu dạng chữ thành số
        X_train_encoded = self.encoder.fit_transform(X_train)
        X_test_encoded = self.encoder.transform(X_test)

        # Chuyển về số nguyên vì CategoricalNB làm việc với category integer
        X_train_encoded = X_train_encoded.astype(int)
        X_test_encoded = X_test_encoded.astype(int)

        # Huấn luyện Naive Bayes
        self.model.fit(X_train_encoded, y_train)

        # Dự đoán tập kiểm tra
        y_pred = self.model.predict(X_test_encoded)

        # Tính accuracy
        self.accuracy = accuracy_score(y_test, y_pred)

        self.classes = self.model.classes_.tolist()
        self.is_trained = True

        print("Huấn luyện model thành công.")
        print(f"Số dòng dữ liệu: {len(self.data)}")
        print(f"Số đặc trưng: {len(self.feature_columns)}")
        print(f"Cột mục tiêu: {self.target_column}")
        print(f"Accuracy: {self.accuracy:.4f}")

        return self

    def predict(self, features: Dict[str, str]):
        if not self.is_trained:
            raise RuntimeError("Model chưa được huấn luyện.")

        # Kiểm tra có thiếu feature không
        missing_features = [
            column
            for column in self.feature_columns
            if column not in features
        ]

        if missing_features:
            raise ValueError(
                f"Thiếu các feature: {missing_features}"
            )

        # Sắp xếp feature theo đúng thứ tự lúc train
        input_data = pd.DataFrame(
            [[features[column] for column in self.feature_columns]],
            columns=self.feature_columns
        )

        input_data = input_data.replace("?", "missing")

        input_encoded = self.encoder.transform(input_data)
        input_encoded = input_encoded.astype(int)

        prediction = self.model.predict(input_encoded)[0]
        probabilities = self.model.predict_proba(input_encoded)[0]

        probability_result = {}

        for class_name, probability in zip(
            self.classes,
            probabilities
        ):
            probability_result[str(class_name)] = round(
                float(probability),
                4
            )

        return {
            "prediction": str(prediction),
            "probabilities": probability_result
        }

    def get_info(self):
        return {
            "is_trained": self.is_trained,
            "dataset_path": str(self.dataset_path),
            "total_rows": len(self.data) if self.data is not None else 0,
            "target_column": self.target_column,
            "feature_count": len(self.feature_columns),
            "feature_columns": self.feature_columns,
            "classes": self.classes,
            "accuracy": round(self.accuracy, 4)
        }


# Tạo model dùng chung cho API
mushroom_model = MushroomNaiveBayes()
mushroom_model.train()