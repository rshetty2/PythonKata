from flask import Flask, render_template,request


app = Flask(__name__)


@app.route('/about',methods=['GET','POST'])
def index():
    request_method = request.method
    request_method_list=['GET','POST','PUT']
    return render_template('about.html', request_methods=request_method_list)
    #return render_template('about.html', len=len(request_method_list),request_methods=request_method_list)

'''
@app.route('/<int:name>')
def say_hello(name):
    return f'Hello {name}'
'''

if __name__ == "__main__":
    app.run(debug=True)