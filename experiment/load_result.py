from surprise.chart import *

import os
import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt


# # dataset
# dataset_path1 = os.path.expanduser('./Dataset/ml-20m/')
# dataset_path2 = os.path.expanduser('./Dataset/LT/')

# # ml_dataset = Dataset(dataset_path=dataset_path1, tag_genome=False)
# lt_dataset = Dataset(dataset_path=dataset_path2,
#                      tag_genome=False, LT=True)
# lt_dataset.split(n_folds=5)
# lt_dataset.info()

import pickle


def load_perf_n_factors(dump_info):
    dump_dir = os.path.expanduser('dumps/n_factors/')
    SVD = pickle.load(open(os.path.join(dump_dir, 'SVD-' + dump_info), 'rb'))
    # ItemTopics = pickle.load(
    #     open(os.path.join(dump_dir, 'ItemTopics-' + dump_info), 'rb'))
    # ItemRelTags = pickle.load(
    #     open(os.path.join(dump_dir, 'ItemRelTags-' + dump_info), 'rb'))
    UserItemTags = pickle.load(
        open(os.path.join(dump_dir, 'UserItemTags-' + dump_info), 'rb'))
    # CrossItemTopics = pickle.load(
    #     open(os.path.join(dump_dir, 'CrossItemTopics-' + dump_info), 'rb'))
    # CrossItemRelTags = pickle.load(open(os.path.join(dump_dir, 'CrossItemRelTags-'+dump_info), 'rb'))
    # compare_factor_perf([SVD, ItemTopics, ItemRelTags,
    #                      UserItemTags, CrossItemTopics], 'rmse')
    compare_factor_perf([SVD, UserItemTags], 'rmse')


def load_perf_n_parts(dump_info):
    dump_dir = os.path.expanduser('dumps/usage_parts/')
    SVD = pickle.load(open(os.path.join(dump_dir, 'SVD-' + dump_info), 'rb'))
    ItemTopics = pickle.load(
        open(os.path.join(dump_dir, 'ItemTopics-' + dump_info), 'rb'))
    ItemRelTags = pickle.load(
        open(os.path.join(dump_dir, 'ItemRelTags-' + dump_info), 'rb'))
    UserItemTags = pickle.load(
        open(os.path.join(dump_dir, 'UserItemTags-' + dump_info), 'rb'))
    CrossItemTopics = pickle.load(
        open(os.path.join(dump_dir, 'CrossItemTopics-' + dump_info), 'rb'))
    # CrossItemRelTags = pickle.load(open(os.path.join(dump_dir, 'CrossItemRelTags-'+dump_info), 'rb'))
    compare_part_usage_perf(
        [SVD, ItemTopics, ItemRelTags, CrossItemTopics, CrossItemRelTags], 'rmse')





load_perf_n_factors('ml_grid_search_n_factors')
