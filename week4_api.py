# Week 4 - Flask API Server

from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
messages = [
    # SPAM messages (label = 1)
    "Congratulations you won 1 lakh rupees click here",
    "Free entry win cash prize call now",
    "You are selected for lottery claim your prize",
    "Win iPhone click this link now",
    "Urgent you have won a reward collect today",
    "Your account is credited with 10 crore click now",
    "You have received a cash reward of 5 lakh",
    "Claim your free gift today limited offer",
    "Your bank account has been credited with prize money",
    "Win big cash prize register now free entry",
    "Congratulations your number is selected for reward",
    "Get rich quick invest now guaranteed returns",
    "Your KYC is expired update now or account blocked",
    "OTP do not share with anyone your account will be blocked",
    "Loan approved instantly no documents required apply now",
    "Free recharge click this link now limited time",
    "Your electricity bill is due pay now or connection cut",
    "Winner winner you have been selected click here",
    "Send money now to claim your lottery prize",
    "Your UPI account will be blocked verify now",

    # NORMAL messages (label = 0)
    "Hey lets meet tomorrow",
    "Meeting at 5pm today please confirm",
    "Mom has made food please come home",
    "Project submission is due tomorrow",
    "Lets go watch a movie today",
    "Can you send me the assignment notes",
    "Bhai aaj gym chalein kya",
    "Your order has been delivered check doorstep",
    "Happy birthday have a great day",
    "Please call me when you are free",
    "Dinner is ready come home soon",
    "Can we reschedule our meeting to tomorrow",
    "Your package will arrive by tomorrow evening",
    "Good morning have a nice day",
    "Thanks for your help yesterday",
    "Please share the document with me",
    "Are you coming to the office today",
    "Your cab has arrived please come down",
    "Your food order is on the way",
    "See you at the station at 6pm",
]

labels = [
    1,1,1,1,1,1,1,1,1,1,
    1,1,1,1,1,1,1,1,1,1,
    0,0,0,0,0,0,0,0,0,0,
    0,0,0,0,0,0,0,0,0,0,
]

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)
model = MultinomialNB()
model.fit(X, labels)

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'status': 'running',
        'info': 'Spam Detector API is Ready!'
    })

# Predict route
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    message = data['message']

    X_test = vectorizer.transform([message])
    result = model.predict(X_test)[0]

    if result == 1:
        label = "SPAM"
        warning = "Be careful! This looks like a spam message."
    else:
        label = "Normal"
        warning = "This message looks safe!"

    return jsonify({
        'message': message,
        'result': label,
        'warning': warning
    })

print("=" * 45)
print("   SPAM DETECTOR API SERVER READY!")
print("=" * 45)
print("Server running at: http://localhost:5000")
print("Keep this terminal open!")
print("=" * 45)

app.run(debug=True)