import pandas as pd
import numpy as np

# Generate 50 samples of real estate data
np.random.seed(42)

data = {
    'SquareFootage': np.random.randint(800, 4000, 50),
    'NumBedrooms': np.random.randint(1, 6, 50),
    'NumBathrooms': np.random.randint(1, 4, 50),
    'Location': np.random.choice(['Urban', 'Suburban', 'Rural'], 50),
    'Amenities': np.random.choice(['Pool', 'Gym', 'Park'], 50),
    'Price': 50000 + 200 * np.random.randn(50)
}

df = pd.DataFrame(data)

# Save the generated data to a CSV file
df.to_csv('real_estate_data.csv', index=False)

# Display the first few rows of the generated data
print(df.head())
