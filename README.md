# Photo-Demo
<del>First stage of automatic: Mouse Simulator</del>

# Environment Setup
### Platform
Unix-like system, with USB access[^1], is required. 

### gPhoto2 CLI and library

- Homebrew:

```sh
brew install gphoto2
brew install libgphoto2
```

- APT:

```sh
sudo apt install gphoto2
sudo apt install libgphoto2-6
```

### Python interface to gPhoto2
- pip

```sh
sudo pip3 install gphoto2
```

[^1]: Tested cannot detect camera on Ubuntu 20.04.5 LTS guest on Microsoft WSL1 on Windows10 Pro 22H2 host. 
