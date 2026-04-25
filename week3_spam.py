# Spam Detector - Interactive Version

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Training data
messages = [
    "Congratulations you won 1 lakh rupees click here",
    "Free entry win cash prize call now",
    "You are selected for lottery claim your prize",
    "Win iPhone click this link now",
    "Urgent you have won a reward collect today",
    "Hey lets meet tomorrow",
    "Meeting at 5pm today please confirm",
    "Mom has made food please come home",
    "Project submission is due tomorrow",
    "Lets go watch a movie today",
]
labels = [1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
# 1 = Spam, 0 = Normal

# Train the model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(messages)
model = MultinomialNB()
model.fit(X, labels)

print("=" * 40)
print("  SPAM DETECTOR READY!")
print("=" * 40)
print("Type your message — I will tell you if it is SPAM or Normal!")
print("Type 'exit' to quit")
print("=" * 40)

# Keep asking for messages until user types exit
while True:
    user_message = input("\nYour message: ")

    if user_message.lower() == 'exit':
        print("Goodbye!")
        break

    if user_message.strip() == "":
        print("Please type something!")
        continue

    X_test = vectorizer.transform([user_message])
    result = model.predict(X_test)[0]

    if result == 1:
        print("SPAM DETECTED — Be careful!")
    else:
        print("NORMAL MESSAGE — Safe!")