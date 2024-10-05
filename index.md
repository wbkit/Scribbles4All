---
layout: project_page
permalink: /

title: Scribbles for All - Benchmarking Scribble Supervised Segmentation Across Datasets
authors:
    Wolfgang Boettcher, Lukas Hoyer, Ozan Unal, Jan Eric Lenssen, Bernt Schiele
affiliations:
    MPI for Informatics, Saarland Informatics Campus, Germany
    ETH Xurich, Switzerland
    Huawei Technologies, Switzerland
paper: https://www.arxiv.org/abs/2408.12489
code: https://github.com/wbkit/Scribbles4All
data: https://github.com/wbkit/Scribbles4All
---

<!-- Using HTML to center the abstract -->
<div class="columns is-centered has-text-centered">
    <div class="column is-four-fifths">
        <h2>Abstract</h2>
        <div class="content has-text-justified">
In this work, we introduce Scribbles for All, a label and training data genera-
tion algorithm for semantic segmentation trained on scribble labels. Training or
fine-tuning semantic segmentation models with weak supervision has become an
important topic recently and was subject to significant advances in model quality.
In this setting, scribbles are a promising label type to achieve high quality segmen-
tation results while requiring a much lower annotation effort than usual pixel-wise
dense semantic segmentation annotations. The main limitation of scribbles as
source for weak supervision is the lack of challenging datasets for scribble segmen-
tation, which hinders the development of novel methods and conclusive evaluations.
To overcome this limitation, Scribbles for All provides scribble labels for several
popular segmentation datasets and provides an algorithm to automatically generate
scribble labels for any dataset with dense annotations, paving the way for new
insights and model advancements in the field of weakly supervised segmentation.
In addition to providing datasets and algorithm, we evaluate state-of-the-art seg-
mentation models on our datasets and show that models trained with our synthetic
labels perform competitively with respect to models trained on manual labels.
Thus, our datasets enable state-of-the-art research into methods for scribble-labeled
semantic segmentation. The datasets, scribble generation algorithm, and baselines
are publicly available at [Githib Link](https://github.com/wbkit/Scribbles4All).
        </div>
    </div>
</div>

---


## Citation
```
@online{boettcherScribblesAllBenchmarking2024,
  title = {Scribbles for {{All}}: {{Benchmarking Scribble Supervised Segmentation Across Datasets}}},
  shorttitle = {Scribbles for {{All}}},
  author = {Boettcher, Wolfgang and Hoyer, Lukas and Unal, Ozan and Lenssen, Jan Eric and Schiele, Bernt},
  date = {2024-08-22},
  eprint = {2408.12489},
  eprinttype = {arXiv},
  eprintclass = {cs},
  doi = {10.48550/arXiv.2408.12489},
  url = {http://arxiv.org/abs/2408.12489},
  urldate = {2024-10-05},
  abstract = {In this work, we introduce Scribbles for All, a label and training data generation algorithm for semantic segmentation trained on scribble labels. Training or fine-tuning semantic segmentation models with weak supervision has become an important topic recently and was subject to significant advances in model quality. In this setting, scribbles are a promising label type to achieve high quality segmentation results while requiring a much lower annotation effort than usual pixel-wise dense semantic segmentation annotations. The main limitation of scribbles as source for weak supervision is the lack of challenging datasets for scribble segmentation, which hinders the development of novel methods and conclusive evaluations. To overcome this limitation, Scribbles for All provides scribble labels for several popular segmentation datasets and provides an algorithm to automatically generate scribble labels for any dataset with dense annotations, paving the way for new insights and model advancements in the field of weakly supervised segmentation. In addition to providing datasets and algorithm, we evaluate state-of-the-art segmentation models on our datasets and show that models trained with our synthetic labels perform competitively with respect to models trained on manual labels. Thus, our datasets enable state-of-the-art research into methods for scribble-labeled semantic segmentation. The datasets, scribble generation algorithm, and baselines are publicly available at https://github.com/wbkit/Scribbles4All},
  pubstate = {prepublished},
  keywords = {Computer Science - Computer Vision and Pattern Recognition}
}
```
