import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    def input_mod(input_print, error_print, enterable_list, get_value):
        while True:
            ret = input(input_print)
            ret = get_value(ret)
            if ret in enterable_list:
                return ret
            else:
                print(error_print)
    city = input_mod('Please input the city name:',
            'Error!Please input the correct city name.',
            ['chicago', 'new york city', 'washington'],
            lambda x: str.lower(x))
    month = input_mod('Please input month name:',
            'Error!Please input the correct month name.',
            ['all','january','february','march','april','may','june'],
            lambda x: str.lower(x))
    day = input_mod('Please input day name:',
            'Error!Please input the correct day name.',
            ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday'],
            lambda x: str.lower(x))
    

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
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
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
    popular_month = df['month'].mode()
    print('Most common month:',popular_month)

    # TO DO: display the most common day of week    
    popular_day = df['day_of_week'].mode()
    print('Most common day of week:',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()
    print('Most common start hour:',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].mode()
    print('Most commonly used start station:',start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].mode()
    print('Most commonly used end station:',end_station)

    # TO DO: display most frequent combination of start station and end station trip
    top = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print('The most frequent combination of start station and end station trip is {} to {}'.format(top[0], top[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = np.sum(df['Trip Duration'])
    print('Total travel time:',total_time)

    # TO DO: display mean travel time
    mean_time = np.mean(df['Trip Duration'])
    print('The mean travel time:',mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = pd.value_counts(df['User Type'])
    print('The user types:',user_type)

    # TO DO: Display counts of gender
    try:
        user_type = pd.value_counts(df['Gender'])
        print('The gender:',user_type)
    except:
        print('error')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        print('The earliest:',earliest)
    except:
        print('error')
    try:
        most_recent = df['Birth Year'].max()
        print('The most recent:',most_recent)
    except:
        print('error')
    try:
        popular_year = pd.value_counts(df['Birth Year']).mode()
        print('Most common year of birth:',popular_year)
    except:
        print('error')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()