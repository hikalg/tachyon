# The Tachyon Rating Engine

Tachyon uses a simple algorithm to calculate a numerical value representing the relative skill of an entity.

An entity in Tachyon is what is commonly referred to as a player (individual), pre-defined team (for team-based), or a temporary group of players (drafted/matchmaking)

The equation to calculate an entity's rating is:
$$ x = x_{0} + psc $$
wheras:
- $x$ is the new rating of the entity
- $x_{0}$ is the old rating of the entity
- $p$ is the polarity of the change
- $s$ is the predefined scaling of the change
- $c$ is the amount of change applied to the rating

## $p$
<!-- TODO: Explain polarity algorithm -->

## $s$
<!-- TODO: Explain scaling -->
<!-- 
    - Predefining scaling (as before)
    - Dynamic scaling
      - Compare distance between ratings
      - Do math magic to calculate a sensible scaling
 -->