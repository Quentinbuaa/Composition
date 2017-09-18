#!/usr/bin/python

from generate_testcase import *

def MR_1(a = 1, b = 1, matrix=[[1]]):
    row = len(matrix)
    column = len(matrix[0])
    follow_up_matrix = []
    for i in range(row):
        row = []
        for j in range(column):
            row.append(matrix[i][j]*a+b)
        follow_up_matrix.append(row)
    return follow_up_matrix

def main():
    a = 3.1 # the slope
    b = 2.2 # the interception

    num_attribute = 4  # number of attribute
    num_training_instances = 100  # number of training samples
    num_testing_instances = 10  # number of testing samples

    matrix_1 = create_training_attribute_matrix(num_attribute, num_training_instances)
    follow_up_matrix_1 = MR_1(a, b , matrix_1)
    matrix_2 = create_training_label_matrix(1, num_training_instances)
    matrix_3 = create_testing_attribute_matrix(num_attribute, num_testing_instances)
    follow_up_matrix_3 = MR_1(a, b , matrix_3)
    matrix_4 = create_testing_label_matrix(1, num_testing_instances)

    try:
        training_dataset = merge_matrix(matrix_1, matrix_2)
        follow_up_training_dataset = merge_matrix(follow_up_matrix_1, matrix_2)
        testing_dataset = merge_matrix(matrix_3, matrix_4)
        follow_up_testing_dataset = merge_matrix(follow_up_matrix_3, matrix_4)
        generate_training_dataset("training.arff", training_dataset)
        generate_testing_dataset("testing.arff", testing_dataset)
        generate_dataset("follow_up_training.arff", follow_up_training_dataset)
        generate_dataset("follow_up_testing.arff", follow_up_testing_dataset)

    except Exception as e:
        print(e.args)
        exit(-1)




if __name__ == "__main__":
    main()