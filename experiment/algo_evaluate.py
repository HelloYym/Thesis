
from surprise import KNNWithMeans
from surprise import Dataset
from surprise import evaluate, print_perf, evaluate_parts

import pickle
import os

from surprise import SVD, UserItemTags, UserItemGenomeTags, ItemRelTags, UserItemRelTags, ItemTopics, UserItemTopics
from surprise import CrossUserItemTags, CrossUserItemRelTags, CrossItemRelTags, CrossItemTopics

from surprise import GridSearch

from surprise.chart import *


# path to dataset file
dump_dir = os.path.expanduser('~') + '/Thesis/experiment/dumps/Dataset'

ml_dataset = pickle.load(open(os.path.join(dump_dir, 'ml-20m-first-10000'), 'rb'))
lt_dataset = pickle.load(open(os.path.join(dump_dir, 'lt-first-10000'), 'rb'))

d1 = ml_dataset.info()
d2 = lt_dataset.info()
tag_set1 = d1.tags_set
tag_set2 = d2.tags_set
all_tag_set = tag_set1.intersection(tag_set2)
print('tags overlapping: {}'.format(len(all_tag_set)))

# ml_dataset.cut(limits=100)
# lt_dataset.cut(limits=100)

biased = False
n_factors = 100
n_epochs = 50
lr_all = 0.01
reg_all = 0.01
n_topics = 10
n_lda_iter = 2000
alpha = 0.02
eta = 0.01
dump_info = 'lt-unb-glo-01lr-10parts'

algo1 = SVD(biased=biased, n_factors=n_factors,
            n_epochs=n_epochs, lr_all=lr_all, reg_all=reg_all)

algo2 = ItemTopics(biased=biased, n_factors=n_factors,
                   n_epochs=n_epochs, lr_all=lr_all, reg_all=reg_all, n_topics=n_topics, n_lda_iter=n_lda_iter, eta=eta, alpha=alpha)

algo3 = ItemRelTags(biased=biased, n_factors=n_factors,
                    n_epochs=n_epochs, lr_all=lr_all, reg_all=reg_all)

algo4 = CrossItemTopics(biased=biased, n_factors=n_factors, n_epochs=n_epochs, lr_all=lr_all,
                        reg_all=reg_all, n_topics=n_topics, n_lda_iter=n_lda_iter, eta=eta, alpha=alpha)

algo5 = UserItemTags(biased=biased, n_factors=n_factors,
                     n_epochs=n_epochs, lr_all=lr_all, reg_all=reg_all)

algo6 = UserItemRelTags(biased=biased, n_factors=n_factors,
                        n_epochs=n_epochs, lr_all=lr_all, reg_all=reg_all)

algo7 = CrossItemRelTags(biased=biased, n_factors=n_factors,
                         n_epochs=n_epochs, lr_all=lr_all, reg_all=reg_all)
# Evaluate performances of our algorithm on the dataset.
# print_perf(evaluate(algo1, dataset=ml_dataset, measures=['RMSE', 'MAE']))
# print_perf(evaluate(algo2, dataset=ml_dataset, measures=['RMSE', 'MAE']))
# print_perf(evaluate(algo3, dataset=ml_dataset, measures=['RMSE', 'MAE']))
# print_perf(evaluate(algo4, dataset=ml_dataset,
#                     aux_dataset=lt_dataset, measures=['RMSE', 'MAE']))
# print_perf(evaluate(algo5, dataset=ml_dataset, measures=['RMSE', 'MAE']))
# print_perf(evaluate(algo6, dataset=ml_dataset, measures=['RMSE', 'MAE']))

perf1 = evaluate_parts(algo1, dataset=lt_dataset, measures=[
                       'RMSE', 'MAE'], trainset_parts=10, with_dump=True, dump_info=dump_info)
perf2 = evaluate_parts(algo2, dataset=lt_dataset, measures=[
                       'RMSE', 'MAE'], trainset_parts=10, with_dump=True, dump_info=dump_info)
perf3 = evaluate_parts(algo3, dataset=lt_dataset, measures=[
                       'RMSE', 'MAE'], trainset_parts=10, with_dump=True, dump_info=dump_info)
perf4 = evaluate_parts(algo5, dataset=lt_dataset, measures=[
                       'RMSE', 'MAE'], trainset_parts=10, with_dump=True, dump_info=dump_info)
perf5 = evaluate_parts(algo6, dataset=lt_dataset, measures=[
                       'RMSE', 'MAE'], trainset_parts=10, with_dump=True, dump_info=dump_info)
perf6 = evaluate_parts(algo4, dataset=lt_dataset, aux_dataset=ml_dataset, measures=[
                       'RMSE', 'MAE'], trainset_parts=10, with_dump=True, dump_info=dump_info)
perf7 = evaluate_parts(algo7, dataset=lt_dataset, aux_dataset=ml_dataset, measures=[
                       'RMSE', 'MAE'], trainset_parts=10, with_dump=True, dump_info=dump_info)



