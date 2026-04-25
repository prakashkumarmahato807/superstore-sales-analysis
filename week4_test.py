# Week 4 - Interactive API Tester

import requests

print("=" * 45)
print("   SPAM DETECTOR - API TESTER READY!")
print("=" * 45)
print("Type your message — API will check it!")
print("Type 'exit' to quit")
print("=" * 45)

while True:
    print("\n--- Enter Message ---")
    user_message = input("Your message: ")

    if user_message.lower() == 'exit':
        print("Goodbye!")
        break

    if user_message.strip() == "":
        print("Please type something!")
        continue

    try:
        # API ko message bhejo
        response = requests.post(
            'http://localhost:5000/predict',
            json={'message': user_message}
        )

        # Result lo
        data = response.json()

        print("\n" + "=" * 45)
        print(f"  Message  : {data['message']}")
        print(f"  Result   : {data['result']}")
        print(f"  Warning  : {data['warning']}")

        if data['result'] == 'SPAM':
            print("  Status   : SPAM DETECTED!")
        else:
            print("  Status   : SAFE MESSAGE!")

        print("=" * 45)

    except Exception as e:
        print("Error — Make sure week4_api.py is running!")
        print("Open a new terminal and run: py -3.12 week4_api.py")