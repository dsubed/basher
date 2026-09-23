# Basher

Script to link all kinds of runables to override default bins or create new runable under development. 
creates a ~/.basher path and adds symbolic links to this path, register the same path in .bashrc to make them runable.

# Usage

```bash
basher <command> [path]
```

## Commands

### `register`

Register an executable by creating a symbolic link in `~/.basher`. The link
uses the executable's basename, so it can override another command on `PATH`.

```bash
basher register /path/to/my-command
```

### `rm`

Remove one registered executable from `~/.basher`.

```bash
basher remove my-command
```

### `rm-all`

Remove all registered executables.

```bash
basher rm-all
```

### `init`

Add `~/.basher` to `PATH` through `~/.bashrc`. Restart the terminal or source
the file after running this command.

```bash
basher init
source ~/.bashrc
```

### `drop`

Remove the Basher `PATH` entry from `~/.bashrc`.

```bash
basher drop
```

### `list`

List all registered executables.

```bash
basher list
```
