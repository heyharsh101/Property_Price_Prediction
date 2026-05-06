import os
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # Import Pillow for image handling
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Load and preprocess data
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
EXCEL_PATH = os.path.join(BASE_DIR, 'Property_Price_Pridiction.xlsx')

df = pd.read_excel(EXCEL_PATH)
df = df.drop(columns=['ocean_proximity'])
df.dropna(inplace=True)

# Prepare training data
X_multi = df[['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income']]
y_multi = df['median_house_value']
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)

# Train model
multi_model = LinearRegression()
multi_model.fit(X_train_multi, y_train_multi)

# Function to predict house value
def predict_house_value():
    try:
        user_data = np.array([[
            float(entry_longitude.get()),
            float(entry_latitude.get()),
            float(entry_age.get()),
            float(entry_rooms.get()),
            float(entry_bedrooms.get()),
            float(entry_population.get()),
            float(entry_households.get()),
            float(entry_income.get())
        ]])
        
        predicted_value = multi_model.predict(user_data)[0]
        messagebox.showinfo("Prediction Result", f"Predicted Median House Value: ${predicted_value:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")

# Create GUI app
root = tk.Tk()
root.title("House Value Predictor")
root.geometry("400x500")

# Load background image if present in the project folder
bg_image_path = os.path.join(BASE_DIR, 'download (2).jpg')
if os.path.exists(bg_image_path):
    image = Image.open(bg_image_path)
    image = image.resize((400, 500))
    bg_photo = ImageTk.PhotoImage(image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(relwidth=1, relheight=1)
else:
    root.configure(bg='lightgray')

# Create input fields
tk.Label(root, text="Longitude:", bg="lightgray").pack()
entry_longitude = tk.Entry(root)
entry_longitude.pack()

tk.Label(root, text="Latitude:", bg="lightgray").pack()
entry_latitude = tk.Entry(root)
entry_latitude.pack()

tk.Label(root, text="Housing Median Age:", bg="lightgray").pack()
entry_age = tk.Entry(root)
entry_age.pack()

tk.Label(root, text="Total Rooms:", bg="lightgray").pack()
entry_rooms = tk.Entry(root)
entry_rooms.pack()

tk.Label(root, text="Total Bedrooms:", bg="lightgray").pack()
entry_bedrooms = tk.Entry(root)
entry_bedrooms.pack()

tk.Label(root, text="Population:", bg="lightgray").pack()
entry_population = tk.Entry(root)
entry_population.pack()

tk.Label(root, text="Households:", bg="lightgray").pack()
entry_households = tk.Entry(root)
entry_households.pack()

tk.Label(root, text="Median Income:", bg="lightgray").pack()
entry_income = tk.Entry(root)
entry_income.pack()

tk.Button(root, text="Predict House Value", command=predict_house_value, bg="lightblue").pack()

root.mainloop()
