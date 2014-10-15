r:-[test].
a.
b.
qw(X,Z):-
number(X),
Z is sqrt(X).
f(0,1):-!. % To make sure it does not go on after this. Funktordarstellung
f(Z,F):- % Funktordarstellung
number(Z),
Z>0,
Z1 is Z-1,
f(Z1,F1),
F is F1*Z.
ist(X,Y) :- 
X is Y.
:- op(800, xfx, ist).
myLength(Liste, X):-
Liste \= [],
Liste = [_Erst | Rest],
myLength(Rest, Y),
X is Y + 1.
myLength([],0).