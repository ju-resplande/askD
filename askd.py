# coding=utf-8
# Lint as: python3
"""AskDocs: A medical QA dataset."""


import json

import datasets


logger = datasets.logging.get_logger(__name__)

_CITATION = """\
#TODO: citation
}
"""

_DESCRIPTION = """\
#TODO: description
"""


class AskDConfig(datasets.BuilderConfig):
    """BuilderConfig for AskD."""

    def __init__(self, **kwargs):
        """BuilderConfig for AskD.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(AskDConfig, self).__init__(**kwargs)


class AskD(datasets.GeneratorBasedBuilder):
    """AskDocs: A medical QA dataset."""

    VERSION = datasets.Version("1.0.0")

    BUILDER_CONFIGS = [
        AskDConfig(
            name="default",
            version=datasets.Version("1.0.0"),
            description="Default config",
        ),
    ]

    DEFAULT_CONFIG_NAME = "default"

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                    "q_id": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "selftext": datasets.Value("string"),
                    "category": datasets.Value("string"),
                    "subreddit": datasets.Value("string"),
                    "answers": {
                        "a_id": datasets.features.Sequence(datasets.Value("string")),
                        "text": datasets.features.Sequence(datasets.Value("string")),
                        "score": datasets.features.Sequence(datasets.Value("int32")),
                        "text_urls": datasets.features.Sequence(
                            datasets.features.Sequence(datasets.Value("string"))
                        ),
                    },
                    "title_urls": datasets.features.Sequence(datasets.Value("string")),
                    "selftext_urls": datasets.features.Sequence(
                        datasets.Value("string")
                    ),
                }
            ),
            supervised_keys=None,
            citation=_CITATION,
        )

    def _split_generators(self):
        _URL = "https://jingshensn2.github.io/eli5c/datasets/"
        downloaded_files = dl_manager.download_and_extract(
            {
                "train_pt": _URL + "AskDocs-train_pt.json.gz",
                "validation_pt": _URL + "AskDocs-validation_pt.json.gz",
                "test_pt": _URL + "AskDocs-test_pt.json.gz",
                "train_en": _URL + "AskDocs-train_en.json.gz",
                "validation_en": _URL + "AskDocs-validation_en.json.gz",
                "test_en": _URL + "AskDocs-test_en.json.gz",
            }
        )
        return [
            datasets.SplitGenerator(
                name=datasets.Split.datasets.Split(key),
                gen_kwargs={"filepath": downloaded_files[key]},
            )
            for key in downloaded_files
        ]

    def _generate_examples(self, filepath):
        logger.info("generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            example = json.load(f)
            for id_, row in enumerate(example):
                yield id_, row
