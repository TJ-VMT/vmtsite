# TJ VMT Website

This is the official repository of the TJHSST Varsity Math Team website.  The official site can be found [here](https://activities.tjhsst.edu/vmt/).

## Contact

If you have any questions or concerns, please either file a bug report or email VMT [officers](mailto:vmtofficers@gmail.com).

## Install
Making a python virtual enviornment is highly recommended, note that python3 is required. Sample method of creating a virtualenv is shown below:

```bash
python3 -m venv /path/to/virtual/environment
```

Everytime you need to make new changes:
```bash
source /path/to/virtual/environment/bin/activate
```

First you have to install the following packages:

```bash
pip3 install pelican Markdown typogrify ghp-import
```

## Make Changes
Currently, the pages are written in ReStructuredText, but you can use Markdown if you wish. Tutorials for either markup languages can be easily found online.

After you make approapiate changes, use the following commands to build and test the website:

```bash
make html
make serve
```

Once you feel confident in the new changes first update the source code on branch `master`:

```bash
git push origin master
```

Then publish the website (the website is under branch `web`):

```bash
make github
```

Finally update on TJ server:
```bash
git pull origin web
```


## Documentation

For details, please consult the lastest pelican documentation at [here](http://docs.getpelican.com/en/stable).

Doumentation on theme-specific details is under the `theme` folder; note that several redundant CSS files were removed for sake of compactness.
