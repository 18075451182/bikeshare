import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
citys = CITY_DATA.keys()
months = ['all','january', 'february', 'march', 'april', 'may', 'june']
days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
def input_mod(input_print,enterable_list):
    while True:
        ret = input(input_print).lower()
        if ret in enterable_list:
            break
    return ret
    print('-'*40)

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
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['hour'] = df['Start Time'].dt.hour
    df['trip'] = df['Start Station'] + df['End Station']
    if month != 'all':
        month = months.index(month)
        df = df[df['month'] == month]    
    if day != 'all':
        day = days.index(day) - 1
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    print('Most Frequent Times of Travel: ', months[df['month'].mode()[0]])
    
    # TO DO: display the most common day of week

    print('The most common day of week: ', days[df['day_of_week'].mode()[0] + 1])

    # TO DO: display the most common start hour

    print('The most common start hour: ',df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most commonly used start station: ',df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('The most commonly used end station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip

    print('The most frequent combination of start station and end station trip: ',df['trip'].mode()[0])   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('The total travel time: ',df['Trip Duration'].sum()) 

    # TO DO: display mean travel time
    print('The mean travel time: ',df['Trip Duration'].mean()) 

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The counts of user types:\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('The counts of gender:\n',df['Gender'].value_counts())
    except:
        print('The Washington dataset lacks the Gender columns')
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print('The earliest, most recent, and most common year of birth:',df['Birth Year'].min(),df['Birth Year'].max(),df['Birth Year'].mode()[0])
    except:
        print('The Washington dataset lacks the Birth Year columns')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city = input_mod('\n Enter the name of the city you want to analyze: chicago, new york city or washington.\n', citys)
        month = input_mod('\n Enter the name of the month you want to analyze: all,january, february, march, april, may, june.\n', months)
        day = input_mod('\n Enter the name of the day you want to analyze: all,monday,tuesday,wednesday,thursday,friday,saturday,sunday.\n', days)

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
