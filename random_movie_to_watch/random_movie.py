import requests
from bs4 import BeautifulSoup as bs
import random


def get_random_movie():
    random_num = random.randint(1, 5000)

    page_with_movie = requests.get(
        f'https://letterboxd.com/prof_ratigan/list/top-5000-films-of-all-time-calculated/page/{int(random_num / 100) + 1}/')
    soup = bs(page_with_movie.text, 'html.parser')

    movie = soup.select('.numbered-list-item')[abs(random_num) % 100 - 1]

    name_of_movie = movie.select('img')[0]['alt']
    link_to_movie = "https://letterboxd.com" + movie.select('div')[0]['data-target-link']

    if is_movie_in_watchlist(name_of_movie, link_to_movie):
        get_random_movie()
    else:
        write_movie_in_file(name_of_movie, link_to_movie)
        print(f'Your random movie: \n'
              f'{name_of_movie} ({random_num})\n'
              f'link -> {link_to_movie}\n')


def write_movie_in_file(movie, link):
    watchlist = open("watchlist.txt", "a", encoding="utf8")
    watchlist.write(f'"{movie}": {link}\n')
    watchlist.flush()
    watchlist.close()


def is_movie_in_watchlist(movie, link):
    check_line = f'"{movie}": {link}\n'
    watchlist = open("watchlist.txt", "r", encoding="utf8")
    watchlist_lines = watchlist.readlines()
    watchlist.close()

    if len(watchlist_lines) == 5000:
        print("You watched all the films!.. Or you have a giant watchlist")
        exit()

    return check_line in watchlist_lines


def show_watchlist():
    f = open('watchlist.txt', 'r')
    print(f.read())
    f.close()


actions = {
    1: get_random_movie,
    2: show_watchlist,
    3: False
}

if __name__ == "__main__":
    print("This is a randomizer for selecting a movie from the list of Top 5,000 Films of All Time\n"
          "(Link to top: https://letterboxd.com/prof_ratigan/list/top-5000-films-of-all-time-calculated/)\n"
          "Each randomly selected movie is added to the watchlist file")

    flag = True

    while flag:
        answer = input("What do you want?\n"
                       "1 - get random movie;\n"
                       "2 - show watchlist;\n"
                       "3 - exit\n")
        if not answer.isdigit() or int(answer) not in actions:
            print("Please choose from the list")
        elif answer == "3":
            flag = actions[int(answer)]
        else:
            actions[int(answer)]()
