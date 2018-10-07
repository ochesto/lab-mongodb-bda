
#!/bin/bash

pyuic5 -x menu_window.ui -o menu_window.py

pyuic5 -x create_movie_window.ui -o create_movie_window.py

pyuic5 -x show_movie_window.ui -o show_movie_window.py

pyuic5 -x update_movie.ui -o update_movie_window.py

pyuic5 -x delete_movie_window.ui -o delete_movie_window.py

pyuic5 -x create_company_window.ui -o create_company_window.py


