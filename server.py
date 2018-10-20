from flask import Flask
from flask import request
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World!'

#docker run -d -p 5000:5000 sortapp

@app.route('/sort', methods = ['POST'])
def sort_post_json_handler():
    print (request.is_json)
    content = request.get_json()
    unsorted_array = content['array']
    sorted_array = bubble(unsorted_array)
    print sorted_array
    sorted_array = ', '.join(str(x) for x in sorted_array)
    sorted_array = '[' + sorted_array + ']'
    return sorted_array #return JSON of sorted:<sorted_array>


def bubble(bad_list):
    #unicode to string:
    bad_list = str(bad_list)
    bad_list = bad_list.translate(None,'[nil]')
    bad_list = bad_list.replace(', ,', ',')
    flat_list = [int(i) for i in bad_list.split(',')]
    print bad_list
    print type(bad_list)

    #flatten the list
    print flat_list
    length = len(flat_list) - 1
    constraint_length = 10000
    if length >= constraint_length:
        return 'array is too long'

    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if flat_list[i] > flat_list[i+1]:
                sorted = False
                flat_list[i], flat_list[i+1] = flat_list[i+1], flat_list[i]

    return flat_list

if __name__ == '__main__':
    app.run(host='0.0.0.0')      