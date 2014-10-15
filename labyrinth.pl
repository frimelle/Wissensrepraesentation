r:-['/path/to/file/labyrinth.pl'].

weg(3, 100).
weg(100, 1).
weg(100, 101).
weg(101, 2).
weg(101, 4).
isEnd(4).


lab(100, 1, Liste).
lab(A, B, Liste):-
	not(weg(A, B)),
	weg(A, X),
	lab(X, B, Liste),
	Liste = [Liste | X].

labB(101, 4, List):-
	List = 4.

labB(A, B, Liste):-
	not(weg(A, B)),
	weg(A, X),
	labB(X, B, Wegpunkte),
	Liste = [X | Wegpunkte].
	
	





myLength(Liste, X):-
Liste \= [],
Liste = [_Erst | Rest],
myLength(Rest, Y),
X is Y + 1.
myLength([],0).


