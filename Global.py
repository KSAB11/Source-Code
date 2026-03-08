# Global market roulette 

import random

# 1. Database: Country: Stocks 1,2 and 3
markets = {
    "USA": ["NVIDIA", "Apple", "Tesla"],
    "Japan": ["Toyota", "Sony", "Nintendo"],
    "India": ["Reliance", "TCS", "HDFC Bank"],
    "S.Korea": ["Samsung", "SK Hynix", "Hyundai"],
    "Germany": ["SAP", "Siemens", "Mercedes"],
    "UK": ["Shell", "AstraZeneca", "Unilever"],
    "China": ["Tencent", "Alibaba", "BYD"],
    "Taiwan": ["TSMC", "Foxconn", "MediaTek"],
    "Canada": ["Royal Bank", "Shopify", "Enbridge"],
    "Hong Kong": ["AIA Group", "Meituan", "HSBC"]
}

def stock():
    country = random.choice(list(markets.keys()))
    picked = random.choice(markets[country])
    return country, picked

if __name__ == "__main__":
    
    # User interface, greetings
    print("--- WELCOME TO STOCK ROULETTE ---")

    while True:
        user_input = input("\nPress 1 to spin (or 2 to quit): ")
        
        if user_input == '1':
            country_name, stock_name = stock()
            print(f"\nResult: {stock_name} ({country_name})")
            
        # Exiting the program    
        elif user_input == '2':
            print("\nThank you!")
            break
        
        # Handling unexpected input
        else:
            print("Invalid! Press 1 or 2.")
            