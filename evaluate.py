# Created by xunannancy at 2025/02/07
import argparse
import json
from tqdm import tqdm
import numpy as np

def evaluate_amber(gen_file):
    res = json.load(open(gen_file))
    correctness = 0
    for entry in tqdm(res, total=len(res)):
        answer, annotation = entry['answer'].lower(), entry['annotation']
        if 'yes' in answer:
            pred = 'yes'
        else:
            pred = 'no'
        if pred == annotation:
            correctness += 1
    summary = {
        'score': correctness,
        'total': len(res),
        'accuracy': correctness/len(res),
    }
    print(summary)
    return

_vqav2_idx_prefixes = [
    'ambiguous',
    'depend',
    "i can't",
    'not sure',
    'not possible',
    "unknown",
    "bad question",
    "don't know",
    "none",
    "sorry",
    "uncertain",
    "cannot confirm",
    "it is difficult",
    "not clear",
    "hard to determine",
    "unanswerable",
    # new added on July 27th, 2024
    "i am not sure",
    'it is impossible',
    'it is not possible',
    "i don't know",
    'it is unknown',
    "i'm not sure",
    'it is unclear',
    "i can't determine",
    'it is ambiguous',
    'there is no',
    'there are no',
    'is not',
    'are not',
    'unknown',
    'no specific',
]
def evaluate_vqav2(gen_file):
    res = json.load(open(gen_file))
    score = 0
    for entry in tqdm(res, total=len(res)):
        answer = entry['answer']
        acc = any([i in answer.lower() for i in _vqav2_idx_prefixes])
        score += acc
    summary = {
        'score': score,
        'total': len(res),
        'accuracy': score/len(res),
    }
    print(summary)
    return

from collections import OrderedDict
manualMap = OrderedDict({
    # 'none': '0',
    # 'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'ten': '10',
})

reversed_manualMap = dict(zip(manualMap.values(), manualMap.keys()))
def evaluate_counting_chars(gen_file):
    res = json.load(open(gen_file))
    score_list = list()
    for entry in tqdm(res, total=len(res)):
        reference, candidate = entry['annotation'], entry['answer']
        if reference in candidate:
            score_list.append(1.0)
        elif reference in reversed_manualMap and reversed_manualMap[reference] in candidate:
            score_list.append(1.0)
        else:
            score_list.append(0.)
    summary = {
        'score': float(np.sum(score_list)),
        'total': len(res),
        'accuracy': float(np.mean(score_list)),
    }
    print(summary)
    return

if __name__ == '__main__':
    parser = argparse.ArgumentParser('evaluate inductive bias')
    parser.add_argument('--dataset', type=str, choices=['amber', 'vqav2-idk', 'counting_chars'], required=True)
    parser.add_argument('--gen-file', type=str, required=True)
    args = parser.parse_args()
    if args.dataset == "amber":
        evaluate_amber(args.gen_file)
    elif args.dataset == 'vqav2-idk':
        evaluate_vqav2(args.gen_file)
    elif args.dataset == 'counting_chars':
        evaluate_counting_chars(args.gen_file)
