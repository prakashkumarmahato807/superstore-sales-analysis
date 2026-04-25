# Week 1 - House Price Prediction (Interactive Version)

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pandas as pd

# Training data
data = {
    'Area':  [500, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    'Rooms': [1,   2,   2,    3,    3,    4,    4,    5,    5,    6   ],
    'Price': [20,  35,  45,   55,   70,   85,   95,   110,  130,  160 ]
}
df = pd.DataFrame(data)

# Train the model
X = df[['Area', 'Rooms']]
y = df['Price']
model = LinearRegression()
model.fit(X, y)

print("=" * 45)
print("   HOUSE PRICE PREDICTOR READY!")
print("=" * 45)
print("Enter house details — I will predict the price!")
print("Type 'exit' to quit")
print("=" * 45)

# Keep asking until user types exit
while True:
    print("\n--- Enter House Details ---")

    # Area input
    area_input = input("Enter Area (in sqft): ")
    if area_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Rooms input
    rooms_input = input("Enter Number of Rooms: ")
    if rooms_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Validate - sirf numbers accept karo
    try:
        area = float(area_input)
        rooms = int(rooms_input)

        # Valid range check
        if area <= 0 or rooms <= 0:
            print("Area and Rooms must be greater than 0!")
            continue

        # Predict price
        predicted = model.predict([[area, rooms]])
        price = predicted[0]

        print("\n" + "=" * 45)
        print(f"  Area         : {area} sqft")
        print(f"  Rooms        : {rooms}")
        print(f"  Predicted Price : Rs. {price:.1f} Lakh")

        # Price category
        if price < 40:
            print("  Category     : Budget Home")
        elif price < 80:
            print("  Category     : Mid Range Home")
        elif price < 120:
            print("  Category     : Premium Home")
        else:
            print("  Category     : Luxury Home")

        print("=" * 45)

    except ValueError:
        print("Please enter valid numbers only!")
        continue