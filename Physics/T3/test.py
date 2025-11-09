import pygmt

region = [-43.35, -43.05, -23.05, -22.83]  # ~30x25 km
grid = pygmt.datasets.load_earth_relief(
    resolution="01s", region=region, registration="gridline"
)
fig = pygmt.Figure()
perspective = [135, 30]  # Vista clássica do Rio (sudeste, 30° de elevação)
fig.grdview(
    grid=grid,
    region=region + [0, 3500],
    projection="M18c",
    perspective=perspective,
    frame=["a", "z500f100"],
    zsize="4c",
    surftype="i",
    shading="+a45+nt0.8",
    cmap="geo",
    contourpen="0.3p,gray30",
)
fig.grdcontour(
    grid=grid,
    levels=100,  # a cada 100m
    annotation="500",  # anotar a cada 500m
    pen="0.4p,gray10",
    perspective=perspective,
)
fig.coast(
    resolution="f",
    shorelines=True,
    water="lightblue@80",  # água semi-transparente
    borders="1/0.6p,gray",
    perspective=perspective,
)
fig.colorbar(
    perspective=perspective,
    frame=["a500f100", "x+lElevação (m)", "y+lm"],
    position="JBC+o0c/1c+w14c/0.8c+h",
)
fig.text(
    text="Rio de Janeiro - Topografia 3D (30 m)",
    position="TC",
    font="18p,Helvetica-Bold,white",
    offset="0/0.8c",
    perspective=perspective,
    fill="black@90",  # fundo semi-transparente
)
fig.savefig("rio_3D_perfeito.png", dpi=600)
print("Mapa 3D salvo como 'rio_3D_perfeito.png' (600 DPI - pronto para impressão A1!)")
fig.show()
