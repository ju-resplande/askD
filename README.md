<br />
<div align="center">
    <h2 align="center">AskDocs: A medical QA dataset</h2>
    <img src="https://images.emojiterra.com/google/noto-emoji/v2.034/512px/1fa7a.png" alt="https://en.wikipedia.org/wiki/Stethoscope" width="250">
    <br />
  <img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/ju-resplande/askD?include_prereleases">
  <img alt="GitHub" src="https://img.shields.io/github/license/ju-resplande/askD">
  <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/ju-resplande/askD?style=social">
  <p align="center">
  <b>
    <a href="https://huggingface.co/datasets/eli5">ELI5 dataset</a> adapted on <a href="https://www.reddit.com/r/AskDocs/">Medical Questions (AskDocs)</a> subreddit.
  </b>
  </p>
</div>

## Getting Started

|                             | Train  | Valid | Test | External |
| -----                       | ------ | ----- | ---- | -------- |
| en                          | 24256  |  5198 | 5198 | 166804   |
| pt                          | 24256  |  5198 | 5198 | 166804   |

The dataset questions and answers span a period from January 2013 to December 2019.

We additionally translated to Portuguese and used <a href="https://github.com/LasseRegin/medical-question-answer-data"> external data from here<a>, which is a binary classification dataset "a QNLI medical-like". We adapted to value 5 or 0.

### Usage

#### Datasets :hugs:

```python
from datasets import load_dataset

data = load_dataset("ju-resplande/askD", split="train_pt")
# ['train_en', 'validation_en', 'test_en', 'external_en', 'train_pt', 'validation_pt', 'test_pt', 'external_pt']
```

## Citing

```bibtex
@misc{Gomes20202,
  author = {GOMES, J. R. S.},
  title = {AskDocs: A medical QA dataset},
  year = {2020},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/ju-resplande/askD}},
  commit = {42060c4402c460e174cbb75a868b429c554ba2b7}
}
```

## Acknowledgments

[@viniciusplo](https://github.com/viniciusplo) and [@ruanchaves](https://github.com/ruanchaves) for giving the idea. :smiley:
