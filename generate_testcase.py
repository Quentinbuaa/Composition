#!/usr/bin/python

from shutil import copyfile
import random

def create_attribute_matrix(column = 4, row=100, lower_range = 1, upper_range = 20):
    matrix = []
    for i in range(row):
        row = []
        for j in range(column):
            row.append(random.randint(lower_range, upper_range))
        matrix.append(row)
    return matrix

def create_label_matrix(column =1, row = 100, nominal = [1, 2, 3, 4, 5]):
    matrix  = []
    for i in range(row):
        row = []
        for j in range(column):
            row.append(random.choice(nominal))
        matrix.append(row)
    return matrix

def merge_matrix(matrix_1, matrix_2):
    if not len(matrix_1) == len(matrix_2):
        raise Exception("In _merge_matrix: the column dimension is not the same")
    else:
        matrix = []
        for i in range(len(matrix_1)):
            matrix.append(matrix_1[i]+matrix_2[i])
        return matrix


def generate_dataset(filename, data_set):
    copyfile("header.arff" , filename )
    delimiter = ','   # the delimiter of the ARFF data format
    if len(data_set) is 0:
       raise Exception("In generate_dataset: the dataset size is 0")
    with open(filename, 'at') as f:
        count = 0
        length = len(data_set[0])
        for i in range(len(data_set)):
            for item in data_set[i]:
                count +=1
                f.write(str(item))
                if not count == length:
                    f.write(delimiter)
                else:
                    f.write('\n')
                    count = 0

def create_training_attribute_matrix(num_attribute, num_training_instances):
    return create_attribute_matrix(num_attribute, num_training_instances)

def create_testing_attribute_matrix(num_attribute, num_testing_instances):
    return create_attribute_matrix(num_attribute, num_testing_instances)

def create_training_label_matrix(num_target_class = 1,  num_training_instances =100):
    return create_label_matrix(num_target_class , num_training_instances)

def create_testing_label_matrix(num_target_class = 1,  num_testing_instances =100):
    return create_label_matrix(num_target_class , num_testing_instances)

def generate_training_dataset(filename, data_set):
    generate_dataset(filename, data_set)

def generate_testing_dataset(filename, data_set):
    generate_dataset(filename, data_set)



def main():
    num_attribute = 4 # number of attribute
    num_training_instances = 100 # number of training samples
    num_testing_instances  = 10  # number of testing samples

    matrix_1 = create_training_attribute_matrix(num_attribute, num_training_instances)
    matrix_2 = create_training_label_matrix(1,  num_training_instances)
    matrix_3 = create_testing_attribute_matrix(num_attribute, num_testing_instances)
    matrix_4 = create_testing_label_matrix(1, num_testing_instances)

    try:
        training_dataset = merge_matrix(matrix_1, matrix_2)
        testing_dataset = merge_matrix(matrix_3, matrix_4)
        generate_training_dataset("training.arff", training_dataset)
        generate_testing_dataset("testing.arff", testing_dataset)
    except Exception as e:
        print(e.args)
        exit(-1)


if __name__ == "__main__":
    main()