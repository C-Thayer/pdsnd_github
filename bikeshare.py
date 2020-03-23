import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

options = ['chicago', 'new york city', 'washington']
months = ['all','january', 'february','march','april','may','june']
DOW = ['all', 'monday', 'tuesday', 'wednesday',
       'thursday', 'friday', 'saturday', 'sunday']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    message = '''Invalid option please try again.'''

    city = input("Please select a city: Chicago, New York City, or Washington: ").strip().lower()

    while city not in options:
        print(message)
        city = input("Please select a city: Chicago, New York City, or Washington: ").strip().lower()

    
    # TO DO: get user input for month (all, january, february, ... , june)
    
    month = input("Please enter a valid month (January - June) or use 'all' to choose all months: ").strip().lower()

    while month not in months:
        print("Invalid input please try again.")
        month = input("Please enter a valid month (January - June)  or use 'all' to choose all months: ").strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day = input("Please enter a valid day or use 'all' to choose all days in the week: ").strip().lower()

    while day not in DOW:
        print("Invalid input please try again.")
        day = input("Please enter a valid day or use 'all' to choose all days in the week: ").strip().lower()

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].value_counts().idxmax()
    print("The most common month is \n", common_month)
    # TO DO: display the most common day of week
    common_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of the week is \n", common_week)
    # TO DO: display the most common start hour
    common_day = df['hour'].value_counts().idxmax()
    print("The most common hour is \n", common_day)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].value_counts().idxmax()
    print("The most common starting station is: \n", common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].value_counts().idxmax()
    print("The most common ending station is: \n", common_end)

    # TO DO: display most frequent combination of start station and end station trip
    combined_station = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most used starting and ending stations are: \n", combined_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print("Total Travel Time: \n", travel_time)
    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Average Travel Time: \n", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Number of User Types: \n", user_types)
    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts()
        print("Number of Gender Types: \n", gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        min_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode().iloc[0]
        
        print("Oldest birth year: \n", min_birth_year)
        print("Most recent birth year: \n", most_recent_birth_year)
        print("Most common birth year: \n", common_birth_year)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def input_data(df): 
    for x in df.head().iterrows():
        
        df_rows = input("Would you like to see a specific trip's raw data? Please answer 'yes' or 'no'. ").strip().lower()
        if df_rows.lower() != 'yes':
            break
        print(x)
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        input_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
