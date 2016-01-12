-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

CREATE TABLE IF NOT EXISTS players (
  id          SERIAL  PRIMARY KEY,
  name        TEXT    NOT NULL,
  created_at  TIMESTAMP WITH TIME ZONE  DEFAULT now(),
  updated_at  TIMESTAMP WITH TIME ZONE  DEFAULT now()
);

CREATE TABLE IF NOT EXISTS tournaments (
  id          SERIAL  PRIMARY KEY,
  name        TEXT    NOT NULL,
  created_at  TIMESTAMP WITH TIME ZONE  DEFAULT now(),
  updated_at  TIMESTAMP WITH TIME ZONE  DEFAULT now()
);

CREATE TABLE IF NOT EXISTS tournament_players (
  id          SERIAL  PRIMARY KEY,
  tournament_id SERIAL  NOT NULL  REFERENCES tournaments(id) MATCH FULL ON DELETE CASCADE,
  player_id     SERIAL  NOT NULL  REFERENCES players(id) MATCH FULL ON DELETE CASCADE,
  created_at  TIMESTAMP WITH TIME ZONE DEFAULT now(),
  updated_at  TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TABLE IF NOT EXISTS matches (
  id          SERIAL  PRIMARY KEY,
  round       INTEGER NULL,
  winner_id   INTEGER  NOT NULL  REFERENCES tournament_players(id) ON DELETE CASCADE,
  loser_id    INTEGER  NULL  REFERENCES tournament_players(id) ON DELETE CASCADE CHECK(winner_id <> loser_id),
  time        TIMESTAMP WITH TIME ZONE  NULL,
  created_at  TIMESTAMP WITH TIME ZONE  DEFAULT now(),
  updated_at  TIMESTAMP WITH TIME ZONE  DEFAULT now()
);

DROP VIEW IF EXISTS registrations CASCADE;

CREATE VIEW registrations AS
  SELECT tournament_players.tournament_id AS tournament,
         tournament_players.id AS player, 
         players.name AS name
  FROM tournament_players LEFT JOIN players
  ON tournament_players.player_id = players.id
  GROUP BY tournament_players.id, players.name;


DROP VIEW IF EXISTS wins CASCADE;

CREATE VIEW wins AS
  SELECT registrations.tournament AS tournament, 
         registrations.player AS player,
         registrations.name AS name,
         count(matches.winner_id) AS wins
  FROM registrations LEFT JOIN matches
  ON registrations.player = matches.winner_id
  GROUP BY tournament, player, name;


DROP VIEW IF EXISTS losses CASCADE;

CREATE VIEW losses AS
  SELECT registrations.tournament AS tournament, 
         registrations.player AS player,
         registrations.name AS name,
         count(matches.loser_id) AS losses
  FROM registrations LEFT JOIN matches
  ON registrations.player = matches.loser_id
  GROUP BY tournament, player, name;


DROP VIEW IF EXISTS standings CASCADE;

CREATE VIEW standings AS
  SELECT wins.tournament AS tournament, 
         wins.player AS player,
         wins.name AS name,
         wins.wins AS wins,
         wins.wins + losses.losses AS matches
  FROM wins LEFT JOIN losses
  ON wins.tournament = losses.tournament
  AND wins.player = losses.player
  ORDER BY wins DESC, matches ASC, name ASC;





