# envsync

envsync is a command-line tool that keeps the `.env` file on your machine in sync with the environment variables of a project on the config server. `envsync pull` downloads the latest values. `envsync push` uploads your values.

## Install

envsync needs Node 20 or newer. It does not start on Node 18.

```
npm install -g envsync-cli
```

## First use

1. Open the web UI of the config server. Get a token under Profile > Tokens.
2. Put the token in the `ENVSYNC_TOKEN` environment variable.

   ```
   export ENVSYNC_TOKEN=<your token>
   ```

3. Go to the project folder and run `envsync init`. The command asks for the project name and writes `.envsync.json`.
4. Commit `.envsync.json`. It holds only the project name and the server URL, and no secrets.
5. Run `envsync pull`. The command downloads the values of the project and writes `.env`.

envsync reads and writes only the `.env` file in the folder that holds `.envsync.json`.

## Before you push

`envsync push` replaces the values on the server with the values in your `.env`. It does not merge. Each person on the team gets your values on their next pull.

- Run `envsync diff` before each push to see which keys differ.
- Run `envsync push --dry-run` to see what the push would change. It writes nothing.
- `envsync push` refuses an empty `.env`.

The server keeps the last 20 versions of the values for each project. If a push was wrong, use `envsync history` and `envsync restore <version>` to put an earlier version back.

## Commands

| Command | What it does |
|---|---|
| `envsync init` | Asks for the project name and writes `.envsync.json`. |
| `envsync pull` | Downloads the values of the project and writes `.env`. |
| `envsync push` | Uploads your `.env` and replaces the values on the server. |
| `envsync diff` | Shows the names of the keys that differ between `.env` and the server. |
| `envsync history` | Lists the versions that the server keeps for the project. |
| `envsync restore <version>` | Puts one version back on the server. |

### pull

- `envsync pull` writes `.env` with file mode 600, so other users on the machine cannot read it.
- If `.env` has local changes that are not on the server, `envsync pull` stops with exit code 3. It changes nothing. Run `envsync diff` to see the keys that differ. When a pull seems to do nothing, this conflict is the usual cause.
- `envsync pull --force` overwrites the local file. It first saves the old file as `.env.bak`.
- `envsync pull --dry-run` prints what would change and writes nothing.

### diff

`envsync diff` prints key names only, because people share their screens. To print the values too, use `envsync diff --show`.

### restore

`envsync restore <version>` is a push. It replaces the values that are on the server now, and the team gets them on the next pull.

## Keys that stay local

List a key in `.envsyncignore` to keep it on your machine only. Write one key per line. envsync never pushes a listed key, and `envsync pull` never overwrites it. Use this file for values that belong to one machine, such as local ports.

## Use in CI

Use `envsync pull --ci` in a CI job.

- With `--ci`, the command never prompts.
- With `--ci`, the command fails with exit code 5 if `.envsync.json` is missing.
- CI tokens are read-only. A push from CI always fails with exit code 2. This behavior is deliberate.
- envsync uses `HTTPS_PROXY` if your runners are behind a proxy.

## Reference

### Exit codes

| Code | Meaning |
|---|---|
| 2 | The token is missing or expired, or a read-only CI token tried to push. The command prints `not authenticated`. |
| 3 | Conflict. `.env` has local changes that are not on the server, and `envsync pull` changed nothing. |
| 4 | A value is larger than 64 KB and the server rejected the push. The message names the key. |
| 5 | `envsync pull --ci` did not find `.envsync.json`. |

### Limits

- One value can be 64 KB at most.
- One project can hold 500 keys at most.
- One project has one set of values. You cannot keep different values for each branch. Environments may come later, but they are not planned yet.
- envsync does not support `.env.local`.

### Server URL

envsync uses the config server of the company by default. To use a different server, pass `--server` or set the URL in `.envsync.json`.

### Platforms

envsync works on macOS, Linux, and Windows. On Windows, we tested it only in WSL. Native PowerShell may work, but we did not test it.

### Telemetry

envsync collects no telemetry.

## Update

```
npm update -g envsync-cli
```

envsync prints a notice when a newer version exists. It does not update itself.

## License

MIT
