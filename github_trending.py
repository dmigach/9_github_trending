import requests
import datetime
import tabulate
import argparse

GITHUB_REPOSITORY_API = 'https://api.github.com/search/repositories'


def get_date(days_ago):
    return datetime.date.today() - datetime.timedelta(days=days_ago)


def get_trending_repositories(top_count, api_url, days_ago):
    created_date = '{}{}'.format('created:>=', get_date(days_ago))
    params_for_request = {'q': created_date, 'sort': 'stars', 'order': 'desc'}
    repository_data = requests.get(api_url, params=params_for_request).json()
    top_trending_repositories = repository_data['items'][:top_count]
    return top_trending_repositories


def print_out_trending_repositories(repositories, days_ago):
    print('\nTop {} trending repositories created'
          ' in {} last days:\n'.format(number_of_repositories,
                                       days_ago))
    repositories_list = [
        [
            repository['name'],
            repository['stargazers_count'],
            repository['open_issues_count'],
            repository['html_url']
        ]
        for repository in repositories]
    headers = ['Name', 'Stars', 'Open issues', 'Link']
    print(tabulate.tabulate(repositories_list,
                            headers=headers,
                            tablefmt='psql'))


def parse_arguments():
    parser = argparse.ArgumentParser(description='Find out top trending '
                                                 'repositories')
    parser.add_argument('number', nargs='?', default=20,
                        type=int, help='number of repositories to print')
    parser.add_argument('days', nargs='?', default=7, type=int,
                        help='number of previous days to search')
    arguments = parser.parse_args()
    return arguments.number, arguments.days


if __name__ == '__main__':
    number_of_repositories, number_of_days = parse_arguments()
    repositories_to_print = get_trending_repositories(number_of_repositories,
                                                      GITHUB_REPOSITORY_API,
                                                      number_of_days)
    print_out_trending_repositories(repositories_to_print, number_of_days)
