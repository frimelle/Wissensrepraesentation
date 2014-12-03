r:-['WR-Uebung2.pl'].
:-ensure_loaded('ops5_interpreter(v8_6).pl').

% Regeln aus der Problembeschreibung

:-build(r1, if, (karte(gueltig), versuche(nicht_ueberschritten), pin(richtig), betrag(nicht_ueber_Maximum),
		kontostand(ausreichend)), then, (make(auszahlung(erfolgt)), make(kartenrueckgabe(erfolgt)))).
:-build(r2, if, (karte(ungueltig)), then, (make(auszahlung(nicht_erfolgt)), make(kartenrueckgabe(erfolgt)))).
:-build(r3, if, (versuche(ueberschritten)), then, (make(auszahlung(nicht_erfolgt)), make(kartenrueckgabe(nicht_erfolgt)))).
:-build(r4, if, (pin(falsch)), then, (make(auszahlung(nicht_erfolgt)), make(kartenrueckgabe(erfolgt)))).
:-build(r5, if, (betrag(ueber_Maximum)), then, (make (auszahlung(nicht_erfolgt)), make(kartenrueckgabe(erfolgt)))).
:-build(r6, if, (kontostand(nicht_ausreichend), then, (make(auszahlung(nicht_erfolgt)), make(kartenrueckgabe(erfolgt)))).


:-make(betrag(nicht_ueber_Maximum)).
:-make(karte(gueltig)).
:-make(versuche(nicht_ueberschritten)).
:-make(pin(richtig)).
:-make(kontostand(ausreichend)).

:-build(frage,if,(auszahlung(erfolgt)), then, (writeln('Geld erhalten'), halt)).
:-build(frage,if,(auszahlung(nicht_erfolgt)), then, (writeln('Geld nicht erhalten'), halt)).