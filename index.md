# Welcome to the Graph-Tool Tutorial

Welcome to this website dedicated to learning and exploring the [`graph-tool`](https://graph-tool.skewed.de/) package!

This site is built using [Sphinx](https://www.sphinx-doc.org/en/master/), a flexible documentation generator, along with [MyST-NB](https://myst-nb.readthedocs.io/), which allows seamless integration of Jupyter notebooks into Sphinx.

```{toctree}
:maxdepth: 1
installation

```

```{toctree}
:maxdepth: 2
:caption: Basics

basics/basics
basics/graph_plotting
```

```{toctree}
:maxdepth: 2
:caption: Cookbook

cookbook/intro
cookbook/inference-undirected-graphs
cookbook/topsbm
```

```{toctree}
:maxdepth: 2
:caption: Use Cases

use_cases/degree_distribution_visualization
use_cases/centrality
use_cases/random_graphs_generation
use_cases/null_models



```

_Last updated on: {{ last_updated }}_