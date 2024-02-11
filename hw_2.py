import pandas as pd


if __name__ == "__main__":


    # Define data as a dictionary
    data = {
        'Name': ['John', 'Anna', 'Peter', 'Linda'],
        'Age': [28, 34, 29, 32],
        'City': ['New York', 'Paris', 'Berlin', 'London']
    }

    # Create a DataFrame
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df)
