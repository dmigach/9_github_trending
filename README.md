# Github trends

This script allows you to get github repositories with most stars for given time period, number of their open issues and repository URL.

## Prerequisites

The script is written in `Python 3`, so you'll need it's interpretator to run it.

## Install

To install all the necessary libraries to run the script just open your terminal, go to downloaded project directory and type:

    pip install -r requirements.txt

## Usage

To run the script type following in terminal:
    
    python github_trending.py

By default you'll get a table of top 20 repositories in last 7 days, but you can customize script run by adding arguments to call in form of

    python github_trending.py reppsitories_number days

For example, to get top 5 repositories in last 2 days type

    python github_trending.py 5 2

## Support

In case of any difficulties or questions please contact <dmitrygach@gmail.com>.


