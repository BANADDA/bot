import random

R_LIKE = "I love learning new things about the scientific world"


def unknown():
    response = ['Could you please re-phrase that?', '...', 'Sounds about right', 'What does that mean?'][random.randrange(4)]
     
     
    return response