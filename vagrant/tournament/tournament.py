#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2 as pg

DB_NAME = "tournament"
TOURNAMENT_ID = 1

def connect(dbName=DB_NAME):
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return pg.connect("dbname=" + dbName)


def query(SQL, dbName=DB_NAME):
    db = connect(dbName)
    c = db.cursor()
    c.execute(SQL)
    db.commit()
    db.close()
    return


def deleteMatchesOfTournament(tournament_id):
    """Remove the match records of a tournament from the database."""
    SQL = "DELETE FROM matches WHERE tournament_id = %s" % tournament_id
    query(SQL)


def deleteMatches():
    """Remove all the match records of a tournament from the database."""
    SQL = "DELETE FROM matches"
    query(SQL)


def deletePlayersOfTournament(tournament_id):
    """Remove the player records registered to a tournament from the database."""
    SQL = "DELETE FROM tournament_players WHERE tournament_id = %s" % tournament_id
    query(SQL)


def deletePlayers():
    """Remove all the player records from the database."""
    SQL = "DELETE FROM players"
    query(SQL)


def deleteTournaments():
    """Remove all tournaments records from the database."""
    SQL = "DELETE FROM tournaments"
    query(SQL)


def countTournaments():
    """Returns the number of all tournaments."""
    SQL = "SELECT count(id) FROM tournaments"
    db = connect()
    c = db.cursor()
    c.execute(SQL)
    result = c.fetchall()
    db.close()
    print "count tournaments: %s" % result
    assert len(result) == 1
    return int(result[0][0])


def countPlayers():
    """Returns the number of all known players."""
    SQL = "SELECT count(id) FROM players"
    db = connect()
    c = db.cursor()
    c.execute(SQL)
    result = c.fetchall()
    db.close()
    print "count players: %s" % result
    assert len(result) == 1
    return int(result[0][0])


def countPlayersOfTournament(tournament_id):
    """Returns the number of players currently registered to a tournament."""
    rawSQL = "SELECT count(id) FROM tournament_players WHERE tournament_id = {tournament_id}"
    SQL = rawSQL.format(tournament_id=tournament_id)
    db = connect()
    c = db.cursor()
    c.execute(SQL)
    result = c.fetchall()
    db.close()
    print "count tournament players: %s" % result
    assert len(result) == 1
    return int(result[0][0])


def registerTournament(name):
    """Adds a tournament to the tournament database.
  
    The database assigns a unique serial id number for the tournament.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the tournament name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    SQL = "INSERT INTO tournaments (name) VALUES (%s) RETURNING (id)"
    c.execute(SQL, (name,))
    result = c.fetchone()[0]
    print "Tournament created with id: %s" % result
    db.commit()
    db.close()
    return result


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()
    SQL = "INSERT INTO players (name) VALUES (%s) RETURNING (id)"
    c.execute(SQL, (name,))
    result = c.fetchone()[0]
    print "Player created with id: %s" % result
    db.commit()
    db.close()
    return result


def registerPlayerToTournament(player_id, tournament_id):
    SQL = """
    INSERT INTO tournament_players (player_id, tournament_id)
    VALUES (%s, %s) RETURNING (id)
    """
    db = connect()
    c = db.cursor()
    c.execute(SQL, (player_id, tournament_id))
    result = c.fetchone()[0]
    db.commit()
    db.close()
    return result


def playerStandings(tournament_id):
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


