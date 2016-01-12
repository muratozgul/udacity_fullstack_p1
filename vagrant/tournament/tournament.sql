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
  round       INTEGER NOT NULL,
  home_id     SERIAL  NOT NULL  REFERENCES tournament_players(id) ON DELETE CASCADE,
  away_id     SERIAL  NOT NULL  REFERENCES tournament_players(id) ON DELETE CASCADE CHECK(home_id <> away_id),
  winner_id      INTEGER NULL,
  is_complete BOOLEAN NOT NULL  DEFAULT false,
  is_bye      BOOLEAN NOT NULL  DEFAULT false,
  time        TIMESTAMP WITH TIME ZONE  NULL,
  created_at  TIMESTAMP WITH TIME ZONE  DEFAULT now(),
  updated_at  TIMESTAMP WITH TIME ZONE  DEFAULT now()
);

DROP VIEW IF EXISTS home_matches;

CREATE VIEW home_matches AS
  SELECT tournament_players.id as tp_id, matches.id
  FROM tournament_players
  LEFT JOIN matches
  ON tournament_players.id = matches.home_id
  GROUP BY tournament_players.id, matches.id;









