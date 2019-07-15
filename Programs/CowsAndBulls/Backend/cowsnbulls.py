#cows and bulls
import random
from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/getcowbull', methods=['GET'])
def getcowbull():
    chance = int(request.args.get('chance'))
    if chance==1:
        number = ''.join(random.sample('0123456789',4))
        #print(random.randint(1000,9999))
        #print(number)
    else:
        number = request.args.get('chknum') 
    num_dict = {}
    for i in range(0,4):
        a=number[i]
        num_dict[i+1] = a
        #print(num_dict)
        #for j in range(10):
    
    cows=0
    bulls=0
    n = request.args.get('number')
    
    print(chance)
    n_dict={}
    for i in range(0,4):
        n_dict[i+1] = n[i]
    bull_items = {k:num_dict[k] for k in num_dict if k in n_dict and num_dict[k]==n_dict[k]}
    cow_items = {k:num_dict[k] for k in num_dict if num_dict[k] in n_dict.values() and num_dict[k]!=n_dict[k]}
    bulls=len(bull_items)
    cows=len(cow_items)
    print(bulls,' Bulls')
    print(cows,' Cows')
    result = {
        'cows' : cows,
        'bulls' : bulls,
        'num' : number,
        'chance': chance
    }
    if bulls==4 and cows==0:
        return({'msg':'Congrats..You guessed it right.'})
    elif chance != 8:
        return(jsonify(result))
    elif chance == 8:
        return({'msg':'oops you ran out of chances. The number is: '+ number})
# if guessed==0:
#     print('The correct ans is: '+ number)
# print('Want to play again. Press Y to continue. Press any other key to exit.')
# play=input()

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
    
