weiblich(sibylla).
weiblich(herrad).
weiblich(humilitas).
maennlich(wiligis).
maennlich(grigorss).
bruder(sibylla, wiligis).
schwester(wiligis, sibylla).
sohn(sibylla, grigorss).
sohn(wiligis, grigorss).
tochter(sibylla, herrad).
tochter(grigorss, herrad).
tochter(sibylla, humilitas).
tochter(grigorss, humilitas).
ehemann(sibylla,grigorss).




/*BASE1: Die Schwester eines Elternteils
*/
elternteil(X,Z) & schwester(Z, Y) => base1(X,Y).
/*BASE2: Die Tochter von Onkel oder Tante. .*/
(onkel(X,Z) '|' tante(X,Z)) & tochter(Z,Y) => base2(X,Y).
/*VETTER: Der Sohn von Onkel oder Tante.
*/
(onkel(X,Z) '|' tante(X,Z)) & sohn(Z,Y) => vetter(X,Y).
/*COUSINE: Synonym zu Base2.
*/
base2(X,Y) => cousine(X,Y).
/*COUSIN: Synonym zu Vetter.
*/
vetter(X,Y) => cousin(X,Y).
/*ONKEL: Der Bruder des Vaters oder der Mutter. */
(vater(X,Z) | mutter(X,Z)) & bruder(Z,Y) => onkel(X,Y).
/*TANTE: Die Schwester des Vaters oder der Mutter. */
(vater(X,Z) | mutter(X,Z)) & schwester(Z,Y) => tante(X,Y).
/*ELTERN: Vater und Mutter
vater(X,Y) &mutter(X, Z) => eltern(X,[Y,Z]).
*/
/*ELTERNTEIL: Vater oder Mutter..
*/
(vater(X,Z) | mutter(X,Z)) => elternteil(X,Z).
/*BRUDER: Männl. Kind des gemeinsamen Elternteils.
*/
elternteil(X,Z)& sohn(Z,Y) & Y\=X => bruder(X,Y).
/*SCHWESTER: Weibl. Kind des gemeinsamen Elternteils.
*/
elternteil(Y, Z) & tochter(Z, X) & Y \= X => schwester(Y, X).
/*NEFFE: Der Sohn des Bruders oder der Schwester.
*/
(bruder(X,Z) | schwester(X,Z))&sohn(Z,Y) => neffe(X,Y).
/*NICHTE: Die Tochter des Bruders oder der Schwester.
*/
(bruder(X,Z) | schwester(X,Z))&tochter(Z,Y) => nichte(X,Y).
/*GESCHWISTER: Bruder oder Schwester
*/
(bruder(X, Y) | schwester(X,Y)) => geschwister(X, Y).
/*VATER; Elternteil ist männlich
*/
elternteil(X, Y) & maennlich(Y) => vater(X,Y).
/*MUTTER; Elternteil und weiblich
*/
elternteil(X, Y) & weiblich(Y) => mutter(X,Y).
/*VATER/MUTTER-Beziehung zur Tochter */
tochter(X, Y) => vater(Y,X)&maennlich(X) | mutter(Y,X)& weiblich(X).
/*VATER/MUTTER-Beziehung zum Sohn */
sohn(X, Y) => vater(Y,X) &maennlich(X)| mutter(Y,X) & weiblich(X).
