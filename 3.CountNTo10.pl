count_to_10(N) :-
    N =< 10,
    write(N), nl,
    Next is N + 1,
    count_to_10(Next).
count_to_10(_).
