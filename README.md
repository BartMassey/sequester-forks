# sequester-forks: Move forked projects into separate Github org
Bart Massey 2021

**This code comes with absolutely no warranty, and is
probably too dangerous to try to run on your precious
repos. It worked for me, but I feel lucky that I lost
nothing in the process.**

So I ended up with 47 projects sitting in my personal
repository that were just forks of projects that I had PRs
out for at one point. This was annoying, as it was getting
to be about 1/5 of my total repos. I decided to move the
projects to a separate `BartMassey-upstream` Github
organization and do future forking into there. That way I
could keep my stuff and other people's stuff straight.

This tiny Python program makes use of the excellent
`PyGithub` to comb through my repos and transfer the ones
that are forks of other people's code. It reads my Github
OAuth token from `~/.github-oauthtoken` and my Github
username from `~/.github-username`. Run it with the name of
the organization you want to transfer to as the command-line
argument.

The repository transfer call hasn't yet been added to
`PyGithub`. However, there is a
[PR](https://github.com/PyGithub/PyGithub/pull/1749) waiting
to be completed for this, so I pulled the code from the PR
and monkey-patched it into
`github.Repository.Repository`. Ugly, but works for now.

This program is licensed under the "MIT License". Please see
the file `LICENSE` in this distribution for license terms.
