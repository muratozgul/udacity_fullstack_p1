#!/usr/bin/env python
#
# Test cases for tournament.py

from tournament import *

def testDeleteMatches():
    deleteMatches()
    print "1. Old matches can be deleted."


def testDelete():
    deleteMatches()
    deletePlayers()
    print "2. Player records can be deleted."


def testCount():
    deleteMatches()
    deletePlayers()
    c = countPlayers()
    if c == '0':
        raise TypeError(
            "countPlayers() should return numeric zero, not string '0'.")
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "3. After deleting, countPlayers() returns zero."


def testRegisterTournament():
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    registerTournament("Chess 2016")
    c = countTournaments()
    if c != 1:
        raise ValueError(
            "After one tournament registers, countTournament() should be 1.")
    print "4a. After registering a tournament, countTournaments() returns 1."


def testRegister():
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    registerPlayer("Chandra Nalaar")
    c = countPlayers()
    if c != 1:
        raise ValueError(
            "After one player registers, countPlayers() should be 1.")
    print "4b. After registering a player, countPlayers() returns 1."


def testRegisterToTournament():
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    tournament_id = registerTournament("Chess 2016")
    player_id = registerPlayer("Chandra Nalaar")
    registerPlayerToTournament(player_id, tournament_id)
    c = countPlayersOfTournament(tournament_id)
    if c != 1:
        raise ValueError(
            "After one player registers to a tournament, countPlayersOfTournament() should be 1.")
    print "4c. After registering a player to a tournament, countPlayersOfTournament() returns 1."


def testRegisterCountDelete():
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    registerPlayer("Markov Chaney")
    registerPlayer("Joe Malik")
    registerPlayer("Mao Tsu-hsi")
    registerPlayer("Atlanta Hope")
    c = countPlayers()
    if c != 4:
        raise ValueError(
            "After registering four players, countPlayers should be 4.")
    deletePlayers()
    c = countPlayers()
    if c != 0:
        raise ValueError("After deleting, countPlayers should return zero.")
    print "5. Players can be registered and deleted."


def testRegisterToTournamentCountDelete():
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    p1 = registerPlayer("Markov Chaney")
    p2 = registerPlayer("Joe Malik")
    p3 = registerPlayer("Mao Tsu-hsi")
    p4 = registerPlayer("Atlanta Hope")
    t1 = registerTournament("PingPong 2016")
    registerPlayerToTournament(p1, t1)
    registerPlayerToTournament(p2, t1)
    registerPlayerToTournament(p3, t1)
    registerPlayerToTournament(p4, t1)
    c = countPlayersOfTournament(t1)
    if c != 4:
        raise ValueError(
            "After registering four players to a tournament, countTournamentPlayers should be 4.")
    deletePlayersOfTournament(t1)
    c = countPlayersOfTournament(t1)
    if c != 0:
        raise ValueError("After deleting players of a tournament, countTournamentPlayers should return zero.")
    print "5. Players can be registered to a tournament and deleted from a tournament."


def testStandingsBeforeMatches():
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    t1 = registerTournament("PingPongMasters 2016")
    p1 = registerPlayer("Melpomene Murray")
    p2 = registerPlayer("Randy Schwartz")
    rp1 = registerPlayerToTournament(p1, t1)
    rp2 = registerPlayerToTournament(p2, t1)
    standings = playerStandings(t1)
    if len(standings) < 2:
        raise ValueError("Players should appear in playerStandings even before "
                         "they have played any matches.")
    elif len(standings) > 2:
        raise ValueError("Only registered players should appear in standings.")
    if len(standings[0]) != 4:
        raise ValueError("Each playerStandings row should have four columns.")
    [(id1, name1, wins1, matches1), (id2, name2, wins2, matches2)] = standings
    if matches1 != 0 or matches2 != 0 or wins1 != 0 or wins2 != 0:
        raise ValueError(
            "Newly registered players should have no matches or wins.")
    if set([name1, name2]) != set(["Melpomene Murray", "Randy Schwartz"]):
        raise ValueError("Registered players' names should appear in standings, "
                         "even if they have no matches played.")
    print "6. Newly registered players appear in the standings with no matches."


def testReportMatches():
    deleteMatches()
    deletePlayers()
    registerPlayer("Bruno Walton")
    registerPlayer("Boots O'Neal")
    registerPlayer("Cathy Burton")
    registerPlayer("Diane Grant")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    standings = playerStandings()
    for (i, n, w, m) in standings:
        if m != 1:
            raise ValueError("Each player should have one match recorded.")
        if i in (id1, id3) and w != 1:
            raise ValueError("Each match winner should have one win recorded.")
        elif i in (id2, id4) and w != 0:
            raise ValueError("Each match loser should have zero wins recorded.")
    print "7. After a match, players have updated standings."


def testPairings():
    deleteMatches()
    deletePlayers()
    registerPlayer("Twilight Sparkle")
    registerPlayer("Fluttershy")
    registerPlayer("Applejack")
    registerPlayer("Pinkie Pie")
    standings = playerStandings()
    [id1, id2, id3, id4] = [row[0] for row in standings]
    reportMatch(id1, id2)
    reportMatch(id3, id4)
    pairings = swissPairings()
    if len(pairings) != 2:
        raise ValueError(
            "For four players, swissPairings should return two pairs.")
    [(pid1, pname1, pid2, pname2), (pid3, pname3, pid4, pname4)] = pairings
    correct_pairs = set([frozenset([id1, id3]), frozenset([id2, id4])])
    actual_pairs = set([frozenset([pid1, pid2]), frozenset([pid3, pid4])])
    if correct_pairs != actual_pairs:
        raise ValueError(
            "After one match, players with one win should be paired.")
    print "8. After one match, players with one win are paired."


if __name__ == '__main__':
    testDeleteMatches()
    testDelete()
    testCount()
    testRegisterTournament()
    testRegister()
    testRegisterToTournament()
    testRegisterCountDelete()
    testRegisterToTournamentCountDelete()
    #testStandingsBeforeMatches()
    #testReportMatches()
    #testPairings()
    print "Success!  All tests pass!"
    print "Repopulate"
    deleteMatches()
    deletePlayers()
    deleteTournaments()
    t1 = registerTournament("PingPongMasters 2016")
    p1 = registerPlayer("Melpomene Murray")
    p2 = registerPlayer("Randy Schwartz")
    rp1 = registerPlayerToTournament(p1, t1)
    rp2 = registerPlayerToTournament(p2, t1)
    print "Repopulate done"


