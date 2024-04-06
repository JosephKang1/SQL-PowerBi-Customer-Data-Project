import csv
from faker import Faker
from datetime import datetime

# Create a Faker instance
fake = Faker()

# Define the number of customers you want to generate
num_customers = 10000

# Define the CSV file name
csv_file = "customer_data.csv"

# Define the CSV headers
headers = ["Customer Id", "First Name", "Last Name", "Email", "Phone", "Birthday", "Age", "Age Band", "Gender", "Occupation", "Education Level", "Company", "Country", "City", "Address", "Postal Code"]

# Define age bands
age_bands = [
    {"band": "18-25", "min_age": 18, "max_age": 25},
    {"band": "26-35", "min_age": 26, "max_age": 35},
    {"band": "36-45", "min_age": 36, "max_age": 45},
    {"band": "46-55", "min_age": 46, "max_age": 55},
    {"band": "56-65", "min_age": 56, "max_age": 65},
    {"band": "65+", "min_age": 66, "max_age": 120}
]

# Generate customer data and write to CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write headers to CSV file
    writer.writerow(headers)
    
    # Generate and write customer data to CSV file
    for _ in range(num_customers):
        customer_id = fake.uuid4()
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.email()
        phone = fake.phone_number()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=90)
        age = (datetime.now().date() - birthday).days // 365
        gender = fake.random_element(["Male", "Female"])
        
        # Assign age band
        for band in age_bands:
            if band["min_age"] <= age <= band["max_age"]:
                age_band = band["band"]
                break
        
        occupation = fake.job()
        education_level = fake.random_element(["High School", "Bachelor's Degree", "Master's Degree", "PhD"])
        company = fake.company()
        country = fake.country()
        city = fake.city()
        address = fake.street_address()
        postal_code = fake.postalcode()
        
        writer.writerow([customer_id, first_name, last_name, email, phone, birthday, age, age_band, gender, occupation, education_level, company, country, city, address, postal_code])

print(f"{num_customers} customer records have been generated and saved to '{csv_file}'.")
