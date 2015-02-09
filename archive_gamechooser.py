import simplejson as json
from urllib.request import urlopen
import random

def choose_page():
  """ Returns a string representation of an archive.org page """
  random.seed()
  page_number = random.randint(1, 200)
  url = "https://archive.org/advancedsearch.php?q=%28collection%3Aclassicpcgames+OR+mediatype%3Aclassicpcgames%29+AND+-mediatype%3Acollection&fl%5B%5D=creator&fl%5B%5D=date&fl%5B%5D=description&fl%5B%5D=identifier&fl%5B%5D=publicdate&fl%5B%5D=publisher&fl%5B%5D=subject&fl%5B%5D=title&fl%5B%5D=type&sort%5B%5D=titleSorter+desc&sort%5B%5D=&sort%5B%5D=&rows=50&indent=yes&output=json&page=" + str(page_number)
  html_string = urlopen(url).read()
  archive_json = json.loads(html_string)
  if archive_json['response']['numFound'] > archive_json['response']['start']:
    return archive_json
  else:
    print("Chose a page out of bounds. Trying again.")
    return choose_page()

def parse_page(archive_json):
  """Parse the page from archive.org.

  Arguments:
  archive_page -- a simplejson object

  Returns: a list of games from the API call
  """
  games = archive_json['response']['docs']
  return games

def choose_game(games):
  """Return a dictionary associated with a random game"""
  game = random.choice(games)
  return game

if __name__ == "__main__":
  archive_page = choose_page()
  game_list = parse_page(archive_page)
  chosen_game = choose_game(game_list)
  print("Title: " + chosen_game['title'])
  print("Description: " + chosen_game['description'])
  print("URL: http://archive.org/details/" + chosen_game['identifier'])
