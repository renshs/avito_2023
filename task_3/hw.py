from typing import List, Dict
from collections.abc import Iterable


class CountVectorizer:
    def __init__(self) -> None:
        self.vocabulary: Dict[str: int] = {}

    def fit_transform(self, data: list) -> List[list]:
        """
        Creating a dictionary vocabulary{} with features names.
        Then creates document term matrix and returns it.
        """

        assert isinstance(data, Iterable), "Not iterable data"
        assert all(isinstance(i, str) for i in data), (
            "Not only" "strings in data"
        )
        index = 0
        dtm = []
        for string in data:
            string = self.clear_string(string)
            for word in string.split():
                if word not in self.vocabulary:
                    self.vocabulary[word] = index
                    index += 1
        for string in data:
            string = self.clear_string(string)
            row = [0] * len(self.vocabulary.keys())
            for word in string.split():
                row[self.vocabulary[word]] += 1
            dtm.append(row)

        return dtm

    def get_feature_names(self) -> List[str]:
        """
        Returns a list of features names.
        """
        return list(self.vocabulary.keys())

    @staticmethod
    def clear_string(string: str) -> str:
        """
        Clears string.
        """
        return " ".join(
            [
                "".join([char for char in word if char.isalpha()])
                for word in string.split()
            ]
        ).lower()


if __name__ == "__main__":
    corpus = [
        "Crock Pot Pasta Never boil pasta again",
        "Pasta Pomodoro Fresh ingredients Parmesan to taste",
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(count_matrix)
