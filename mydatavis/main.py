import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

df = pd.read_csv("pokemon.csv")

# Top 10 pokemon  by Attack for each Type
top_pokemon_by_type = df.groupby("Type 1").apply(lambda x: x.nlargest(10, "Attack")).reset_index(drop=True)

# Top 10 pokemon  by Speed
top_speed_pokemon = df.nlargest(10, "Speed")

# Scatter plot for Attack vs Defense
scatter = go.Scatter(
    x=df["Attack"],
    y=df["Defense"],
    mode="markers",
    marker=dict(color='rgba(135, 206, 235, 0.8)', size=10, line=dict(width=1, color='rgba(0, 0, 0, 0.5)')),
    text=df["Name"],
    hoverinfo="text",
    name="Attack vs Defense"
)

# a color for each pokemon type 
type_colors = {type_name: color for type_name, color in zip(df['Type 1'].unique(), px.colors.qualitative.Set1)}

# subplots: 1 row, 3 columns
fig = make_subplots(
    rows=1, 
    cols=3, 
    subplot_titles=[
        "Top Pokémon by Attack for All Types", 
        "Attack vs. Defense",
        "Top 10 Pokémon by Speed"
    ]
)

# bar chart for top 10 Pokemon of each type
fig.add_trace(
    go.Bar(
        x=top_pokemon_by_type["Name"],
        y=top_pokemon_by_type["Attack"],
        marker_color=top_pokemon_by_type["Type 1"].map(type_colors),
        text=top_pokemon_by_type["Attack"],
        textposition='auto',
        hoverinfo="text",
        hovertext=[f"{name}<br>Attack: {attack}" for name, attack in 
                  zip(top_pokemon_by_type["Name"], top_pokemon_by_type["Attack"])]
    ),
    row=1, col=1
)

# attack vs defence scatter plot
fig.add_trace(
    scatter,
    row=1, col=2
)

# top 10 pokemon by speed
fig.add_trace(
    go.Bar(
        x=top_speed_pokemon["Name"],
        y=top_speed_pokemon["Speed"],
        marker_color='orange',  # Customize color for speed
        text=top_speed_pokemon["Speed"],
        textposition='auto',
        hoverinfo="text",
        hovertext=[f"{name}<br>Speed: {speed}" for name, speed in 
                  zip(top_speed_pokemon["Name"], top_speed_pokemon["Speed"])]
    ),
    row=1, col=3
)


fig.update_layout(
    title_text="Top Pokémon by Attack, Attack vs Defense, and Top 10 by Speed",
    height=600,
    width=1800,
    showlegend=False
)

# update axis
fig.update_xaxes(tickangle=45, row=1, col=1)
fig.update_xaxes(title="Attack", row=1, col=2)
fig.update_xaxes(title="Speed", row=1, col=3)
fig.update_yaxes(title="Defense", row=1, col=2)

# Show the plot
fig.show()