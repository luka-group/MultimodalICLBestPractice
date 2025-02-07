# MultimodalICLBestPractice
Codes for our NAACL 2025 paper "From Introspection to Best Practices: Principled Analysis of Demonstrations in Multimodal In-Context Learning"

### Datasets
We provide train and test split data for inductive bias tasks, i.e., `Flipped Labels`, `Visual Hallucination`, and `Counting Characters`.
1. Flipped Labels
It is based on [AMBER](https://github.com/junyangwang0410/AMBER.git) dataset. Please download the images accordingly. We directly adopt original attribute and relation data, with their labels flipped from yes to no, or no to yes. 
For existence dataset, we use both truth and hallucinated existence annotations to ensure 
that model captures inductive bias underlying demonstrations rather than achieving high accuracy through answering "Yes" or "No". You can find 
train and test split data in `./datasets/AMBER/`.
2. Visual Hallucination
It is based on [vqav2-idk](https://github.com/ncsoft/idk). All used images are from coco val2014, you can download from their official [website](https://cocodataset.org/#download).
Original vqav2-idk dataset only contains questions that are unanswerable. We randomly extract 5k instances from vqav2-idk and 5k from vqav2 as train, to ensure models do not learn shortcuts from demonstrations.
You can find the train and test prompts in `./datasets/vqav2_idk`.
3. Counting Characters
We creat this dataset by our own. You can find questions and images in `./datasets/counting_chars`.

### Evaluation
After obtaining generation from models, you can run the following command to evaluate their performance:
```shell
python evaluate.py --dataset amber --gen-file gen_file.json
```
NOTE that for amber dataset, we purely compute accuracy, i.e., whether the prediction is identical to the flipped label.
The higher the accuracy, the better the model captures inductive bias from demonstrations. This is different from the metric we use in our paper, where we compare prediction with the original label, which is the lower the better.

### Citation
If you find our work helpful, please cite this paper
```shell
@article{xu2024introspection,
  title={From introspection to best practices: Principled analysis of demonstrations in multimodal in-context learning},
  author={Xu, Nan and Wang, Fei and Zhang, Sheng and Poon, Hoifung and Chen, Muhao},
  journal={arXiv preprint arXiv:2407.00902},
  year={2024}
}
```
