squares(N) :-
    N =< 20,
    Square is N * N,
    write('Square of '), write(N), write(' is '), write(Square), nl,
    Next is N + 1,
    squares(Next).
squares(_).
