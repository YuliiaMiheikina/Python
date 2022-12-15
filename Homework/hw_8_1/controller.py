from sort import sort,get_data
from view import get_number_operation,get_data
from w_r import read_file,write_file
from main import sort_data


def button():
    return sort_data(get_number_operation,read_file,write_file,sort,get_data,get_data)