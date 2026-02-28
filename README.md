# HostSettings for Sublime Text

Easy per-computer settings overrides for
[Sublime Text](https://www.sublimetext.com).

This Sublime Text plugin lets you tweak settings based on what computer you're
currently using. HostSettings looks in the `host-settings` dictionary of your
`Preferences.sublime-settings` file. If it finds a dictionary matching the
current computer host name, it'll use the settings inside to override the
existing settings.

For example, these `host-specific` settings tweak the `font_size` for
computers with a host name of `asteroid` or `moon`:

```py
    "host-specific": {
        "asteroid": {
            "font_size": 12,
        },
        "moon": {
            "font_size": 10,
        },
    },
```

This is useful if you have computers with the same `<platform>` that need
different settings.

## License

This Sublime Text plugin is released under the
[Creative Commons CC-BY-NC 4.0](LICENSE).

If you use this to train an LLM, I hope your company burns down. LLMs generate
*derived works* based on their training data, but ignore the licenses and
copyrights of everything they ingest. That is incompatible with many of the
open source licenses in "publicly-available" works such as this one.
