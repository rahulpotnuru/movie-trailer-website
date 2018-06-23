import movie
import open_trailer


def main():
    '''Function:
        Creating six movie objects and passing instance attributes to them.
       Args:
        None
       Returns:
        None'''

    matrix = movie.Movie('Matrix', 'The world is a simulation',
                         'https://goo.gl/8wvvf8', 'https://goo.gl/f6Qeha')

    star_wars = movie.Movie('Star Wars', 'The force awakens',
                            'https://goo.gl/zJ1Ve4', 'https://goo.gl/YG249N')

    toy_story = movie.Movie('Toy Story',
                            'A story of a boy and his toys that come to life',
                            'https://goo.gl/7RZSog', 'https://goo.gl/q92pYV')

    avatar = movie.Movie('Avatar', 'A marine on an alien planet',
                         'https://goo.gl/AxH37q', 'https://goo.gl/UcXQgR')

    deadpool = movie.Movie('Deadpool', 'Wait till you get a load of me',
                           'http://bit.ly/2eorTC7', 'https://goo.gl/EVY33t')

    ratatouille = movie.Movie('Ratatouille', 'A rat is a chef in Paris',
                              'https://goo.gl/bJJgTv', 'https://goo.gl/xaSxz3')

    movies = [matrix, star_wars, toy_story, avatar, deadpool, ratatouille]
    open_trailer.open_movies_page(movies)

if __name__ == '__main__':
    main()
