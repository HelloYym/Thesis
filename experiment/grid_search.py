import os
from surprise import Dataset
from surprise import SVD, UserItemTags, UserItemGenomeTags, ItemRelTags
from surprise import GridSearch

import numpy as np


# dataset
dataset_path = os.path.expanduser('./Dataset/ml-20m/')
data = Dataset(dataset_path=dataset_path, tag_genome=False)
data.split(n_folds=3)
data.info()


param_grid = {'n_factors': np.arange(10, 50, 10), 'lr_all': [
    0.01, ], 'reg_all': [0.05, ], 'n_epochs': [20, ]}

grid_search0 = GridSearch(ItemRelTags, param_grid, measures=['RMSE', 'MAE'])
# grid_search1 = GridSearch(SVD, param_grid, measures=['RMSE', 'MAE'])
# grid_search2 = GridSearch(UserItemTags, param_grid, measures=['RMSE', 'MAE'])
# grid_search3 = GridSearch(UserItemGenomeTags, param_grid, measures=['RMSE', 'MAE'])

grid_search0.evaluate(data)
# grid_search1.evaluate(data)
# grid_search2.evaluate(data)
# grid_search3.evaluate(data)

print("----ItemRelTags----")
grid_search0.print_perf()
# print("----SVD----")
# grid_search1.print_perf()
# print('----UserItemTags----')
# grid_search2.print_perf()
# print('----UserItemGenomeTags----')
# grid_search3.print_perf()
