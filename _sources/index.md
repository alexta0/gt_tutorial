# Welcome to the Graph-Tool Tutorial

Welcome to this website dedicated to learning and exploring the [`graph-tool`](https://graph-tool.skewed.de/) package!

This site is built using [Sphinx](https://www.sphinx-doc.org/en/master/), a flexible documentation generator, along with [MyST-NB](https://myst-nb.readthedocs.io/), which allows seamless integration of Jupyter notebooks into Sphinx. That means **you can contribute using plain Jupyter notebooks or Markdown**, without worrying about complex tooling — just focus on writing and experimenting. 

We'd love to have you contribute to this tutorial, whether it's fixing a typo, adding a new example, or sharing a neat trick you've discovered. The Github repository for this website can be found [here](https://github.com/alexta0/gt_tutorial). 

---

## 📚 What's Inside

This tutorial is organized into three main parts:

1. **Getting Started with `graph-tool`**  
   A gentle introduction to the basic API and programming patterns — perfect if you're new to the library.

2. **Stochastic Block Model (SBM) Recipes**  
   A collection of practical examples showing how to use `graph-tool` for Bayesian inference using stochastic block models.

3. **Use Cases & Tips**  
   Handy guides for common tasks like generating random graphs, along with some performance tricks and real-world examples.

Let’s dive in and start exploring networks the `graph-tool` way!


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