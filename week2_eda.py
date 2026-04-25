# Week 2 - Interactive Data Visualization (EDA)

import pandas as pd
import matplotlib.pyplot as plt

# Training data
data = {
    'Area':  [500, 800, 1000, 1200, 1500, 1800, 2000, 2200, 2500, 3000],
    'Rooms': [1,   2,   2,    3,    3,    4,    4,    5,    5,    6   ],
    'Price': [20,  35,  45,   55,   70,   85,   95,   110,  130,  160 ]
}
df = pd.DataFrame(data)

print("=" * 45)
print("   INTERACTIVE GRAPH GENERATOR READY!")
print("=" * 45)
print("Enter your house details — Graph will update!")
print("Type 'exit' to quit")
print("=" * 45)

while True:
    print("\n--- Enter House Details ---")

    area_input = input("Enter Area (in sqft): ")
    if area_input.lower() == 'exit':
        print("Goodbye!")
        break

    rooms_input = input("Enter Number of Rooms: ")
    if rooms_input.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        area = float(area_input)
        rooms = int(rooms_input)

        if area <= 0 or rooms <= 0:
            print("Area and Rooms must be greater than 0!")
            continue

        # Price estimate karo simple formula se
        estimated_price = (area * 0.045) + (rooms * 5)

        print(f"\nEstimated Price: Rs. {estimated_price:.1f} Lakh")
        print("Generating graphs... please wait!")

        # ── GRAPH 1 — Area vs Price (user point highlight) ──
        plt.figure(figsize=(8, 5))
        plt.scatter(df['Area'], df['Price'],
                    color='blue', s=100, label='Existing Houses')
        plt.scatter(area, estimated_price,
                    color='red', s=200, zorder=5,
                    label=f'Your House ({area} sqft = Rs.{estimated_price:.1f}L)')
        plt.title('Area vs Price')
        plt.xlabel('Area (sqft)')
        plt.ylabel('Price (Lakh)')
        plt.legend()
        plt.grid(True)
        plt.savefig('graph1_area_price.png')
        plt.show()
        print("Graph 1 saved!")

        # ── GRAPH 2 — Rooms vs Price (user bar highlight) ──
        plt.figure(figsize=(8, 5))
        colors = []
        for r in df['Rooms']:
            if r == rooms:
                colors.append('red')
            else:
                colors.append('green')
        plt.bar(df['Rooms'], df['Price'], color=colors)
        plt.title('Rooms vs Price (Red = Your Selection)')
        plt.xlabel('Number of Rooms')
        plt.ylabel('Price (Lakh)')
        plt.grid(True)
        plt.savefig('graph2_rooms_price.png')
        plt.show()
        print("Graph 2 saved!")

        # ── GRAPH 3 — Price Comparison Bar Chart ──
        plt.figure(figsize=(8, 5))
        categories = ['Min Price', 'Average Price',
                      'Your House', 'Max Price']
        values = [df['Price'].min(), df['Price'].mean(),
                  estimated_price, df['Price'].max()]
        bar_colors = ['blue', 'green', 'red', 'orange']
        plt.bar(categories, values, color=bar_colors)
        plt.title('Price Comparison')
        plt.ylabel('Price (Lakh)')
        plt.grid(True)
        plt.savefig('graph3_comparison.png')
        plt.show()
        print("Graph 3 saved!")

        # ── Summary ──
        print("\n" + "=" * 45)
        print(f"  Area             : {area} sqft")
        print(f"  Rooms            : {rooms}")
        print(f"  Your Price       : Rs. {estimated_price:.1f} Lakh")
        print(f"  Market Min       : Rs. {df['Price'].min()} Lakh")
        print(f"  Market Average   : Rs. {df['Price'].mean()} Lakh")
        print(f"  Market Max       : Rs. {df['Price'].max()} Lakh")

        if estimated_price < df['Price'].mean():
            print("  Status           : Below Average Price")
        else:
            print("  Status           : Above Average Price")
        print("=" * 45)

    except ValueError:
        print("Please enter valid numbers only!")
        continue