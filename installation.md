# Installation Guides

Installing `graph-tool` can be tricky, but using [package manager](https://en.wikipedia.org/wiki/Package_manager#:~:text=A%20package%20manager%20or%20package,computer%20in%20a%20consistent%20manner.) such as `conda` makes it much easier. Here's how to do it on both Linux servers and macOS.

```{admonition} Why install graph-tool can be tricky? 
Installing `graph-tool` can be challenging because it relies heavily on C++ libraries like Boost and CGAL, which require compilation with exact Python bindings and compatible system dependencies. Unlike typical Python packages, `graph-tool` integrates a high-performance backend that needs to be compiled with features like OpenMP and Cairo, making it difficult to install via pip or in virtual environments. Official binary support is limited—especially on Windows—and manual compilation not only demands careful dependency management but also requires at least 3GB of RAM during the build process, which can be a barrier on resource-constrained systems.
```

---

## Linux Server (No Root Access)

If you're using a shared server and **don’t have root (admin) access**, the easiest way is to install `graph-tool` using **Miniconda**.

Download the installer:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Run the installer:
```bash
bash Miniconda3-latest-Linux-x86_64.sh
```

Follow the prompts:

*   Accept the license agreement.
    
*   Choose an install location (e.g., `~/miniconda3`). The default is usually fine.
    
*   No need for `sudo`.
    


After installation, activate Conda by updating your `.bashrc`:

```bash
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

This ensures `conda` is available every time you open a terminal.


## macOS (Apple Silicon)

If you're using a Mac with an Apple M-series chip, the easiest way to install Miniconda is through **[Homebrew](https://brew.sh/)**.


```bash
brew install miniconda
```

After installation, make sure Homebrew has added Miniconda to your shell environment. If not, you may need to add this to your .zprofile or .zshrc:

```bash
export PATH="/opt/homebrew/Caskroom/miniconda/base/bin:$PATH"
```

## Install `graph-tool` using conda

The following code creates a new Conda environment named `gt` and installs the `graph-tool` package from the `conda-forge` channel:

```bash
conda create --name gt -c conda-forge graph-tool
conda activate gt
```
