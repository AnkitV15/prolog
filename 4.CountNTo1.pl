count_to_1(N) :-
    N >= 1,
    write(N), nl,
    Next is N - 1,
    count_to_1(Next).
count_to_1(_).
