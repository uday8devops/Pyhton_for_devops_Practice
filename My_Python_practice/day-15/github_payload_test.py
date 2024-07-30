
# This is ssimple program to understand the payload, that we are getting from github (webhook)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    payload = request.json

    # Print the complete payload received from GitHub
    # print(payload)

    
    # To learn How to iterate over the payload

    # Iterarte over the payload(To Filter) and Print the "comment-body" from complete JSON payload received from GitHub
    
    print(payload["comment"]["body"])


    # Respond with a success status
    return jsonify({'message': 'Payload received'}), 200

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

# host this in an EC2-instance and use the below URL as webhook in Git-Hub 

# http://ec2-13-235-135-168.ap-south-1.compute.amazonaws.com:5000/webhook 

# Replace this < ec2-13-235-135-168.ap-south-1.compute.amazonaws.com > with your EC2 instance DNS name 
