#panel convert script.py --to pyodide-worker --out pyodide

import bokeh
import numpy as np
import panel as pn
import holoviews as hv

button = pn.widgets.Button(name='Generate Points in Frequency Space', button_type='primary')
plot = pn.pane.HoloViews()

def sine_fs(F, X, period):
    Y = np.zeros(X.shape)
    for n, coeff in enumerate(F):
        Y += (coeff)*(np.sin(2*n*np.pi*X/period))
    return np.array([X, Y]).T

def cosine_fs(F, X, period):
    Y = np.zeros(X.shape)
    for n, coeff in enumerate(F):
        Y += (coeff)*(np.cos(2*n*np.pi*X/period))
    return np.array([X, Y]).T

def gen(event):
    hv.extension("plotly")
    coeff = np.random.randn(6, 5)

    x = np.linspace(-3, 3, 1000)
    sines = {ind: hv.Curve(sine_fs(F, x, 2)) for ind, F in enumerate(coeff)}
    cosines = {ind: hv.Curve(cosine_fs(F, x, 2)) for ind, F in enumerate(coeff)}
    
    fvs = hv.Scatter3D(coeff, kdims=["n=1", "n=2", "n=3"], vdims=["color", "size"]).opts(color=hv.dim("color"), size=np.abs(hv.dim("size"))*100, cmap="afmhot", width=400, height=400)

    hmap_s = hv.HoloMap(sines, kdims='curves', group="temporal waves", label="sine curves").opts(width=300, height=300)
    hmap_c = hv.HoloMap(cosines, kdims='curves', group="temporal waves", label="cosine curves").opts(width=300, height=300)

    plot.object = hv.Layout([fvs, hmap_s * hmap_c]).cols(2)
    plot.widget = {"curves": {"value": 0}}
    plot.widget_location = "top"
    
button.on_click(gen)
gen(None)
app = pn.Column(button, plot.layout).servable()