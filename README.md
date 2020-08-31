# song2
Musical Works Aggregator

## Project setup
1) ```git clone https://github.com/ZhanaraDev/song2.git```
2) ```cd song2/```
3) ```docker-compose up```

## To run music works insertion/reconcilation command
```docker-compose exec django python manage.py insert_musical_works```

## APIs
1) http://0.0.0.0:8000/api/musical_works/ - list of all musical works.
2) http://0.0.0.0:8000/api/musical_works/<: iswc :>/music_by_iswc/ - get musical work by iswc
