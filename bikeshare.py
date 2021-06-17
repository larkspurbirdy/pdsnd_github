import time
import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None)

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITIES = ['chicago', 'new york city', 'washington']
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']
YN = ['yes', 'no']


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('                                               $"   *.\n                   d$$$$$$$P                   $    J\n                       ^$.                     4r  "\n                       d"b                    .db\n                      P   $                  e" $\n             ..ec.. ."     *.              zP   $.zec..\n         .^        3*b.     *.           .P" .@"4F      "4\n       ."         d"  ^b.    *c        .$"  d"   $         %\n      /          P      $.    "c      d"   @     3r         3\n     4        .eE........$r===e$$$$eeP    J       *..        b\n     $       $$$$$       $   4$$$$$$$     F       d$$$.      4\n     $       $$$$$       $   4$$$$$$$     L       *$$$"      4\n     4         "      ""3P ===$$$$$$"     3                  P\n      *                 $       """        b                J\n       ".             .P                    %.             @\n         %.         z*"                      ^%.        .r"\n            "*==*""                             ^"*==*""   Gilo94\'\n    \nHello! Let\'s explore some US bikeshare data!\n')
    # Get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter one of these cities: Chicago, New York City, or Washington --> ').lower()
    while city not in CITIES:
        city = input('Oops! That\'s not a valid entry. Enter Chicago, New York City, or Washington --> ').lower()

    # Get user input for month (all, january, february, ... , june)
    month = input('Now enter a month between January and June, or type "all" to see data for all months. --> ').lower()
    while month not in MONTHS:
        month = input('Oops! That\'s not a valid entry. Enter a month between January and June, or type "all". --> ').lower()
    # Get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Finally, enter a day of the week, or type "all" to see data for all days. --> ').lower()
    while day not in DAYS:
        day = input('Oops! That\'s not a valid entry. Enter a day of the week, or type "all". --> ').lower()

    print('~'*40)
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
    df['Month'] = df['Start Time'].dt.month
    df['Day_Of_Week'] = df['Start Time'].dt.weekday_name
    df['Hour'] = df['Start Time'].dt.hour
    df['Route'] = "From " + df['Start Station'] + " to " + df['End Station']
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['Month'] == month]
    if day != 'all':
        df = df[df['Day_Of_Week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    common_month = df['Month'].mode()[0]
    common_month = MONTHS[common_month - 1].title()
    print('The most common month of travel is: {}'.format(common_month))

    # Display the most common day of week
    common_day_of_week = df['Day_Of_Week'].mode()[0]
    print('The most common day of the week to travel is: {}'.format(common_day_of_week))

    # Display the most common start hour
    common_hour = df['Hour'].mode()[0]
    print('The most common hour to travel is: {}:00'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("The most popular starting station is: {}".format(common_start))

    # Display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("The most popular end station is: {}".format(common_end))

    # Display most frequent combination of start station and end station trip
    common_route = df['Route'].mode()[0]
    print("The most popular trip is: {}".format(common_route))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('Calculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    duration_sum = df['Trip Duration'].sum()
    def sec_conversion(seconds):
        """Converts seconds to year, day, hour, and minute"""
        seconds_in_year = 31536000
        seconds_in_day = 86400
        seconds_in_hour = 3600
        seconds_in_minute = 60
        years = int(seconds // seconds_in_year)
        days = int((seconds - (years * seconds_in_year)) // seconds_in_day)
        hours = int((seconds - (years * seconds_in_year) - (days * seconds_in_day)) // seconds_in_hour)
        minutes = int((seconds - (years * seconds_in_year) - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute)
        return "{} years, {} days, {} hours, {} minutes".format(years, days, hours, minutes)

    print("The total duration of all trips is: {}".format(sec_conversion(duration_sum)))

    # Display mean travel time
    duration_mean = df['Trip Duration'].mean()
    print("The average trip duration is: {} minutes".format(int(duration_mean/60)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('~'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    if 'Gender' not in df:
        print('Calculating User Stats...\n\nSorry! User statistics are not available for Washington.')
    else:
        print('\nCalculating User Stats...\n')
        start_time = time.time()

        # Display counts of user types
        user_type_count = df['User Type'].value_counts().to_string()
        print('The total count of each user type are: \n{}'.format(user_type_count))

        # Display counts of gender
        gender_count = df['Gender'].value_counts().to_string()
        print('\nThe total count of each gender are: \n{}'.format(gender_count))

        # Display earliest, most recent, and most common year of birth
        earliest_birth = int(df['Birth Year'].min())
        recent_birth = int(df['Birth Year'].max())
        common_birth = int(df['Birth Year'].mode()[0])
        print('\nThe oldest user was born in {}, the youngest user was born in {}, and the most common year of birth is {}.'.format(earliest_birth, recent_birth, common_birth))

        print("\nThis took %s seconds." % (time.time() - start_time))
        print('~'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        #Display raw data by 10 lines at a time
        raw_data = input('\nWould you like to view 10 lines of raw data? Enter yes or no.\n')
        while raw_data not in YN:
            raw_data = input('Oops! That\'s not a valid entry. Enter yes or no.\n').lower()
        dstart = 0
        dend = 10
        while raw_data.lower() != 'no':
            print(df.iloc[dstart:dend, :])
            dstart += 10
            dend += 10
            raw_data = input('\nWould you like to view 10 more lines? Enter yes or no.\n')

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print("Have a nice day!")
            break


if __name__ == "__main__":
	main()
