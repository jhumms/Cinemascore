# Cinemascore-api
This is the unofficial API for getting movies from the Cinemascore website. This is the easiest way to get movies from Cinemascore. 

The code comes with two functions:
1. Allows for you to search for whatever movie you want:
```
import cinemascore
cinemascore.search("planet")
[{'TITLE': 'DAWN OF THE PLANET OF THE APES', 'GRADE': 'A-', 'YEAR': '2014'}, {'TITLE': 'ESCAPE FROM PLANET EARTH', 'GRADE': 'B+', 'YEAR': '2013'}, {'TITLE': 'PLANET 51', 'GRADE': 'B+', 'YEAR': '2009'}, {'TITLE': 'PLANET OF THE APES', 'GRADE': 'B-', 'YEAR': '2001'}, {'TITLE': 'RED PLANET', 'GRADE': 'C', 'YEAR': '2000'}, {'TITLE': 'RISE OF THE PLANET OF THE APES', 'GRADE': 'A-', 'YEAR': '2011'}, {'TITLE': 'TREASURE PLANET', 'GRADE': 'A-', 'YEAR': '2002'}, {'TITLE': 'VALERIAN AND THE CITY OF A THOUSAND PLANETS', 'GRADE': 'B-', 'YEAR': '2017'}, {'TITLE': 'WAR FOR THE PLANET OF THE APES', 'GRADE': 'A-', 'YEAR': '2017'}, {'TITLE': 'WHAT PLANET ARE YOU FROM?', 'GRADE': 'C+', 'YEAR': '2000'}]
```

2. This returns all movies on the website (will take some time to run). 

```
all_movies()
```




