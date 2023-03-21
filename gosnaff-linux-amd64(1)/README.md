# gosnaff

## What is this?

It's like [Snaffler](https://github.com/SnaffCon/Snaffler) but ✨*multi-platform*✨.

## Key differences

At some point I'm gonna list them here, but for now read up on the source code.

Disadvantages from Snaffler:

- It doesn't use the fancy Windows DLLs so it can't do some of the same fancy stuff

Advantages over Snaffler:

- It doesn't use the dumb Windows DLLs so it will run on literally anything

## Why golang?

Because Python sucks at concurrency.
And C# still sucks at multiplatform distribution.
And Rust hurts my brain.
And Java is Java.

And Go is *cool* and *hip* and *with it*, okay!

## How to use

1. [Download the latest bundle](https://github.com/zxsecurity/gosnaff/releases) for your OS
2. `gosnaff -z generate`
3. Edit the config file so it's got what you need in it, and tweak the rules to your liking
4. `gosnaff -z your_config.toml`

*Alternatively:*

1. `go get github.com/zxsecurity/gosnaff`
2. Create a new working directory for gosnaff to operate out of
3. `gosnaff -z generate`
4. Edit the config file so it's got what you need in it
5. Optionally, copy the `rules` directory to the working directory and modify the rules
6. Make sure the config file points to the rules directory you want (either the path to gosnaff's defaults, or the custom rules you've implemented)
7. `gosnaff -z your_config.toml`

## Other notes

To make it easier for distribution, you can append all of the default rules together with:

```sh
find ./rules -name '*.toml' -exec sh -c 'cat {}; echo;' \; > all_rules.toml
```

If you want to run the output through some other tools afterwards (e.g [jq](...)), use `LogFileAsJsonLines = true` in your config file. Then you can do funky stuff like:

```sh
# Get all of the files that were rated with a `Black` triage level:
jq '. | select(.FindingType == "File") .Finding | select(.Triage == "Black") .Path' snaffle.json

# Get all Red/Black finding paths and contents:
jq '. | select(.FindingType == "File" or .FindingType == "Path") .Finding | select(.Triage == "Black" or .Triage == "Red") | {"Path": "\\\\\(.Server)\\\(.Share)\\\(.Path)", "Content": .MatchedContent}' snaffle.json
```

## Todo:

- [ ] Ensure that the dependency chain thing is actually robust
  - I think it's pretty good, but we'll see based on people's experiences with it
- [ ] Test it on Windows + other platforms that aren't x86_64 Linux
