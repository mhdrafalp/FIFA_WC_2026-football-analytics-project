# BEYOND 90 — FIFA WORLD CUP 2026 FOOTBALL INTELLIGENCE

An interactive football analytics and scouting intelligence project built around FIFA World Cup 2026 player-performance data.

**PROJECT OVERVIEW**

BEYOND 90 transforms FIFA World Cup 2026 player-performance data into meaningful football and scouting insights.

The project evaluates players across different positions, analyzes performance and efficiency, identifies potentially overlooked players, and presents the results through interactive Tableau dashboards.

The goal is to demonstrate how raw football data can be transformed into practical analytical insights that can support player comparison and scouting decisions.

**OBJECTIVES**

• Analyze FIFA World Cup 2026 player performance • Compare players across different positions • Identify high-performing players • Identify efficient players based on playing time and contribution • Discover potential hidden gems • Analyze attacking, midfield, defensive and goalkeeper performance • Compare individual players with tournament-level statistics • Build interactive football scouting dashboards • Present football data through clear visualizations

**DATASET**

The project uses player-level FIFA World Cup 2026 performance data containing more than 1,200 player records.

Player Information • Player name • Age • Position • Nationality

Playing Statistics • Minutes played • Games played • Goals • Assists • Key passes • Crosses • Dribbles

Defensive Statistics • Tackles • Interceptions • Blocks • Clearances

Goalkeeper Statistics • Saves • Save percentage • Clean sheets • Inside-box saves • Penalty saves

Performance • Player rating • Position-specific performance indicators

**TECHNOLOGIES**

Python Used for data loading, cleaning, preprocessing, missing-value handling and feature preparation.

SQL Used for data exploration, filtering, aggregation, player comparisons and analytical queries.

Tableau Used for interactive dashboards, player analysis, position-based analysis, efficiency analysis and scouting visualization.

Libraries • Pandas • NumPy

**PROJECT WORKFLOW**

Raw FIFA World Cup 2026 Dataset ↓ Data Cleaning ↓ Data Preprocessing ↓ Feature Preparation ↓ SQL Analysis ↓ Performance Analysis ↓ Player Categorization ↓ Hidden Gem Identification ↓ Tableau Visualization ↓ Football Intelligence ↓ Scouting Insights

**DASHBOARD PREVIEW**

The BEYOND 90 Tableau dashboards provide an interactive view of player performance, position-based statistics, efficiency and scouting insights.

Main Dashboard

![BEYOND 90 Main Dashboard](screenshots/Main_Dashboard.png)

Hidden Gems Dashboard

![Hidden Gems Dashboard](screenshots/Hiddengems.png)

Position-Based Statistics — Dashboard 1

![Position-Based Statistics Dashboard 1](screenshots/Player_Dashboard_1.png)

Position-Based Statistics — Dashboard 2

![Position-Based Statistics Dashboard 2](screenshots/Player_Dashboard_2.png)

**POSITION-BASED ANALYSIS**

Goalkeepers

• Saves • Save percentage • Clean sheets • Inside-box saves • Penalty saves • Games played • Player rating

Defenders

• Tackles • Interceptions • Blocks • Clearances • Minutes played • Player rating

Midfielders

• Key passes • Interceptions • Dribbles • Crosses • Minutes played • Player rating

Forwards

• Goals • Assists • Dribbles • Key passes • Crosses • Minutes played • Player rating

**KEY ANALYSES**

Player Performance Analysis

Players are evaluated using ratings, playing time and position-specific performance statistics.

Player Efficiency

Player contribution is evaluated relative to playing time. This provides a more balanced comparison than raw statistical totals alone.

Hidden Gems

The project identifies players who demonstrate strong performance indicators while receiving comparatively less attention than established high-profile players.

The analysis considers:

• Player rating • Playing time • Age • Position • Statistical contribution • Efficiency

Player Intelligence

Individual player dashboards allow users to explore:

• Player profile • Age • Position • Nationality • Minutes played • Position-specific statistics • Rating • Contribution metrics • Comparison with tournament-level statistics

**KEY QUESTIONS**

The project explores questions such as:

• Who were the highest-rated players? • Which players were the most efficient? • Which young players performed strongly? • Who are potential hidden gems? • How does performance differ across positions? • Which players contributed strongly despite limited playing time? • How does an individual player compare with tournament-level performance? • Which metrics are most useful for evaluating different positions?

**KEY INSIGHTS**

The project demonstrates how football performance data can be transformed into scouting-oriented insights.

The analysis considers more than traditional statistics such as goals and assists. It also examines:

• Efficiency • Defensive contribution • Creativity • Playing time • Player ratings • Age • Position-specific performance

Specific numerical findings from the final dashboards will be documented here.

**LIMITATIONS**

• The analysis is primarily based on FIFA World Cup 2026 tournament statistics. • Some players have limited playing time, which can affect efficiency comparisons. • Player ratings depend on the methodology used by the underlying dataset. • Statistical data cannot capture every aspect of a player's ability. • Tournament performance alone cannot guarantee future performance. • Market value and transfer-market information are not included in the current analysis. • The Hidden Gems classification is an analytical approach developed for this project and is not an official scouting evaluation.

**FUTURE IMPROVEMENTS**

• Historical tournament comparison • Club-level performance integration • Live player market-value integration • Multi-tournament player tracking • Player performance forecasting • Transfer-value prediction • Advanced machine-learning scouting models • Automated scouting recommendations

**PROJECT STRUCTURE**

football-analytics-project/
