# Installation Guides

Installing `graph-tool` can be tricky, but using `conda` makes it much easier. Here's how to do it on both Linux servers and macOS.

---

## 🐧 Linux Server (No Root Access)

If you're using a shared server and **don’t have root (admin) access**, the easiest way is to install `graph-tool` using **Miniconda**.

### Step 1: Install Miniconda

Download the installer:

```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

Run the installer:
```
bash Miniconda3-latest-Linux-x86_64.sh
```

Follow the prompts:

*   Accept the license agreement.
    
*   Choose an install location (e.g., `~/miniconda3`). The default is usually fine.
    
*   No need for `sudo`.
    

### Step 2: Initialize Conda

After installation, activate Conda by updating your `.bashrc`:

```
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

This ensures `conda` is available every time you open a terminal.


## 🍏 macOS (Apple Silicon)

If you're using a Mac with an Apple M-series chip, the easiest way to install Miniconda is through **Homebrew**.

### Step 1: Install Miniconda via Homebrew

brew install miniconda

After installation, make sure Homebrew has added Miniconda to your shell environment. If not, you may need to add this to your .zprofile or .zshrc:

```
export PATH="/opt/homebrew/Caskroom/miniconda/base/bin:$PATH"
```

### Step 2: Set Up graph-tool

Once Miniconda is installed and working, you can create a new environment and install graph-tool. These steps will depend on your system (Linux or macOS) and compatibility, so check the official guide:
📘 Official documentation 